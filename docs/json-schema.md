# EOAP Problem Details Registry

- [1. Property `EOAP Problem Details Registry > anyOf > AlreadyExists`](#anyOf_i0)
  - [1.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > ProblemDetails`](#anyOf_i0_allOf_i0)
    - [1.1.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > instance`](#anyOf_i0_allOf_i0_instance)
    - [1.1.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > code`](#anyOf_i0_allOf_i0_code)
    - [1.1.3. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors`](#anyOf_i0_allOf_i0_errors)
      - [1.1.3.1. EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > ErrorDetail](#anyOf_i0_allOf_i0_errors_items)
        - [1.1.3.1.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > detail`](#anyOf_i0_allOf_i0_errors_items_detail)
        - [1.1.3.1.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > pointer`](#anyOf_i0_allOf_i0_errors_items_pointer)
        - [1.1.3.1.3. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > parameter`](#anyOf_i0_allOf_i0_errors_items_parameter)
        - [1.1.3.1.4. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > header`](#anyOf_i0_allOf_i0_errors_items_header)
        - [1.1.3.1.5. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > code`](#anyOf_i0_allOf_i0_errors_items_code)
  - [1.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1`](#anyOf_i0_allOf_i1)
    - [1.2.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > type`](#anyOf_i0_allOf_i1_type)
    - [1.2.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > status`](#anyOf_i0_allOf_i1_status)
    - [1.2.3. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > title`](#anyOf_i0_allOf_i1_title)
    - [1.2.4. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > detail`](#anyOf_i0_allOf_i1_detail)
- [2. Property `EOAP Problem Details Registry > anyOf > BadRequest`](#anyOf_i1)
  - [2.1. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > ProblemDetails`](#anyOf_i1_allOf_i0)
  - [2.2. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1`](#anyOf_i1_allOf_i1)
    - [2.2.1. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > type`](#anyOf_i1_allOf_i1_type)
    - [2.2.2. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > status`](#anyOf_i1_allOf_i1_status)
    - [2.2.3. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > title`](#anyOf_i1_allOf_i1_title)
    - [2.2.4. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > detail`](#anyOf_i1_allOf_i1_detail)
- [3. Property `EOAP Problem Details Registry > anyOf > BusinessRuleViolation`](#anyOf_i2)
  - [3.1. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > ProblemDetails`](#anyOf_i2_allOf_i0)
  - [3.2. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1`](#anyOf_i2_allOf_i1)
    - [3.2.1. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > type`](#anyOf_i2_allOf_i1_type)
    - [3.2.2. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > status`](#anyOf_i2_allOf_i1_status)
    - [3.2.3. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > title`](#anyOf_i2_allOf_i1_title)
    - [3.2.4. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > detail`](#anyOf_i2_allOf_i1_detail)
- [4. Property `EOAP Problem Details Registry > anyOf > Forbidden`](#anyOf_i3)
  - [4.1. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > ProblemDetails`](#anyOf_i3_allOf_i0)
  - [4.2. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1`](#anyOf_i3_allOf_i1)
    - [4.2.1. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > type`](#anyOf_i3_allOf_i1_type)
    - [4.2.2. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > status`](#anyOf_i3_allOf_i1_status)
    - [4.2.3. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > title`](#anyOf_i3_allOf_i1_title)
    - [4.2.4. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > detail`](#anyOf_i3_allOf_i1_detail)
- [5. Property `EOAP Problem Details Registry > anyOf > InvalidBodyPropertyFormat`](#anyOf_i4)
  - [5.1. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > ProblemDetails`](#anyOf_i4_allOf_i0)
  - [5.2. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1`](#anyOf_i4_allOf_i1)
    - [5.2.1. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > type`](#anyOf_i4_allOf_i1_type)
    - [5.2.2. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > status`](#anyOf_i4_allOf_i1_status)
    - [5.2.3. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > title`](#anyOf_i4_allOf_i1_title)
    - [5.2.4. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > detail`](#anyOf_i4_allOf_i1_detail)
- [6. Property `EOAP Problem Details Registry > anyOf > InvalidBodyPropertyValue`](#anyOf_i5)
  - [6.1. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > ProblemDetails`](#anyOf_i5_allOf_i0)
  - [6.2. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1`](#anyOf_i5_allOf_i1)
    - [6.2.1. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > type`](#anyOf_i5_allOf_i1_type)
    - [6.2.2. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > status`](#anyOf_i5_allOf_i1_status)
    - [6.2.3. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > title`](#anyOf_i5_allOf_i1_title)
    - [6.2.4. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > detail`](#anyOf_i5_allOf_i1_detail)
- [7. Property `EOAP Problem Details Registry > anyOf > InvalidParameters`](#anyOf_i6)
  - [7.1. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > ProblemDetails`](#anyOf_i6_allOf_i0)
  - [7.2. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1`](#anyOf_i6_allOf_i1)
    - [7.2.1. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > type`](#anyOf_i6_allOf_i1_type)
    - [7.2.2. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > status`](#anyOf_i6_allOf_i1_status)
    - [7.2.3. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > title`](#anyOf_i6_allOf_i1_title)
    - [7.2.4. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > detail`](#anyOf_i6_allOf_i1_detail)
- [8. Property `EOAP Problem Details Registry > anyOf > InvalidRequestHeaderFormat`](#anyOf_i7)
  - [8.1. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > ProblemDetails`](#anyOf_i7_allOf_i0)
  - [8.2. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1`](#anyOf_i7_allOf_i1)
    - [8.2.1. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > type`](#anyOf_i7_allOf_i1_type)
    - [8.2.2. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > status`](#anyOf_i7_allOf_i1_status)
    - [8.2.3. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > title`](#anyOf_i7_allOf_i1_title)
    - [8.2.4. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > detail`](#anyOf_i7_allOf_i1_detail)
- [9. Property `EOAP Problem Details Registry > anyOf > InvalidRequestParameterFormat`](#anyOf_i8)
  - [9.1. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > ProblemDetails`](#anyOf_i8_allOf_i0)
  - [9.2. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1`](#anyOf_i8_allOf_i1)
    - [9.2.1. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > type`](#anyOf_i8_allOf_i1_type)
    - [9.2.2. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > status`](#anyOf_i8_allOf_i1_status)
    - [9.2.3. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > title`](#anyOf_i8_allOf_i1_title)
    - [9.2.4. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > detail`](#anyOf_i8_allOf_i1_detail)
- [10. Property `EOAP Problem Details Registry > anyOf > InvalidRequestParameterValue`](#anyOf_i9)
  - [10.1. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > ProblemDetails`](#anyOf_i9_allOf_i0)
  - [10.2. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1`](#anyOf_i9_allOf_i1)
    - [10.2.1. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > type`](#anyOf_i9_allOf_i1_type)
    - [10.2.2. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > status`](#anyOf_i9_allOf_i1_status)
    - [10.2.3. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > title`](#anyOf_i9_allOf_i1_title)
    - [10.2.4. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > detail`](#anyOf_i9_allOf_i1_detail)
- [11. Property `EOAP Problem Details Registry > anyOf > LicenseCancelled`](#anyOf_i10)
  - [11.1. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > ProblemDetails`](#anyOf_i10_allOf_i0)
  - [11.2. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1`](#anyOf_i10_allOf_i1)
    - [11.2.1. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > type`](#anyOf_i10_allOf_i1_type)
    - [11.2.2. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > status`](#anyOf_i10_allOf_i1_status)
    - [11.2.3. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > title`](#anyOf_i10_allOf_i1_title)
    - [11.2.4. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > detail`](#anyOf_i10_allOf_i1_detail)
- [12. Property `EOAP Problem Details Registry > anyOf > LicenseExpired`](#anyOf_i11)
  - [12.1. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > ProblemDetails`](#anyOf_i11_allOf_i0)
  - [12.2. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1`](#anyOf_i11_allOf_i1)
    - [12.2.1. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > type`](#anyOf_i11_allOf_i1_type)
    - [12.2.2. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > status`](#anyOf_i11_allOf_i1_status)
    - [12.2.3. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > title`](#anyOf_i11_allOf_i1_title)
    - [12.2.4. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > detail`](#anyOf_i11_allOf_i1_detail)
- [13. Property `EOAP Problem Details Registry > anyOf > MissingBodyProperty`](#anyOf_i12)
  - [13.1. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > ProblemDetails`](#anyOf_i12_allOf_i0)
  - [13.2. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1`](#anyOf_i12_allOf_i1)
    - [13.2.1. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > type`](#anyOf_i12_allOf_i1_type)
    - [13.2.2. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > status`](#anyOf_i12_allOf_i1_status)
    - [13.2.3. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > title`](#anyOf_i12_allOf_i1_title)
    - [13.2.4. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > detail`](#anyOf_i12_allOf_i1_detail)
- [14. Property `EOAP Problem Details Registry > anyOf > MissingRequestHeader`](#anyOf_i13)
  - [14.1. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > ProblemDetails`](#anyOf_i13_allOf_i0)
  - [14.2. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1`](#anyOf_i13_allOf_i1)
    - [14.2.1. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > type`](#anyOf_i13_allOf_i1_type)
    - [14.2.2. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > status`](#anyOf_i13_allOf_i1_status)
    - [14.2.3. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > title`](#anyOf_i13_allOf_i1_title)
    - [14.2.4. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > detail`](#anyOf_i13_allOf_i1_detail)
- [15. Property `EOAP Problem Details Registry > anyOf > MissingRequestParameter`](#anyOf_i14)
  - [15.1. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > ProblemDetails`](#anyOf_i14_allOf_i0)
  - [15.2. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1`](#anyOf_i14_allOf_i1)
    - [15.2.1. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > type`](#anyOf_i14_allOf_i1_type)
    - [15.2.2. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > status`](#anyOf_i14_allOf_i1_status)
    - [15.2.3. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > title`](#anyOf_i14_allOf_i1_title)
    - [15.2.4. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > detail`](#anyOf_i14_allOf_i1_detail)
- [16. Property `EOAP Problem Details Registry > anyOf > NotFound`](#anyOf_i15)
  - [16.1. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > ProblemDetails`](#anyOf_i15_allOf_i0)
  - [16.2. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1`](#anyOf_i15_allOf_i1)
    - [16.2.1. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > type`](#anyOf_i15_allOf_i1_type)
    - [16.2.2. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > status`](#anyOf_i15_allOf_i1_status)
    - [16.2.3. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > title`](#anyOf_i15_allOf_i1_title)
    - [16.2.4. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > detail`](#anyOf_i15_allOf_i1_detail)
- [17. Property `EOAP Problem Details Registry > anyOf > ServerError`](#anyOf_i16)
  - [17.1. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > ProblemDetails`](#anyOf_i16_allOf_i0)
  - [17.2. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1`](#anyOf_i16_allOf_i1)
    - [17.2.1. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > type`](#anyOf_i16_allOf_i1_type)
    - [17.2.2. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > status`](#anyOf_i16_allOf_i1_status)
    - [17.2.3. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > title`](#anyOf_i16_allOf_i1_title)
    - [17.2.4. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > detail`](#anyOf_i16_allOf_i1_detail)
- [18. Property `EOAP Problem Details Registry > anyOf > ServiceUnavailable`](#anyOf_i17)
  - [18.1. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > ProblemDetails`](#anyOf_i17_allOf_i0)
  - [18.2. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1`](#anyOf_i17_allOf_i1)
    - [18.2.1. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > type`](#anyOf_i17_allOf_i1_type)
    - [18.2.2. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > status`](#anyOf_i17_allOf_i1_status)
    - [18.2.3. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > title`](#anyOf_i17_allOf_i1_title)
    - [18.2.4. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > detail`](#anyOf_i17_allOf_i1_detail)
- [19. Property `EOAP Problem Details Registry > anyOf > Unauthorized`](#anyOf_i18)
  - [19.1. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > ProblemDetails`](#anyOf_i18_allOf_i0)
  - [19.2. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1`](#anyOf_i18_allOf_i1)
    - [19.2.1. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > type`](#anyOf_i18_allOf_i1_type)
    - [19.2.2. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > status`](#anyOf_i18_allOf_i1_status)
    - [19.2.3. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > title`](#anyOf_i18_allOf_i1_title)
    - [19.2.4. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > detail`](#anyOf_i18_allOf_i1_detail)
- [20. Property `EOAP Problem Details Registry > anyOf > ValidationError`](#anyOf_i19)
  - [20.1. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > ProblemDetails`](#anyOf_i19_allOf_i0)
  - [20.2. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1`](#anyOf_i19_allOf_i1)
    - [20.2.1. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > type`](#anyOf_i19_allOf_i1_type)
    - [20.2.2. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > status`](#anyOf_i19_allOf_i1_status)
    - [20.2.3. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > title`](#anyOf_i19_allOf_i1_title)
    - [20.2.4. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > detail`](#anyOf_i19_allOf_i1_detail)

**Title:** EOAP Problem Details Registry

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                             |
| ------------------------------------------ |
| [AlreadyExists](#anyOf_i0)                 |
| [BadRequest](#anyOf_i1)                    |
| [BusinessRuleViolation](#anyOf_i2)         |
| [Forbidden](#anyOf_i3)                     |
| [InvalidBodyPropertyFormat](#anyOf_i4)     |
| [InvalidBodyPropertyValue](#anyOf_i5)      |
| [InvalidParameters](#anyOf_i6)             |
| [InvalidRequestHeaderFormat](#anyOf_i7)    |
| [InvalidRequestParameterFormat](#anyOf_i8) |
| [InvalidRequestParameterValue](#anyOf_i9)  |
| [LicenseCancelled](#anyOf_i10)             |
| [LicenseExpired](#anyOf_i11)               |
| [MissingBodyProperty](#anyOf_i12)          |
| [MissingRequestHeader](#anyOf_i13)         |
| [MissingRequestParameter](#anyOf_i14)      |
| [NotFound](#anyOf_i15)                     |
| [ServerError](#anyOf_i16)                  |
| [ServiceUnavailable](#anyOf_i17)           |
| [Unauthorized](#anyOf_i18)                 |
| [ValidationError](#anyOf_i19)              |

## <a name="anyOf_i0"></a>1. Property `EOAP Problem Details Registry > anyOf > AlreadyExists`

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `combining`           |
| **Required**              | No                    |
| **Additional properties** | Any type allowed      |
| **Defined in**            | #/$defs/AlreadyExists |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i0_allOf_i0) |
| [item 1](#anyOf_i0_allOf_i1)         |

### <a name="anyOf_i0_allOf_i0"></a>1.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > ProblemDetails`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/ProblemDetails |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

| Property                                   | Pattern | Type   | Deprecated | Definition | Title/Description                                                                                                                    |
| ------------------------------------------ | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| - [instance](#anyOf_i0_allOf_i0_instance ) | No      | string | No         | -          | A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. |
| - [code](#anyOf_i0_allOf_i0_code )         | No      | string | No         | -          | An API specific error code aiding the provider team understand the error based on their own potential taxonomy or registry.          |
| - [errors](#anyOf_i0_allOf_i0_errors )     | No      | array  | No         | -          | An array of error details to accompany a problem details response.                                                                   |

#### <a name="anyOf_i0_allOf_i0_instance"></a>1.1.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > instance`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced.

| Restrictions   |      |
| -------------- | ---- |
| **Max length** | 1024 |

#### <a name="anyOf_i0_allOf_i0_code"></a>1.1.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > code`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An API specific error code aiding the provider team understand the error based on their own potential taxonomy or registry.

| Restrictions   |    |
| -------------- | -- |
| **Max length** | 50 |

#### <a name="anyOf_i0_allOf_i0_errors"></a>1.1.3. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** An array of error details to accompany a problem details response.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | 1000               |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                | Description                                                                 |
| ---------------------------------------------- | --------------------------------------------------------------------------- |
| [ErrorDetail](#anyOf_i0_allOf_i0_errors_items) | An object to provide explicit details on a problem towards an API consumer. |

##### <a name="anyOf_i0_allOf_i0_errors_items"></a>1.1.3.1. EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > ErrorDetail

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/ErrorDetail |

**Description:** An object to provide explicit details on a problem towards an API consumer.

| Property                                                  | Pattern | Type   | Deprecated | Definition | Title/Description                                                                                                         |
| --------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| + [detail](#anyOf_i0_allOf_i0_errors_items_detail )       | No      | string | No         | -          | A granular description on the specific error related to a body property, query parameter, path parameters, and/or header. |
| - [pointer](#anyOf_i0_allOf_i0_errors_items_pointer )     | No      | string | No         | -          | A JSON Pointer to a specific request body property that is the source of error.                                           |
| - [parameter](#anyOf_i0_allOf_i0_errors_items_parameter ) | No      | string | No         | -          | The name of the query or path parameter that is the source of error.                                                      |
| - [header](#anyOf_i0_allOf_i0_errors_items_header )       | No      | string | No         | -          | The name of the header that is the source of error.                                                                       |
| - [code](#anyOf_i0_allOf_i0_errors_items_code )           | No      | string | No         | -          | A string containing additional provider specific codes to identify the error context.                                     |

###### <a name="anyOf_i0_allOf_i0_errors_items_detail"></a>1.1.3.1.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > detail`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A granular description on the specific error related to a body property, query parameter, path parameters, and/or header.

| Restrictions   |      |
| -------------- | ---- |
| **Max length** | 4096 |

###### <a name="anyOf_i0_allOf_i0_errors_items_pointer"></a>1.1.3.1.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > pointer`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A JSON Pointer to a specific request body property that is the source of error.

| Restrictions   |      |
| -------------- | ---- |
| **Max length** | 1024 |

###### <a name="anyOf_i0_allOf_i0_errors_items_parameter"></a>1.1.3.1.3. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > parameter`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the query or path parameter that is the source of error.

| Restrictions   |      |
| -------------- | ---- |
| **Max length** | 1024 |

###### <a name="anyOf_i0_allOf_i0_errors_items_header"></a>1.1.3.1.4. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > header`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the header that is the source of error.

| Restrictions   |      |
| -------------- | ---- |
| **Max length** | 1024 |

###### <a name="anyOf_i0_allOf_i0_errors_items_code"></a>1.1.3.1.5. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 0 > errors > errors items > code`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A string containing additional provider specific codes to identify the error context.

| Restrictions   |    |
| -------------- | -- |
| **Max length** | 50 |

### <a name="anyOf_i0_allOf_i1"></a>1.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the resource being created is found to already exist on the server.
Your client application tried to create a resource that already exists. Perhaps review your client logic to determine if a user should be able to send such a request.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i0_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i0_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i0_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i0_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i0_allOf_i1_type"></a>1.2.1. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/already-exists"`

#### <a name="anyOf_i0_allOf_i1_status"></a>1.2.2. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `409`

#### <a name="anyOf_i0_allOf_i1_title"></a>1.2.3. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Already exists"`

#### <a name="anyOf_i0_allOf_i1_detail"></a>1.2.4. Property `EOAP Problem Details Registry > anyOf > item 0 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The resource being created already exists."`

## <a name="anyOf_i1"></a>2. Property `EOAP Problem Details Registry > anyOf > BadRequest`

|                           |                    |
| ------------------------- | ------------------ |
| **Type**                  | `combining`        |
| **Required**              | No                 |
| **Additional properties** | Any type allowed   |
| **Defined in**            | #/$defs/BadRequest |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i1_allOf_i0) |
| [item 1](#anyOf_i1_allOf_i1)         |

### <a name="anyOf_i1_allOf_i0"></a>2.1. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i1_allOf_i1"></a>2.2. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The server cannot or will not process the request due to something that is perceived to be a client error (for example, malformed request syntax, invalid request message framing, or deceptive request routing).
Your client application initiated a request that is malformed. Please review your client request against the defined semantics for the API.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i1_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i1_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i1_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i1_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i1_allOf_i1_type"></a>2.2.1. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/bad-request"`

#### <a name="anyOf_i1_allOf_i1_status"></a>2.2.2. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i1_allOf_i1_title"></a>2.2.3. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Bad Request"`

#### <a name="anyOf_i1_allOf_i1_detail"></a>2.2.4. Property `EOAP Problem Details Registry > anyOf > item 1 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request is invalid or malformed."`

## <a name="anyOf_i2"></a>3. Property `EOAP Problem Details Registry > anyOf > BusinessRuleViolation`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/$defs/BusinessRuleViolation |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i2_allOf_i0) |
| [item 1](#anyOf_i2_allOf_i1)         |

### <a name="anyOf_i2_allOf_i0"></a>3.1. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i2_allOf_i1"></a>3.2. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request is deemed invalid as it fails to meet business rule expectations.
Your client issued a request that failed business rule validation. Please review your request to determine if you can remain within appropriate business rules.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i2_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i2_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i2_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i2_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i2_allOf_i1_type"></a>3.2.1. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/business-rule-violation"`

#### <a name="anyOf_i2_allOf_i1_status"></a>3.2.2. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `422`

#### <a name="anyOf_i2_allOf_i1_title"></a>3.2.3. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Business Rule Violation"`

#### <a name="anyOf_i2_allOf_i1_detail"></a>3.2.4. Property `EOAP Problem Details Registry > anyOf > item 2 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request body is invalid and not meeting business rules."`

## <a name="anyOf_i3"></a>4. Property `EOAP Problem Details Registry > anyOf > Forbidden`

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `combining`       |
| **Required**              | No                |
| **Additional properties** | Any type allowed  |
| **Defined in**            | #/$defs/Forbidden |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i3_allOf_i0) |
| [item 1](#anyOf_i3_allOf_i1)         |

### <a name="anyOf_i3_allOf_i0"></a>4.1. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i3_allOf_i1"></a>4.2. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the requested resource (and/or operation combination) is not authorized for the requesting client (and or authorization context).
Your client application tried to perform an operation on a resource that it's not authorized to perform in the given context.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i3_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i3_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i3_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i3_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i3_allOf_i1_type"></a>4.2.1. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/forbidden"`

#### <a name="anyOf_i3_allOf_i1_status"></a>4.2.2. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `403`

#### <a name="anyOf_i3_allOf_i1_title"></a>4.2.3. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Forbidden"`

#### <a name="anyOf_i3_allOf_i1_detail"></a>4.2.4. Property `EOAP Problem Details Registry > anyOf > item 3 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The resource could not be returned as the requestor is not authorized."`

## <a name="anyOf_i4"></a>5. Property `EOAP Problem Details Registry > anyOf > InvalidBodyPropertyFormat`

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `combining`                       |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/$defs/InvalidBodyPropertyFormat |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i4_allOf_i0) |
| [item 1](#anyOf_i4_allOf_i1)         |

### <a name="anyOf_i4_allOf_i0"></a>5.1. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i4_allOf_i1"></a>5.2. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request body contain a malformed property.
Your client issued a request that contained a malformed body property. Please review your request and compare against the shared API definition.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i4_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i4_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i4_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i4_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i4_allOf_i1_type"></a>5.2.1. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/invalid-body-property-format"`

#### <a name="anyOf_i4_allOf_i1_status"></a>5.2.2. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i4_allOf_i1_title"></a>5.2.3. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Invalid Body Property Format"`

#### <a name="anyOf_i4_allOf_i1_detail"></a>5.2.4. Property `EOAP Problem Details Registry > anyOf > item 4 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request body contains a malformed property."`

## <a name="anyOf_i5"></a>6. Property `EOAP Problem Details Registry > anyOf > InvalidBodyPropertyValue`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `combining`                      |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | #/$defs/InvalidBodyPropertyValue |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i5_allOf_i0) |
| [item 1](#anyOf_i5_allOf_i1)         |

### <a name="anyOf_i5_allOf_i0"></a>6.1. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i5_allOf_i1"></a>6.2. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request body contains a invalid property value.
Your client issued a request that contained an invalid body property value. Please review your request and compare against the shared API definition where applicable.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i5_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i5_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i5_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i5_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i5_allOf_i1_type"></a>6.2.1. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/invalid-body-property-value"`

#### <a name="anyOf_i5_allOf_i1_status"></a>6.2.2. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i5_allOf_i1_title"></a>6.2.3. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Invalid Body Property Value"`

#### <a name="anyOf_i5_allOf_i1_detail"></a>6.2.4. Property `EOAP Problem Details Registry > anyOf > item 5 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request body contains an invalid body property value."`

## <a name="anyOf_i6"></a>7. Property `EOAP Problem Details Registry > anyOf > InvalidParameters`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `combining`               |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/$defs/InvalidParameters |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i6_allOf_i0) |
| [item 1](#anyOf_i6_allOf_i1)         |

### <a name="anyOf_i6_allOf_i0"></a>7.1. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i6_allOf_i1"></a>7.2. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when a client request contains invalid or malformed parameters causing the server to reject the request.
Your client application issued a request to an API that contains invalid or malformed parameters.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i6_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i6_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i6_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i6_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i6_allOf_i1_type"></a>7.2.1. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/invalid-parameters"`

#### <a name="anyOf_i6_allOf_i1_status"></a>7.2.2. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i6_allOf_i1_title"></a>7.2.3. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Invalid parameters"`

#### <a name="anyOf_i6_allOf_i1_detail"></a>7.2.4. Property `EOAP Problem Details Registry > anyOf > item 6 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request contained invalid, or malformed parameters (path or header or query)."`

## <a name="anyOf_i7"></a>8. Property `EOAP Problem Details Registry > anyOf > InvalidRequestHeaderFormat`

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/$defs/InvalidRequestHeaderFormat |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i7_allOf_i0) |
| [item 1](#anyOf_i7_allOf_i1)         |

### <a name="anyOf_i7_allOf_i0"></a>8.1. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i7_allOf_i1"></a>8.2. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request contains a malformed request header.
Your client issued a request that contained a malformed request header. Please review your request parameters and compare against the shared API definition when applicable.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i7_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i7_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i7_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i7_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i7_allOf_i1_type"></a>8.2.1. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/invalid-request-header-format"`

#### <a name="anyOf_i7_allOf_i1_status"></a>8.2.2. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i7_allOf_i1_title"></a>8.2.3. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Invalid Request Header Format"`

#### <a name="anyOf_i7_allOf_i1_detail"></a>8.2.4. Property `EOAP Problem Details Registry > anyOf > item 7 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request contains a malformed request header parameter."`

## <a name="anyOf_i8"></a>9. Property `EOAP Problem Details Registry > anyOf > InvalidRequestParameterFormat`

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `combining`                           |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Defined in**            | #/$defs/InvalidRequestParameterFormat |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i8_allOf_i0) |
| [item 1](#anyOf_i8_allOf_i1)         |

### <a name="anyOf_i8_allOf_i0"></a>9.1. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i8_allOf_i1"></a>9.2. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request contains a malformed query or path parameter.
Your client issued a request that contained a malformed query or path parameter. Please review your request parameters and compare against the shared API definition.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i8_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i8_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i8_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i8_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i8_allOf_i1_type"></a>9.2.1. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/invalid-request-parameter-format"`

#### <a name="anyOf_i8_allOf_i1_status"></a>9.2.2. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i8_allOf_i1_title"></a>9.2.3. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Invalid Request Parameter Format"`

#### <a name="anyOf_i8_allOf_i1_detail"></a>9.2.4. Property `EOAP Problem Details Registry > anyOf > item 8 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request contains a malformed request query parameter."`

## <a name="anyOf_i9"></a>10. Property `EOAP Problem Details Registry > anyOf > InvalidRequestParameterValue`

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `combining`                          |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | #/$defs/InvalidRequestParameterValue |

| All of(Requirement)                  |
| ------------------------------------ |
| [ProblemDetails](#anyOf_i9_allOf_i0) |
| [item 1](#anyOf_i9_allOf_i1)         |

### <a name="anyOf_i9_allOf_i0"></a>10.1. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i9_allOf_i1"></a>10.2. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request contains a invalid query or path parameter value.
Your client issued a request that contained an invalid query or path parameter value. Please review your request and compare against the shared API definition where applicable.

| Property                               | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| -------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i9_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i9_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i9_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i9_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i9_allOf_i1_type"></a>10.2.1. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/invalid-request-parameter-value"`

#### <a name="anyOf_i9_allOf_i1_status"></a>10.2.2. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i9_allOf_i1_title"></a>10.2.3. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Invalid Request Parameter Value"`

#### <a name="anyOf_i9_allOf_i1_detail"></a>10.2.4. Property `EOAP Problem Details Registry > anyOf > item 9 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request body contains an invalid request parameter value."`

## <a name="anyOf_i10"></a>11. Property `EOAP Problem Details Registry > anyOf > LicenseCancelled`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `combining`              |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/LicenseCancelled |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i10_allOf_i0) |
| [item 1](#anyOf_i10_allOf_i1)         |

### <a name="anyOf_i10_allOf_i0"></a>11.1. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i10_allOf_i1"></a>11.2. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the license associated with the client has been cancelled thus rendering the service unavailable.
The license associated with your client/organization has been cancelled. Please contact your account manager or representative.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i10_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i10_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i10_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i10_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i10_allOf_i1_type"></a>11.2.1. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/license-cancelled"`

#### <a name="anyOf_i10_allOf_i1_status"></a>11.2.2. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `503`

#### <a name="anyOf_i10_allOf_i1_title"></a>11.2.3. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"License Cancelled"`

#### <a name="anyOf_i10_allOf_i1_detail"></a>11.2.4. Property `EOAP Problem Details Registry > anyOf > item 10 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The service is unavailable as the license associated with your client or organization has been cancelled. Please contact your account manager or representative."`

## <a name="anyOf_i11"></a>12. Property `EOAP Problem Details Registry > anyOf > LicenseExpired`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `combining`            |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/LicenseExpired |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i11_allOf_i0) |
| [item 1](#anyOf_i11_allOf_i1)         |

### <a name="anyOf_i11_allOf_i0"></a>12.1. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i11_allOf_i1"></a>12.2. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the license associated with the client has expired thus rendering the service unavailable.
The license associated with your client/organization has expired. Please contact your account manager or representative.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i11_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i11_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i11_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i11_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i11_allOf_i1_type"></a>12.2.1. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/license-expired"`

#### <a name="anyOf_i11_allOf_i1_status"></a>12.2.2. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `503`

#### <a name="anyOf_i11_allOf_i1_title"></a>12.2.3. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"License Expired"`

#### <a name="anyOf_i11_allOf_i1_detail"></a>12.2.4. Property `EOAP Problem Details Registry > anyOf > item 11 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The service is unavailable as the license associated with your client or organization has expired. Please contact your account manager or representative."`

## <a name="anyOf_i12"></a>13. Property `EOAP Problem Details Registry > anyOf > MissingBodyProperty`

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `combining`                 |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/MissingBodyProperty |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i12_allOf_i0) |
| [item 1](#anyOf_i12_allOf_i1)         |

### <a name="anyOf_i12_allOf_i0"></a>13.1. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i12_allOf_i1"></a>13.2. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request sent to the API is missing an expected body property.
Your client issued a request that omitted an expected body property.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i12_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i12_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i12_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i12_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i12_allOf_i1_type"></a>13.2.1. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/missing-body-property"`

#### <a name="anyOf_i12_allOf_i1_status"></a>13.2.2. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i12_allOf_i1_title"></a>13.2.3. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Missing body property"`

#### <a name="anyOf_i12_allOf_i1_detail"></a>13.2.4. Property `EOAP Problem Details Registry > anyOf > item 12 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request is missing an expected body property."`

## <a name="anyOf_i13"></a>14. Property `EOAP Problem Details Registry > anyOf > MissingRequestHeader`

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `combining`                  |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/$defs/MissingRequestHeader |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i13_allOf_i0) |
| [item 1](#anyOf_i13_allOf_i1)         |

### <a name="anyOf_i13_allOf_i0"></a>14.1. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i13_allOf_i1"></a>14.2. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request sent to the API is missing an expected request header.
Your client issued a request that omitted an expected request header.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i13_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i13_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i13_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i13_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i13_allOf_i1_type"></a>14.2.1. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/missing-request-header"`

#### <a name="anyOf_i13_allOf_i1_status"></a>14.2.2. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i13_allOf_i1_title"></a>14.2.3. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Missing request header"`

#### <a name="anyOf_i13_allOf_i1_detail"></a>14.2.4. Property `EOAP Problem Details Registry > anyOf > item 13 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request is missing an expected HTTP request header."`

## <a name="anyOf_i14"></a>15. Property `EOAP Problem Details Registry > anyOf > MissingRequestParameter`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `combining`                     |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/$defs/MissingRequestParameter |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i14_allOf_i0) |
| [item 1](#anyOf_i14_allOf_i1)         |

### <a name="anyOf_i14_allOf_i0"></a>15.1. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i14_allOf_i1"></a>15.2. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request sent to the API is missing an query or path parameter.
Your client issued a request that omitted an expected query or path par.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i14_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i14_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i14_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i14_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i14_allOf_i1_type"></a>15.2.1. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/missing-request-parameter"`

#### <a name="anyOf_i14_allOf_i1_status"></a>15.2.2. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `400`

#### <a name="anyOf_i14_allOf_i1_title"></a>15.2.3. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Missing request parameter"`

#### <a name="anyOf_i14_allOf_i1_detail"></a>15.2.4. Property `EOAP Problem Details Registry > anyOf > item 14 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request is missing an expected query or path parameter."`

## <a name="anyOf_i15"></a>16. Property `EOAP Problem Details Registry > anyOf > NotFound`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/NotFound |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i15_allOf_i0) |
| [item 1](#anyOf_i15_allOf_i1)         |

### <a name="anyOf_i15_allOf_i0"></a>16.1. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i15_allOf_i1"></a>16.2. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the requested resource could not be found.
Your client application tried to access a resource that does not exist (or could not be found).

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i15_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i15_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i15_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i15_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i15_allOf_i1_type"></a>16.2.1. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/not-found"`

#### <a name="anyOf_i15_allOf_i1_status"></a>16.2.2. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `404`

#### <a name="anyOf_i15_allOf_i1_title"></a>16.2.3. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Not Found"`

#### <a name="anyOf_i15_allOf_i1_detail"></a>16.2.4. Property `EOAP Problem Details Registry > anyOf > item 15 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The requested resource was not found."`

## <a name="anyOf_i16"></a>17. Property `EOAP Problem Details Registry > anyOf > ServerError`

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `combining`         |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/ServerError |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i16_allOf_i0) |
| [item 1](#anyOf_i16_allOf_i1)         |

### <a name="anyOf_i16_allOf_i0"></a>17.1. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i16_allOf_i1"></a>17.2. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the server encounters an unexpected condition that prevents it from fulfilling the request.
Your client application did everything correct. Unfortunately our API encountered a condition that resulted in this problem.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i16_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i16_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i16_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i16_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i16_allOf_i1_type"></a>17.2.1. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/server-error"`

#### <a name="anyOf_i16_allOf_i1_status"></a>17.2.2. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `500`

#### <a name="anyOf_i16_allOf_i1_title"></a>17.2.3. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Server Error"`

#### <a name="anyOf_i16_allOf_i1_detail"></a>17.2.4. Property `EOAP Problem Details Registry > anyOf > item 16 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The server encountered an unexpected error."`

## <a name="anyOf_i17"></a>18. Property `EOAP Problem Details Registry > anyOf > ServiceUnavailable`

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `combining`                |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/$defs/ServiceUnavailable |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i17_allOf_i0) |
| [item 1](#anyOf_i17_allOf_i1)         |

### <a name="anyOf_i17_allOf_i0"></a>18.1. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i17_allOf_i1"></a>18.2. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the service requested is currently unavailable and the server is not ready to handle the request.
Your client application did everything correct. Unfortunately our API is currently unavailable.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i17_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i17_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i17_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i17_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i17_allOf_i1_type"></a>18.2.1. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/service-unavailable"`

#### <a name="anyOf_i17_allOf_i1_status"></a>18.2.2. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `503`

#### <a name="anyOf_i17_allOf_i1_title"></a>18.2.3. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Service Unavailable"`

#### <a name="anyOf_i17_allOf_i1_detail"></a>18.2.4. Property `EOAP Problem Details Registry > anyOf > item 17 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The service is currently unavailable."`

## <a name="anyOf_i18"></a>19. Property `EOAP Problem Details Registry > anyOf > Unauthorized`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `combining`          |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/Unauthorized |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i18_allOf_i0) |
| [item 1](#anyOf_i18_allOf_i1)         |

### <a name="anyOf_i18_allOf_i0"></a>19.1. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i18_allOf_i1"></a>19.2. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the requested resource could not be returned as the client request lacked valid authentication credentials.
Your client application issued a requested to a protected resource without supplying the required auth details.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i18_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i18_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i18_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i18_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i18_allOf_i1_type"></a>19.2.1. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/unauthorized"`

#### <a name="anyOf_i18_allOf_i1_status"></a>19.2.2. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `401`

#### <a name="anyOf_i18_allOf_i1_title"></a>19.2.3. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Unauthorized"`

#### <a name="anyOf_i18_allOf_i1_detail"></a>19.2.4. Property `EOAP Problem Details Registry > anyOf > item 18 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"Access token not set or invalid, and the requested resource could not be returned."`

## <a name="anyOf_i19"></a>20. Property `EOAP Problem Details Registry > anyOf > ValidationError`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `combining`             |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | #/$defs/ValidationError |

| All of(Requirement)                   |
| ------------------------------------- |
| [ProblemDetails](#anyOf_i19_allOf_i0) |
| [item 1](#anyOf_i19_allOf_i1)         |

### <a name="anyOf_i19_allOf_i0"></a>20.1. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > ProblemDetails`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [anyOf_i0_allOf_i0](#anyOf_i0_allOf_i0) |

**Description:** The `ProblemDetails` object provides detailed information about an errors that occurred during an API call execution. This problem object conforms to the [RFC9457](https://www.rfc-editor.org/info/rfc9457) (formerly [RFC7807](https://tools.ietf.org/html/rfc7807)).
The object is extended with the following properties: - `code` - a string identifier to aid the provider team better understand the error - `errors` - and array of errors providing contextual information on the root cause of the problem
The `ProblemDetails` referenced by this domain utilize the [EOAP Problems Registry](https://eoap.github.io/problems-registry/).

### <a name="anyOf_i19_allOf_i1"></a>20.2. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This problem occurs when the request is deemed unprocessable.
Your client issued a request that failed validation. Certain validation libraries return multi-errors and cannot be easily parsed into discreet types. This problem type, afforded the provider with the ability to surface all validation errors and negate the need for a trial and error workflow on your side. 
Please review your request to determine if you can remain within appropriate business rules. Consider validating your request against available metadata (e.g. schemas) prior to sending to the server.

| Property                                | Pattern | Type  | Deprecated | Definition | Title/Description                                                                                                                                            |
| --------------------------------------- | ------- | ----- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [type](#anyOf_i19_allOf_i1_type )     | No      | const | No         | -          | A URI reference that identifies the problem type.                                                                                                            |
| + [status](#anyOf_i19_allOf_i1_status ) | No      | const | No         | -          | The HTTP status code generated by the origin server for this occurrence of the problem.                                                                      |
| + [title](#anyOf_i19_allOf_i1_title )   | No      | const | No         | -          | A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization. |
| + [detail](#anyOf_i19_allOf_i1_detail ) | No      | const | No         | -          | A human-readable explanation specific to this occurrence of the problem.                                                                                     |

#### <a name="anyOf_i19_allOf_i1_type"></a>20.2.1. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `uri`   |

**Description:** A URI reference that identifies the problem type.

Specific value: `"https://eoap.github.io/problems-registry/validation-error"`

#### <a name="anyOf_i19_allOf_i1_status"></a>20.2.2. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > status`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |
| **Format**   | `int32` |

**Description:** The HTTP status code generated by the origin server for this occurrence of the problem.

Specific value: `422`

#### <a name="anyOf_i19_allOf_i1_title"></a>20.2.3. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > title`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.

Specific value: `"Validation Error"`

#### <a name="anyOf_i19_allOf_i1_detail"></a>20.2.4. Property `EOAP Problem Details Registry > anyOf > item 19 > allOf > item 1 > detail`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** A human-readable explanation specific to this occurrence of the problem.

Specific value: `"The request is not valid."`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2026-07-02 at 12:01:42 +0200
