# Method Not Allowed

This problem occurs when the server recognizes the request method but the target resource does not support it.

Your client application should use one of the methods advertised by the server in the `Allow` response header.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/method-not-allowed|Method Not Allowed|405|[MDN: 405 Method Not Allowed](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/405)|

> **Note** A `405 Method Not Allowed` response must include an `Allow` header listing the methods supported by the target resource. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `method-not-allowed` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/method-not-allowed",
    "title": "Method Not Allowed",
    "detail": "The request method is not supported by the target resource.",
    "status": 405,
    "code": "405-01"
}
```
