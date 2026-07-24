# Insufficient Storage

This problem occurs when the server lacks the storage or other capacity required to complete the requested action.

Your client application may retry later after server capacity becomes available.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/insufficient-storage|Insufficient Storage|507|[MDN: 507 Insufficient Storage](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/507)|

> **Note** This condition is temporary and differs from `413 Content Too Large`, which concerns the size of the request rather than current server capacity. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of an `insufficient-storage` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/insufficient-storage",
    "title": "Insufficient Storage",
    "detail": "The server has insufficient storage to complete the requested action.",
    "status": 507,
    "code": "507-01"
}
```
