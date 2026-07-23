# EOAP Problems Registry

[![PyPI - Version](https://img.shields.io/pypi/v/eoap-problems-registry.svg)](https://pypi.org/project/eoap-problems-registry)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/eoap-problems-registry.svg)](https://pypi.org/project/eoap-problems-registry)

[EOAP Problems Registry](https://eoap.github.io/problems-registry/) is a shared registry of API problem detail types for EOAP services. The problem responses conform to [RFC 9457](https://www.rfc-editor.org/info/rfc9457), formerly [RFC 7807](https://www.rfc-editor.org/info/rfc7807), and are published as documentation, JSON Schema/OpenAPI artifacts, and a Python package with generated Pydantic models.

The registry is intended to give API providers and consumers a common vocabulary for reusable `application/problem+json` responses.

## What Is Included

- `schemas/schema.yaml`: JSON Schema definitions for the common `ProblemDetails`, `ErrorDetail`, and each registered EOAP problem type.
- `schemas/openapi.yaml`: reusable OpenAPI 3.1 response components and examples that reference the JSON Schema definitions.
- `src/eoap_problems_registry`: generated Pydantic models for the registry.
- `docs/`: MkDocs pages for each problem type, plus generated JSON Schema and OpenAPI documentation.
- `tests/`: unit tests that verify generated problem models and extension behavior.
- `.github/workflows/`: documentation deployment, package CI, and PyPI release automation.

## Registered Problems

EOAP-specific problem types:

| Problem type | HTTP status |
| --- | --- |
| Already Exists | 409 |
| Missing Body Property | 400 |
| Missing Request Header | 400 |
| Missing Request Parameter | 400 |
| Invalid Body Property Format | 400 |
| Invalid Request Parameter Format | 400 |
| Invalid Request Header Format | 400 |
| Invalid Body Property Value | 400 |
| Invalid Request Parameter Value | 400 |
| Validation Error | 422 |
| Business Rule Violation | 422 |
| License Expired | 503 |
| License Cancelled | 503 |

Common convenience problem types:

| Problem type | HTTP status |
| --- | --- |
| Bad Request | 400 |
| Unauthorized | 401 |
| Forbidden | 403 |
| Gone | 410 |
| Not Found | 404 |
| Invalid Parameters | 400 |
| Server Error | 500 |
| Service Unavailable | 503 |

For generic/common HTTP problem types, prefer the [IANA HTTP Problem Types registry](https://www.iana.org/assignments/http-problem-types/http-problem-types.xhtml) when it fits your use case.

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

## Schemas And OpenAPI

Use the schema and OpenAPI files directly when integrating the registry into API descriptions:

- JSON Schema definitions: [`schemas/schema.yaml`](schemas/schema.yaml)
- OpenAPI response components and examples: [`schemas/openapi.yaml`](schemas/openapi.yaml)
- Published documentation: <https://eoap.github.io/problems-registry/>

When a response needs more context, include an `errors` array. Each item must contain `detail` and may include `pointer`, `parameter`, `header`, `code`, or provider-specific extension fields.

## Development

This repository uses Hatch for Python environments, Ruff for formatting/linting, MkDocs for documentation, and Taskfile tasks for generated artifacts.

Useful commands:

```bash
hatch run test:test
hatch run test:testv
hatch run test:cov
hatch run dev:lint
hatch run dev:check
task process_schema
task generate_openapi_docs
task serve_docs
```

`task process_schema` regenerates the Pydantic models in `src/eoap_problems_registry/__init__.py` and the JSON Schema documentation in `docs/json-schema.md`.

`task generate_openapi_docs` regenerates the static OpenAPI documentation under `docs/openapi/`.

`task serve_docs` starts the MkDocs site locally.

## Contributing Problem Types

To add or update a problem type:

1. Update `schemas/schema.yaml` with the JSON Schema definition under `$defs`.
2. Update `schemas/openapi.yaml` if the problem should be exposed through reusable OpenAPI response components or examples.
3. Add or update the matching Markdown page in `docs/`.
4. Add the page to the `nav` section in `mkdocs.yaml`.
5. Run `task process_schema` to regenerate the Python models and schema docs.
6. Run `task generate_openapi_docs` if OpenAPI components or examples changed.
7. Add or update tests in `tests/` when generated behavior changes.
8. Run the test and lint commands before opening a pull request.

Problem type URIs should use the published registry base URL:

```text
https://eoap.github.io/problems-registry/{problem-name}
```

Use hyphen-separated names for problem page filenames and URI suffixes, for example `missing-body-property`.

## CI And Releases

The package workflow runs Ruff and the unit test suite on Python 3.10 through 3.14 for pushes and pull requests targeting the active development branches. Version tags matching `v*.*.*` build and publish the package to PyPI after verifying that the tag version matches `hatch version`.

The docs workflow publishes the MkDocs site to GitHub Pages when documentation-related files change on `docs`, `develop`, or `main`.

## License

[![Apache License, Version 2.0](https://img.shields.io/badge/license-Apache%20License%202.0-blue)](https://www.apache.org/licenses/LICENSE-2.0)
