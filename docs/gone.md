# Gone

This problem occurs when the requested resource is no longer available at the origin server and the condition is likely to be permanent.

Your client application should not repeat the request and should remove or replace references to the resource. If it is unknown whether the condition is permanent, use `404 Not Found` instead.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/gone|Gone|410|[MDN: 410 Gone](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/410)|

> **Note** A `410 Gone` response is cacheable by default. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `gone` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/gone",
    "title": "Gone",
    "detail": "The requested resource is no longer available and is unlikely to be available again.",
    "status": 410,
    "code": "410-01"
}
```
