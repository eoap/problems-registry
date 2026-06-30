# Server Error

This problem occurs when the server encounters an unexpected condition that prevents it from fulfilling the request.

Your client application did everything correct. Unfortunately our API encountered a condition that resulted in this problem.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/server-error|See HTTP Status Code|N/A|[RFC9457](https://www.iana.org/go/rfc9457)|


> **Note** A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience. 


**Examples of a `server-error` problem details:**
```json
{
    "type": "https://eoap.github.io/problems-registry/server-error",
    "title": "Server Error",
    "detail": "The server encountered an unexpected error",
    "status": 500,
    "code": "500-01"    
}
```
