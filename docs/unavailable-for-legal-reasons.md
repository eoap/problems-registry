# Unavailable For Legal Reasons

This problem occurs when the requested resource cannot be provided because of a legal demand or restriction.

Your client application cannot access the resource while the legal restriction remains in effect.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/unavailable-for-legal-reasons|Unavailable For Legal Reasons|451|[MDN: 451 Unavailable For Legal Reasons](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/451)|

> **Note** A `Link` header with `rel="blocked-by"` may identify the entity implementing the blockage. Information about the party responsible for the legal demand belongs in the response body. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of an `unavailable-for-legal-reasons` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/unavailable-for-legal-reasons",
    "title": "Unavailable For Legal Reasons",
    "detail": "The requested resource is unavailable due to legal reasons.",
    "status": 451,
    "code": "451-01"
}
```
