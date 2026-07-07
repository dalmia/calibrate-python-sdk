# Reference
## Agents
<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">resolve</a>(...) -> ResolveAgentNamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the IDs for your agents by their names
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agents.resolve(
    names=[
        "my-agent",
        "support-bot"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**names:** `typing.List[str]` — Agent names to resolve to IDs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">list</a>() -> typing.List[RoutersAgentsAgentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of all your agents
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agents.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">create</a>(...) -> AgentCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an agent to test inside Calibrate or connect your existing agent to Calibrate
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agents.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Agent name, unique within the workspace
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AgentCreateType]` 

- `agent`: built inside Calibrate
- `connection`: your existing agent connected to Calibrate
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Agent behavioral config. The keys depend on `type`.

**`type=agent`** (built inside Calibrate):
- `system_prompt` (string): the agent's instructions
- `llm.model` (string): `provider/model`, e.g. `openai/gpt-4.1` or `google/gemini-2.5-flash`
- `stt.provider` (string): `deepgram`, `openai`, `cartesia`, `elevenlabs`, `google`, `sarvam`, or `smallest`
- `tts.provider` (string): `cartesia`, `openai`, `google`, `elevenlabs`, `sarvam`, or `smallest`
- `settings.agent_speaks_first` (bool), `settings.max_assistant_turns` (int)
- `system_tools.end_call` (bool, optional): let the agent end the call
- `data_extraction_fields` (array, optional): `[{name, type, description, required}]`

```json
{
  "system_prompt": "You are a helpful support agent.",
  "llm": {"model": "openai/gpt-4.1"},
  "stt": {"provider": "deepgram"},
  "tts": {"provider": "elevenlabs"},
  "settings": {"agent_speaks_first": true, "max_assistant_turns": 50}
}
```

**`type=connection`** (your own HTTP endpoint):
- `agent_url` (string, required): public HTTPS endpoint the agent is called at
- `agent_headers` (object, optional): headers sent on each request, e.g. auth
- `benchmark_provider` (string, optional): `openrouter` (default), `openai`, `google`, `anthropic`, `meta-llama`, `mistralai`, `deepseek`, `x-ai`, `cohere`, `qwen`, or `ai21`

```json
{
  "agent_url": "https://api.example.com/agent",
  "agent_headers": {"Authorization": "Bearer <token>"},
  "benchmark_provider": "openrouter"
}
```

For `type=agent`, omitted keys inherit managed defaults (omit `config` entirely to use all defaults). For `type=connection`, `config` is stored as-is and must contain `agent_url`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">get</a>(...) -> RoutersAgentsAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one agent by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agents.get(
    agent_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — The agent to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">update</a>(...) -> RoutersAgentsAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an agent's configuration
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agents.update(
    agent_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — The agent to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New agent name. Omit to leave the name unchanged
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Agent behavioral config. The keys depend on `type`.

**`type=agent`** (built inside Calibrate):
- `system_prompt` (string): the agent's instructions
- `llm.model` (string): `provider/model`, e.g. `openai/gpt-4.1` or `google/gemini-2.5-flash`
- `stt.provider` (string): `deepgram`, `openai`, `cartesia`, `elevenlabs`, `google`, `sarvam`, or `smallest`
- `tts.provider` (string): `cartesia`, `openai`, `google`, `elevenlabs`, `sarvam`, or `smallest`
- `settings.agent_speaks_first` (bool), `settings.max_assistant_turns` (int)
- `system_tools.end_call` (bool, optional): let the agent end the call
- `data_extraction_fields` (array, optional): `[{name, type, description, required}]`

```json
{
  "system_prompt": "You are a helpful support agent.",
  "llm": {"model": "openai/gpt-4.1"},
  "stt": {"provider": "deepgram"},
  "tts": {"provider": "elevenlabs"},
  "settings": {"agent_speaks_first": true, "max_assistant_turns": 50}
}
```

**`type=connection`** (your own HTTP endpoint):
- `agent_url` (string, required): public HTTPS endpoint the agent is called at
- `agent_headers` (object, optional): headers sent on each request, e.g. auth
- `benchmark_provider` (string, optional): `openrouter` (default), `openai`, `google`, `anthropic`, `meta-llama`, `mistralai`, `deepseek`, `x-ai`, `cohere`, `qwen`, or `ai21`

```json
{
  "agent_url": "https://api.example.com/agent",
  "agent_headers": {"Authorization": "Bearer <token>"},
  "benchmark_provider": "openrouter"
}
```

Replaces the stored config. Omit to leave unchanged.

For `type=connection`, changing `agent_url` or `agent_headers` resets the connection and benchmark verification flags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tests
<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">bulk_create</a>(...) -> BulkTestUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create many test cases at once and link them to your agents
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate, BulkTestItem, ChatMessage
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.tests.bulk_create(
    type="response",
    tests=[
        BulkTestItem(
            name="name",
            conversation_history=[
                ChatMessage(
                    role="user",
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `BulkTestUploadType` 

What the test judges:

- `response`: judges the generated reply
- `tool_call`: diffs the generated tool calls
- `conversation`: judges the full conversation

Applied to every test in the batch.
    
</dd>
</dl>

<dl>
<dd>

**tests:** `typing.List[BulkTestItem]` — Test items to create (non-empty, max 500 per request, names unique within the batch)
    
</dd>
</dl>

<dl>
<dd>

**agent_uuids:** `typing.Optional[typing.List[str]]` — Agents (IDs) to link every created test to. Omit to link none
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Language written to each test's `config.settings.language`. Omit to leave unset
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">list</a>() -> typing.List[RoutersTestsTestResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all the test cases for your agents
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.tests.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">create</a>(...) -> TestCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a test that runs your agent against a conversation and evaluates its answer quality or the tools it calls
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.tests.create(
    name="name",
    type="response",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the test, unique within the workspace
    
</dd>
</dl>

<dl>
<dd>

**type:** `TestCreateType` 

What the test judges:

- `response`: judges the generated reply
- `tool_call`: diffs the generated tool calls
- `conversation`: judges the full conversation
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` 

The calibrate test config. Three top-level keys.

- `history` (array, required): the conversation up to the agent's turn. Each item is `{role, content}` with `role` one of `user`, `assistant`, `tool`. A `tool` message also carries `tool_call_id` and `name`.
- `evaluation` (object, required): `{type, ...}`, where `type` matches the test's `type` (below).
- `settings` (object, optional): e.g. `{"language": "en"}`.

`evaluation` by test type:
- `response`: judge the agent's reply, graded by the linked evaluators. `{"type": "response"}`
- `conversation`: append the reply and judge the whole conversation. `{"type": "conversation"}`
- `tool_call`: diff the agent's tool calls against expected ones. Add `tool_calls`, a list of `{tool, arguments, accept_any_arguments?}`.

For `tool_call`, each expected argument value is one of:
- `{"match_type": "exact", "value": <any>}`: must equal `value`
- `{"match_type": "llm_judge", "criteria": "..."}`: judged against the criteria
- `{"match_type": "any"}`: any value, only checks the argument was passed

`response` / `conversation` example:
```json
{
  "history": [{"role": "user", "content": "What is your return policy?"}],
  "evaluation": {"type": "response"},
  "settings": {"language": "en"}
}
```

`tool_call` example:
```json
{
  "history": [{"role": "user", "content": "Book room 101 for tomorrow"}],
  "evaluation": {
    "type": "tool_call",
    "tool_calls": [
      {
        "tool": "book_room",
        "arguments": {
          "room": {"match_type": "exact", "value": "101"},
          "date": {"match_type": "llm_judge", "criteria": "tomorrow's date"}
        },
        "accept_any_arguments": false
      }
    ]
  }
}
```

Evaluators are linked via the separate `evaluators` field, not inside `config`.

Omit to create the test with no config and fill it in later via update.
    
</dd>
</dl>

<dl>
<dd>

**evaluators:** `typing.Optional[typing.List[RoutersTestsEvaluatorRef]]` — Evaluators to link. Used by `response` and `conversation` tests
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">get</a>(...) -> RoutersTestsTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent test case by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.tests.get(
    test_uuid="b1c2d3e4-f5a6-7890-bcde-f12345678901",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_uuid:** `str` — Test to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">update</a>(...) -> RoutersTestsTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an agent test case
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.tests.update(
    test_uuid="b1c2d3e4-f5a6-7890-bcde-f12345678901",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_uuid:** `str` — Test to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New test name. Omit to leave unchanged
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[TestUpdateType]` 

What the test judges:

- `response`: judges the generated reply
- `tool_call`: diffs the generated tool calls
- `conversation`: judges the full conversation

Immutable. Omit, or send the existing value. A different value is rejected (400).
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` 

The calibrate test config. Three top-level keys.

- `history` (array, required): the conversation up to the agent's turn. Each item is `{role, content}` with `role` one of `user`, `assistant`, `tool`. A `tool` message also carries `tool_call_id` and `name`.
- `evaluation` (object, required): `{type, ...}`, where `type` matches the test's `type` (below).
- `settings` (object, optional): e.g. `{"language": "en"}`.

`evaluation` by test type:
- `response`: judge the agent's reply, graded by the linked evaluators. `{"type": "response"}`
- `conversation`: append the reply and judge the whole conversation. `{"type": "conversation"}`
- `tool_call`: diff the agent's tool calls against expected ones. Add `tool_calls`, a list of `{tool, arguments, accept_any_arguments?}`.

For `tool_call`, each expected argument value is one of:
- `{"match_type": "exact", "value": <any>}`: must equal `value`
- `{"match_type": "llm_judge", "criteria": "..."}`: judged against the criteria
- `{"match_type": "any"}`: any value, only checks the argument was passed

`response` / `conversation` example:
```json
{
  "history": [{"role": "user", "content": "What is your return policy?"}],
  "evaluation": {"type": "response"},
  "settings": {"language": "en"}
}
```

`tool_call` example:
```json
{
  "history": [{"role": "user", "content": "Book room 101 for tomorrow"}],
  "evaluation": {
    "type": "tool_call",
    "tool_calls": [
      {
        "tool": "book_room",
        "arguments": {
          "room": {"match_type": "exact", "value": "101"},
          "date": {"match_type": "llm_judge", "criteria": "tomorrow's date"}
        },
        "accept_any_arguments": false
      }
    ]
  }
}
```

Evaluators are linked via the separate `evaluators` field, not inside `config`.

Replaces the stored config. Omit to leave unchanged.
    
</dd>
</dl>

<dl>
<dd>

**evaluators:** `typing.Optional[typing.List[RoutersTestsEvaluatorRef]]` — New evaluator links for the test. Omit to leave unchanged. An empty list clears them, except on `conversation` tests, which must keep at least one
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AgentTests
<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">run</a>(...) -> AgentTestRunCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run an agent's linked tests as a background job, returning a task ID to poll
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agent_tests.run(
    agent_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — The agent to test.
    
</dd>
</dl>

<dl>
<dd>

**test_uuids:** `typing.Optional[typing.List[str]]` — Tests to run. Omit to run all tests linked to the agent
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">run_batch</a>(...) -> BatchTestRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run agent tests for every agent, or for a selected set
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate, BatchRunRequest
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agent_tests.run_batch(
    request=BatchRunRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[BatchRunRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">get_run</a>(...) -> TestRunStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Poll a test run for its status and evaluation results
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.agent_tests.get_run(
    task_id="a3b2c1d0-e5f4-3210-abcd-ef1234567890",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — Test run to poll for status and results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

