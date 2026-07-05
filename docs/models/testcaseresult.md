# TestCaseResult

Result for a single test case matching calibrate results.json structure


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `test_case_id`                                                 | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |
| `name`                                                         | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |
| `passed`                                                       | *OptionalNullable[bool]*                                       | :heavy_minus_sign:                                             | N/A                                                            |
| `reasoning`                                                    | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |
| `output`                                                       | [OptionalNullable[models.TestOutput]](../models/testoutput.md) | :heavy_minus_sign:                                             | N/A                                                            |
| `test_case`                                                    | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            |
| `judge_results`                                                | List[[models.JudgeResult](../models/judgeresult.md)]           | :heavy_minus_sign:                                             | N/A                                                            |
| `latency_ms`                                                   | *OptionalNullable[float]*                                      | :heavy_minus_sign:                                             | N/A                                                            |
| `cost`                                                         | *OptionalNullable[float]*                                      | :heavy_minus_sign:                                             | N/A                                                            |