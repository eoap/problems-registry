# Conflict

This problem occurs when a request conflicts with the current state of the target resource, such as a concurrent update or version conflict.

Your client application should inspect the problem details, resolve the conflict, and then resubmit the request.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/conflict|Conflict|409|[MDN: 409 Conflict](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/409)|

> **Note** A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `conflict` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/conflict",
    "title": "Conflict",
    "detail": "The request conflicts with the current state of the target resource.",
    "status": 409,
    "code": "409-01"
}
```
