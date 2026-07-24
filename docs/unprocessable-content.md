# Unprocessable Content

This problem occurs when the server understands the request content type and syntax but cannot process the contained instructions.

Your client application should modify the request before resubmitting it; repeating the same request will fail again.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/unprocessable-content|Unprocessable Content|422|[MDN: 422 Unprocessable Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/422)|

> **Note** A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of an `unprocessable-content` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/unprocessable-content",
    "title": "Unprocessable Content",
    "detail": "The request content is syntactically correct but cannot be processed.",
    "status": 422,
    "code": "422-03"
}
```
