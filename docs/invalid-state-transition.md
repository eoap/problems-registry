# Invalid State Transition

This problem occurs when the requested transition is not valid for the current item status.

Your client issued a request that failed current item status transition. Please review your request to determine if you can remain within appropriate status transition.

| Type URI | Title | Recommended HTTP Status Code | Reference |
|----------|-------|------------------------------|-----------|
|https://eoap.github.io/problems-registry/invalid-state-transition|Invalid State Transition|422||

> **Note** A problem is generally **not** meant to be used for end-user input validation, but for client developer convenience. 


**Example of an `invalid-state-transition` problem details:**
```json
{
  "type": "https://eoap.github.io/problems-registry/invalid-state-transition",
  "status": 422,
  "title": "Invalid State Transition",
  "detail": "The requested transition is not valid for the current item status.",
  "code": "422-01",
  "instance": "https://stac.dataspace.copernicus.eu/v1/collections/ccm-optical/items/PH1B_PHR_MS___3_20241115T141727_20241115T141750_TOU_000324_e7a7_COG",
  "errors": [
    {
      "detail": "Item `PH1B_PHR_MS___3_20241115T141727_20241115T141750_TOU_000324_e7a7_COG` cannot transition from `orderable` to `failed`.\n",
      "pointer": "/properties/order:status"
    }
  ]
}
```
