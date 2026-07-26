# Request Timeout

This problem occurs when the server stops waiting to receive a request on an idle or incomplete connection.

Your client application may repeat the request using a new connection.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/request-timeout|Request Timeout|408|[MDN: 408 Request Timeout](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/408)|

> **Note** A server should send `Connection: close` because this status indicates that it has decided to close the connection. A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience.

**Example of a `request-timeout` problem detail:**

```json
{
    "type": "https://eoap.github.io/problems-registry/request-timeout",
    "title": "Request Timeout",
    "detail": "The server timed out while waiting to receive the request.",
    "status": 408,
    "code": "408-01"
}
```
