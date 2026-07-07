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

Resolve agent names to their IDs.
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

List all agents in your workspace.
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

Create a new agent in your workspace. For `type=agent`, defaults are deep-merged with any config you supply.
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

**name:** `str` — Human-readable agent name, unique within the workspace
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AgentCreateType]` — `agent` applies managed defaults deep-merged under any supplied `config`; `connection` stores the config you supply as-is (must eventually contain `agent_url`)
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` — Behavioral config (system_prompt, llm, stt, tts, settings, …). Deep-merged over defaults for `type=agent`; stored as-is for `type=connection`. Omit for `type=agent` to use defaults
    
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

Get an agent in your workspace.
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

**agent_uuid:** `str` — The agent to retrieve. Must be in your workspace.
    
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

Update an agent's name and/or config. Changing `agent_url` or `agent_headers` resets connection and benchmark verification flags.
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

**agent_uuid:** `str` — The agent to update. Must be in your workspace.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New agent name. Omit to leave the name unchanged
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` — Replacement config, stored as-is (no deep-merge on update). Changing `agent_url` or `agent_headers` resets all connection/benchmark verification flags. Omit to leave config unchanged
    
</dd>
</dl>

<dl>
<dd>

**connection_verified:** `typing.Optional[bool]` — Directly set the `connection_verified` flag inside config. Omit to leave it untouched
    
</dd>
</dl>

<dl>
<dd>

**benchmark_models_verified:** `typing.Optional[typing.Dict[str, typing.Any]]` — Directly set the per-model benchmark verification map inside config. Omit to leave it untouched
    
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

Create many tests of one type in a single call, optionally linking them to agents.
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
                    role="system",
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

**type:** `BulkTestUploadType` — Test kind applied to every item in the batch
    
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

List all tests for your workspace, each with its linked evaluators.
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

Create a test in your workspace.
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

**name:** `str` — Human-readable test name, unique within the workspace
    
</dd>
</dl>

<dl>
<dd>

**type:** `TestCreateType` — Test kind (immutable after creation): `response` judges the generated reply, `tool_call` diffs generated tool calls, `conversation` judges the full conversation
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` — Calibrate test config (`history`, `evaluation`, optional `settings`). Omit to create an empty shell to fill in later
    
</dd>
</dl>

<dl>
<dd>

**evaluators:** `typing.Optional[typing.List[RoutersTestsEvaluatorRef]]` — Evaluators to link. **Required (>=1) for `type=conversation`** (no fallback judge). Omit for `response`/`tool_call` to link none
    
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

Get a test by ID, including its linked evaluators.
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

Update a test's name, config, and/or evaluator links.
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

**type:** `typing.Optional[TestUpdateType]` — Test type. Immutable — may only echo the existing value; a different value is rejected (400). Omit to leave unchanged
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` — Replacement calibrate config. Omit to leave unchanged
    
</dd>
</dl>

<dl>
<dd>

**evaluators:** `typing.Optional[typing.List[RoutersTestsEvaluatorRef]]` — Replacement evaluator links (replaces the existing set). Omit to leave links unchanged; an empty list clears them (**rejected for `conversation` tests**)
    
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

Run tests for an agent as a background job.
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

**agent_uuid:** `str` — The agent to test. Must be in your workspace.
    
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

Run agent tests for every agent in your workspace, or for a selected set.
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

Get the status and results of a test run.
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

