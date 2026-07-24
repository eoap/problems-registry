# Failed Dependency

This problem occurs when the requested action cannot be performed because another action on which it depends has failed.

Your client application should resolve the failed prerequisite before retrying the request.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/failed-dependency|Failed Dependency|424|[MDN: 424 Failed Dependency](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/424)|

> **Note** This status originated with WebDAV and is generally used when the dependency between actions is explicit. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `failed-dependency` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/failed-dependency",
    "title": "Failed Dependency",
    "detail": "The requested action failed because an action on which it depended failed.",
    "status": 424,
    "code": "424-01"
}
```
