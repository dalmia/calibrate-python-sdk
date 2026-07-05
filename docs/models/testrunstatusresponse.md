# TestRunStatusResponse


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `task_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `status`                                                   | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `total_tests`                                              | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `passed`                                                   | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `failed`                                                   | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `latency_ms`                                               | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `cost`                                                     | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `total_tokens`                                             | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `evaluators`                                               | List[Dict[str, *Any*]]                                     | :heavy_minus_sign:                                         | N/A                                                        |
| `results`                                                  | List[[models.TestCaseResult](../models/testcaseresult.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `results_s3_prefix`                                        | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `error`                                                    | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `is_public`                                                | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `share_token`                                              | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |