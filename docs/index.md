# EOAP Problem Details Registry

This registry acts as a well-known location for problem detail types returned by various EOAP APIs. It acts as a central registry to promote reuse and clarity of problem detail types conforming to [RFC 9457](https://www.rfc-editor.org/info/rfc9457), formerly [RFC 7807](https://www.rfc-editor.org/info/rfc7807).

## EOAP Problem Types

| Problem type | Description |
|--------------|-------------|
| [Already Exists](already-exists.md) | The request attempted to create a resource that already exists. |
| [Missing Body Property](missing-body-property.md) | The request is missing an expected body property. |
| [Missing Request Header](missing-request-header.md) | The request lacked an expected header. |
| [Missing Request Parameter](missing-request-parameter.md) | The request is missing a query or path parameter. |
| [Invalid Body Property Format](invalid-body-property-format.md) | One or more of the body properties was malformed. |
| [Invalid Request Parameter Format](invalid-request-parameter-format.md) | One or more of the query or path parameters was malformed. |
| [Invalid Request Header Format](invalid-request-header-format.md) | One or more of the request headers was malformed. |
| [Invalid Body Property Value](invalid-body-property-value.md) | One or more of the body property values are invalid. |
| [Invalid Request Parameter Value](invalid-request-parameter-value.md) | One or more of the query or path parameter values are invalid. |
| [Validation Error](validation-error.md) | The request is invalid and deemed unprocessable. |
| [Business Rule Violation](business-rule-violation.md) | The request is deemed invalid as it failed business rule checks. |
| [License Expired](license-expired.md) | The client license has expired, rendering the service unavailable. |
| [License Cancelled](license-cancelled.md) | The client license has been cancelled, rendering the service unavailable. |

## Common Problem Types

The following types can also be leveraged for convenience; however, the recommendation is to utilize the [IANA registry](https://www.iana.org/assignments/http-problem-types/http-problem-types.xhtml) for generic/common types.

| Problem type | Description |
|--------------|-------------|
| [Bad Request](bad-request.md) | The client request is invalid or malformed. |
| [Forbidden](forbidden.md) | The request is not authorized for the resource. |
| [Invalid Parameters](invalid-parameters.md) | One or more of the parameters was malformed. |
| [Not Found](not-found.md) | The requested resource could not be found. |
| [Service Unavailable](service-unavailable.md) | The requested service is currently unavailable. |
| [Server Error](server-error.md) | The server encountered an unexpected error. |
| [Unauthorized](unauthorized.md) | The client request missed or malformed its credentials. |

When necessary, a Problem Detail response *MAY* include additional detail on the problems that have occurred. The additional errors **MUST** be under the `errors` collection, which itself follows the JSON Schema defined in our [GitHub repo](https://github.com/eoap/problems-registry).

## Python Usage

Install the package in an environment with Pydantic 2:

```bash
pip install eoap-problems-registry
```

Use the generated models to build responses with fixed registry fields and optional extension members:

```python
import eoap_problems_registry as registry

problem = registry.MissingRequestParameter(
    instance="https://api.example.test/problems/abc123",
    code="400-03",
    errors=[
        registry.ErrorDetail(
            detail="The query parameter limit is required.",
            parameter="limit",
        )
    ],
    correlation_id="req-123",
)

payload = problem.model_dump(mode="json", exclude_none=True)
```

The resulting payload includes the registered `type`, `status`, `title`, and `detail` values:

```json
{
  "instance": "https://api.example.test/problems/abc123",
  "code": "400-03",
  "errors": [
    {
      "detail": "The query parameter limit is required.",
      "parameter": "limit"
    }
  ],
  "type": "https://eoap.github.io/problems-registry/missing-request-parameter",
  "status": 400,
  "title": "Missing request parameter",
  "detail": "The request is missing an expected query or path parameter.",
  "correlation_id": "req-123"
}
```

`ProblemDetails` and `ErrorDetail` allow additional provider-specific fields, while generated problem classes use Pydantic literal fields to protect the registered `type`, `status`, `title`, and `detail` values.
