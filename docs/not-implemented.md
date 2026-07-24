# Not Implemented

This problem occurs when the server does not support the functionality required to fulfill the request.

Your client application may retry after the server adds support, or use alternative functionality when available.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/not-implemented|Not Implemented|501|[MDN: 501 Not Implemented](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/501)|

> **Note** Use `501 Not Implemented` when the method or functionality is not supported by the server at all. Use `405 Method Not Allowed` when the method is recognized but disallowed for a specific resource. A `501` response is cacheable by default. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `not-implemented` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/not-implemented",
    "title": "Not Implemented",
    "detail": "The server does not support the functionality required to fulfill the request.",
    "status": 501,
    "code": "501-01"
}
```
