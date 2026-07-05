# JudgeResult

One evaluator's verdict for a response-type test case.

Per-row data only — anything constant across rows for the same evaluator
(name, description, output_type, output_config, scale_min/max) lives on
the response-level `evaluators[]` block; look it up by `evaluator_uuid`.

`evaluator_uuid` is None for legacy runs that pre-date the evaluator-
snapshot capture or when the evaluator can't be resolved from the
snapshot.

Exactly one of `match` (binary) / `score` (rating) is set per entry;
both are None for tool-call tests, but tool-call tests don't carry
`judge_results`.

`variable_values` are the {{var}} substitutions used for this evaluator
on this test case, frozen from `test_evaluators.variable_values` at
submission time — stays on the row because it varies per test case.

`value_name` is the human-readable label for `match`/`score` resolved
against the rubric the run actually used (snapshot's
`output_config.scale.name`). Falls back to `Correct`/`Wrong` for binary
or the stringified score for rating when the snapshot lacks named
scale entries (e.g. legacy runs captured before the rubric was
snapshotted).


## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `evaluator_uuid`          | *OptionalNullable[str]*   | :heavy_minus_sign:        | N/A                       |
| `reasoning`               | *OptionalNullable[str]*   | :heavy_minus_sign:        | N/A                       |
| `match`                   | *OptionalNullable[bool]*  | :heavy_minus_sign:        | N/A                       |
| `score`                   | *OptionalNullable[float]* | :heavy_minus_sign:        | N/A                       |
| `value_name`              | *OptionalNullable[str]*   | :heavy_minus_sign:        | N/A                       |
| `variable_values`         | Dict[str, *Any*]          | :heavy_minus_sign:        | N/A                       |