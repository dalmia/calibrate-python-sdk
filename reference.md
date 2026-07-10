# Reference
## Agents
<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">verify_connection</a>(...) -> VerifyConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify an agent's connection and persist the result when successful
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

client.agents.verify_connection(
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

**agent_uuid:** `str` — The agent whose connection to verify
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model to verify. Omit for a basic connection check. Provide it for a model-specific check before benchmarking that model
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[typing.Dict[str, str]]]` — Sample chat messages to send during verification. Omit to use the default probe
    
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

<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">list</a>(...) -> PaginatedResponseAgentSummary</code></summary>
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

**q:** `typing.Optional[str]` — Case-insensitive substring search on `name`. Blank is a no-op
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return. Omit for no limit (all items)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

**`type=agent`**, built inside Calibrate:
- `system_prompt`: the agent's instructions
- `llm.model`: `provider/model`, e.g. `openai/gpt-4.1` or `google/gemini-2.5-flash`
- `stt.provider`: `deepgram`, `openai`, `cartesia`, `elevenlabs`, `google`, `sarvam`, or `smallest`
- `tts.provider`: `cartesia`, `openai`, `google`, `elevenlabs`, `sarvam`, or `smallest`
- `settings.agent_speaks_first`, `settings.max_assistant_turns`
- `system_tools.end_call`: let the agent end the call
- `data_extraction_fields`: `[{name, type, description, required}]`

```json
{
  "system_prompt": "You are a helpful support agent.",
  "llm": {"model": "openai/gpt-4.1"},
  "stt": {"provider": "deepgram"},
  "tts": {"provider": "elevenlabs"},
  "settings": {"agent_speaks_first": true, "max_assistant_turns": 50}
}
```

**`type=connection`**, your own HTTP endpoint:
- `agent_url`: public HTTP(S) endpoint your agent is called at
- `agent_headers`: headers sent on each request, e.g. auth
- `benchmark_provider`: `openrouter` by default. Other values: `openai`, `google`, `anthropic`, `meta-llama`, `mistralai`, `deepseek`, `x-ai`, `cohere`, `qwen`, or `ai21`

```json
{
  "agent_url": "https://api.example.com/agent",
  "agent_headers": {"Authorization": "Bearer <token>"},
  "benchmark_provider": "openrouter"
}
```

For `type=agent`, omitted keys inherit managed defaults. Omit `config` entirely to use all defaults. For `type=connection`, `config` is stored as-is and must contain `agent_url`
    
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

**agent_uuid:** `str` — The agent to retrieve
    
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

**agent_uuid:** `str` — The agent to update
    
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

**`type=agent`**, built inside Calibrate:
- `system_prompt`: the agent's instructions
- `llm.model`: `provider/model`, e.g. `openai/gpt-4.1` or `google/gemini-2.5-flash`
- `stt.provider`: `deepgram`, `openai`, `cartesia`, `elevenlabs`, `google`, `sarvam`, or `smallest`
- `tts.provider`: `cartesia`, `openai`, `google`, `elevenlabs`, `sarvam`, or `smallest`
- `settings.agent_speaks_first`, `settings.max_assistant_turns`
- `system_tools.end_call`: let the agent end the call
- `data_extraction_fields`: `[{name, type, description, required}]`

```json
{
  "system_prompt": "You are a helpful support agent.",
  "llm": {"model": "openai/gpt-4.1"},
  "stt": {"provider": "deepgram"},
  "tts": {"provider": "elevenlabs"},
  "settings": {"agent_speaks_first": true, "max_assistant_turns": 50}
}
```

**`type=connection`**, your own HTTP endpoint:
- `agent_url`: public HTTP(S) endpoint your agent is called at
- `agent_headers`: headers sent on each request, e.g. auth
- `benchmark_provider`: `openrouter` by default. Other values: `openai`, `google`, `anthropic`, `meta-llama`, `mistralai`, `deepseek`, `x-ai`, `cohere`, `qwen`, or `ai21`

```json
{
  "agent_url": "https://api.example.com/agent",
  "agent_headers": {"Authorization": "Bearer <token>"},
  "benchmark_provider": "openrouter"
}
```

Replaces the stored config. Omit to leave unchanged

For `type=connection`, changing `agent_url` or `agent_headers` resets the connection and benchmark verification flags
    
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


Applied to every test in the batch
    
</dd>
</dl>

<dl>
<dd>

**tests:** `typing.List[BulkTestItem]` — Test items to create, at most 500 per request, with names unique within the batch
    
</dd>
</dl>

<dl>
<dd>

**agent_uuids:** `typing.Optional[typing.List[str]]` — IDs of agents to link every created test to. Omit to link none
    
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

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">list</a>(...) -> PaginatedResponseTestListResponse</code></summary>
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

**q:** `typing.Optional[str]` — Case-insensitive substring search on `name`. Blank is a no-op
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return. Omit for no limit (all items)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

- `history`: the required conversation up to the agent's turn. Each item is `{role, content}` with `role` one of `user`, `assistant`, `tool`. A `tool` message also carries `tool_call_id` and `name`.
- `evaluation`: the required `{type, ...}`, where `type` matches the test's `type` below.
- `settings`: an optional object, e.g. `{"language": "en"}`.

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

Omit to create the test with no config and fill it in later via update
    
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

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">get</a>(...) -> TestResponse</code></summary>
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

<details><summary><code>client.tests.<a href="src/calibrate/tests/client.py">update</a>(...) -> TestResponse</code></summary>
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


Immutable. Omit it, or send the current value
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` 

The calibrate test config. Three top-level keys.

- `history`: the required conversation up to the agent's turn. Each item is `{role, content}` with `role` one of `user`, `assistant`, `tool`. A `tool` message also carries `tool_call_id` and `name`.
- `evaluation`: the required `{type, ...}`, where `type` matches the test's `type` below.
- `settings`: an optional object, e.g. `{"language": "en"}`.

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

Replaces the stored config. Omit to leave unchanged
    
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
<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">link</a>(...) -> AgentTestsCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link one or more tests to an agent. Tests that are already linked are skipped.
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

client.agent_tests.link(
    agent_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    test_uuids=[
        "b1c2d3e4-f5a6-7890-bcde-f12345678901"
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

**agent_uuid:** `str` — Agent to link tests to
    
</dd>
</dl>

<dl>
<dd>

**test_uuids:** `typing.List[str]` — Tests to link. Any that are already linked are skipped
    
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

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">list_for_agent</a>(...) -> PaginatedResponseTestListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the tests linked to an agent.
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

client.agent_tests.list_for_agent(
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

**agent_uuid:** `str` — Agent whose linked tests to list
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Case-insensitive substring search on `name`. Blank is a no-op
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return. Omit for no limit (all items)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">list_runs_for_agent</a>(...) -> PaginatedResponseAgentTestRunListItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List an agent's test runs with their results
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

client.agent_tests.list_runs_for_agent(
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

**agent_uuid:** `str` — Agent whose test runs to list
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListRunsForAgentAgentTestsRequestType]` 

Filter by run type. Omit to return both:
- `llm-unit-test`: single runs of an agent's tests
- `llm-benchmark`: multi-model comparisons
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskStatus]` — Filter by run status. Omit for all statuses
    
</dd>
</dl>

<dl>
<dd>

**has_failures:** `typing.Optional[bool]` — Filter by whether the run has any failing test case or model. `true` returns only runs with failures (or errors), `false` only clean runs. Omit for both
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return. Omit for no limit (all items)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">run</a>(...) -> AgentTestRunCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run an agent's linked tests as a background job, returning a task ID to poll.
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

**agent_uuid:** `str` — Agent to test
    
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

Run agent tests for every agent, or for a selected set.
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

Poll a test run for its status and evaluation results.
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

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">benchmark</a>(...) -> AgentTestRunCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run a multi-model benchmark on an agent's linked tests as a background job.
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

client.agent_tests.benchmark(
    agent_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    models=[
        "openai/gpt-4.1",
        "anthropic/claude-sonnet-4"
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

**agent_uuid:** `str` — Agent to benchmark
    
</dd>
</dl>

<dl>
<dd>

**models:** `typing.List[str]` — Model names to benchmark
    
</dd>
</dl>

<dl>
<dd>

**test_uuids:** `typing.Optional[typing.List[str]]` — A subset of the agent's linked tests to benchmark. Each ID must be linked to the agent. Omit to run all linked tests
    
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

<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">get_benchmark</a>(...) -> BenchmarkStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the results of a benchmark run
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

client.agent_tests.get_benchmark(
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

**task_id:** `str` — Benchmark run to poll for status and results
    
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

## Evaluators
<details><summary><code>client.evaluators.<a href="src/calibrate/evaluators/client.py">list</a>(...) -> PaginatedResponseEvaluatorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List your evaluators
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

client.evaluators.list()

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

**evaluator_type:** `typing.Optional[ListEvaluatorsRequestEvaluatorType]` — Filter by what the evaluator judges. Omit for all types
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `typing.Optional[ListEvaluatorsRequestDataType]` — Filter by modality. Omit for all
    
</dd>
</dl>

<dl>
<dd>

**include_defaults:** `typing.Optional[bool]` — When `true`, include the built-in default evaluators alongside the ones you created
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Case-insensitive substring search on `name`. Blank is a no-op
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return. Omit for no limit (all items)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

<details><summary><code>client.evaluators.<a href="src/calibrate/evaluators/client.py">create</a>(...) -> EvaluatorCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an evaluator along with its first version, which is set live
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
from calibrate import Calibrate, EvaluatorVersionCreate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.evaluators.create(
    name="name",
    version=EvaluatorVersionCreate(
        judge_model="judge_model",
        system_prompt="system_prompt",
    ),
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

**name:** `str` — Evaluator name, unique within your workspace
    
</dd>
</dl>

<dl>
<dd>

**version:** `EvaluatorVersionCreate` — The evaluator's first version. Set as live when you create the evaluator
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description. Omit to leave blank
    
</dd>
</dl>

<dl>
<dd>

**evaluator_type:** `typing.Optional[EvaluatorCreateEvaluatorType]` 

What the evaluator judges:

- `tts`: TTS audio
- `stt`: one transcript
- `llm`: a reply with its conversation history
- `llm-general`: a standalone input and output pair
- `conversation`: a full conversation
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `typing.Optional[EvaluatorCreateDataType]` 

The modality the judge reads:

- `text`
- `audio`
    
</dd>
</dl>

<dl>
<dd>

**output_type:** `typing.Optional[EvaluatorCreateOutputType]` 

How the evaluator scores:

- `binary`: pass or fail
- `rating`: a numeric score, using the scale in `output_config`
    
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

<details><summary><code>client.evaluators.<a href="src/calibrate/evaluators/client.py">get</a>(...) -> EvaluatorDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one evaluator with its full version history
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

client.evaluators.get(
    evaluator_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**evaluator_uuid:** `str` — Evaluator to retrieve
    
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

<details><summary><code>client.evaluators.<a href="src/calibrate/evaluators/client.py">create_version</a>(...) -> VersionCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new version to an evaluator you created
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

client.evaluators.create_version(
    evaluator_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    judge_model="judge_model",
    system_prompt="system_prompt",
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

**evaluator_uuid:** `str` — Evaluator to add a version to
    
</dd>
</dl>

<dl>
<dd>

**judge_model:** `str` — The model that runs the judge, named the way its provider does, for example `openai/gpt-4.1` or `anthropic/claude-sonnet-4`
    
</dd>
</dl>

<dl>
<dd>

**system_prompt:** `str` — Judge system prompt. May contain `{{variable}}` placeholders
    
</dd>
</dl>

<dl>
<dd>

**output_config:** `typing.Optional[OutputConfig]` — The scale points and their labels. Required for a `rating` evaluator. A `binary` evaluator uses the default Correct/Wrong labels unless you set your own
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.List[VariableSpec]]` — Declared prompt variables. Omit if the prompt has none. After the first version the variable names are fixed. You can change a variable's description or default, but not add, remove, or rename one
    
</dd>
</dl>

<dl>
<dd>

**make_live:** `typing.Optional[bool]` — When `true`, immediately point the evaluator's live version at this new version
    
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

## AnnotationTasks
<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">list</a>(...) -> PaginatedResponseAnnotationTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List annotation tasks with linked evaluators
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

client.annotation_tasks.list()

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

**q:** `typing.Optional[str]` — Case-insensitive substring search on `name`. Blank is a no-op
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return. Omit for no limit (all items)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">create</a>(...) -> AnnotationTaskCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an annotation task for annotators to label items against evaluators
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

client.annotation_tasks.create(
    name="name",
    type="stt",
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

**name:** `str` — Task name, unique within your workspace
    
</dd>
</dl>

<dl>
<dd>

**type:** `AnnotationTaskCreateType` 

Task type. Determines the shape of each item's payload.
- `stt`: judge a transcript on its own
- `llm`: judge one response with its conversation history
- `llm-general`: judge a standalone `input -> output` pair
- `conversation`: judge a full conversation
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description for the task. Omit for none
    
</dd>
</dl>

<dl>
<dd>

**evaluator_ids:** `typing.Optional[typing.List[str]]` — IDs of evaluators to link when the task is created, in order. Each must be one you created or a built-in default. Omit to create with no linked evaluators
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">get</a>(...) -> AnnotationTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one annotation task with linked evaluators, items, and labelling jobs
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

client.annotation_tasks.get(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**task_uuid:** `str` — Task to retrieve
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">link_evaluator</a>(...) -> EvaluatorLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link an evaluator to a task, appending it to the display order
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

client.annotation_tasks.link_evaluator(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    evaluator_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**evaluator_id:** `str` — The evaluator to link. Must be one you created or a built-in default
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">add_items</a>(...) -> BulkCreateItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk-create annotation items in a task, optionally seeding human annotations
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

client.annotation_tasks.add_items(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    items=[],
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[AnnotationItemPayload]` — Items to insert. Insertion order is preserved
    
</dd>
</dl>

<dl>
<dd>

**annotator_id:** `typing.Optional[str]` — Annotator these initial annotations belong to. Required when any item carries annotations
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">update_items</a>(...) -> BulkUpdateItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk-update item payloads in a task
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

client.annotation_tasks.update_items(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    updates=[],
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.List[ItemUpdatePayload]` — The new payload for each item you're updating. Entries not in this task, or referencing deleted items, are skipped
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">create_evaluator_run</a>(...) -> EvaluatorRunLaunchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run evaluators on task items as a background job
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
from calibrate import Calibrate, EvaluatorRunRequestEntry
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    api_key="<value>",
    environment=CalibrateEnvironment.DEFAULT,
)

client.annotation_tasks.create_evaluator_run(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    evaluators=[
        EvaluatorRunRequestEntry(
            evaluator_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**evaluators:** `typing.List[EvaluatorRunRequestEntry]` — The evaluators to run. Each must be linked to the task
    
</dd>
</dl>

<dl>
<dd>

**item_ids:** `typing.Optional[typing.List[str]]` — Item IDs to run on. **Required when `select_all=false`**. Ignored when `select_all=true`
    
</dd>
</dl>

<dl>
<dd>

**select_all:** `typing.Optional[bool]` — When `true`, run on every item in the task. Set `q` to run only items whose name matches it
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Case-insensitive substring filter on `payload.name`. Applies only when `select_all=true`
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">get_evaluator_run</a>(...) -> EvaluatorRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one evaluator-run job with results and human-agreement summary
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

client.annotation_tasks.get_evaluator_run(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    job_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**job_uuid:** `str` — The evaluator run to act on
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">get_agreement</a>(...) -> TaskAgreementResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get human-vs-human and human-vs-evaluator agreement metrics for a task
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

client.annotation_tasks.get_agreement(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**bucket:** `typing.Optional[GetAgreementAnnotationTasksRequestBucket]` — How to bucket points in the trend series
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Trailing window in days for the trend series
    
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

<details><summary><code>client.annotation_tasks.<a href="src/calibrate/annotation_tasks/client.py">get_summary</a>(...) -> TaskSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a paginated summary table of items, evaluator runs, and human annotations for a task
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

client.annotation_tasks.get_summary(
    task_uuid="f47ac10b-58cc-4372-a567-0e02b2c3d479",
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

**task_uuid:** `str` — Annotation task to act on
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `typing.Optional[str]` — Filter rows to a single item. The full task-wide annotator union is still returned in `annotators`
    
</dd>
</dl>

<dl>
<dd>

**live_only:** `typing.Optional[bool]` — When true, emit only one row for each (item, evaluator) pair using the evaluator's live version. Versions other than the live one that have runs are excluded
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Case-insensitive substring search on `payload.name`. Blank is a no-op
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Sort key for the results
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetSummaryAnnotationTasksRequestOrder]` — Sort direction
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results
    
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

