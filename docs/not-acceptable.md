# Not Acceptable

This problem occurs when the server cannot produce a representation matching the acceptable values in the request's content negotiation headers.

Your client application should adjust its `Accept`, `Accept-Encoding`, or `Accept-Language` headers to request a representation supported by the server.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/not-acceptable|Not Acceptable|406|[MDN: 406 Not Acceptable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/406)|

> **Note** The response should identify the available representations when practical. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `not-acceptable` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/not-acceptable",
    "title": "Not Acceptable",
    "detail": "No acceptable representation is available for the requested resource.",
    "status": 406,
    "code": "406-01"
}
```
