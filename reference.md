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

Resolve a list of agent names to their UUIDs within the caller's org.

Auth accepts either a JWT (frontend) or an `sk_` API key (programmatic
clients) via `get_org_jwt_or_api_key`, so CI tooling can map human-friendly
agent names to the UUIDs the run/poll endpoints expect. Agent names are
unique per org, so each name resolves to at most one agent. Names with no
matching (non-deleted) agent in the org are returned under `not_found`.
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
        "names"
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

**names:** `typing.List[str]` 
    
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

<details><summary><code>client.agents.<a href="src/calibrate/agents/client.py">list</a>() -> typing.List[RoutersAgentToolsAgentResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agents for the caller's current org.

Auth accepts either a JWT (frontend) or an `sk_` API key (programmatic
clients) via `get_org_jwt_or_api_key`, so CI tooling can enumerate every
agent UUID in the org without knowing names up front (the run/poll and
`/resolve` endpoints accept the same key).
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

## AgentTests
<details><summary><code>client.agent_tests.<a href="src/calibrate/agent_tests/client.py">run</a>(...) -> TaskCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run one or more tests for an agent.

This starts a background task that runs the calibrate LLM tests command
with the agent's config and the combined test cases from all specified tests.

Returns a task ID that can be used to poll for status and results.

Auth: requires either a JWT (frontend) or an `sk_` API key. The agent
must belong to the caller's org or this 404s.
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
    agent_uuid="agent_uuid",
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

**agent_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**test_uuids:** `typing.Optional[typing.List[str]]` 
    
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

Run every linked test for a set of agents, one ``llm-unit-test`` job per agent.

Scope is driven by the optional ``agent_names`` payload:

- **Provided (non-empty)** — run only those agents. Names are unique per org
  and **all are validated up front**: if any doesn't resolve to a
  (non-deleted) agent in the caller's org, the call 404s with the offending
  names and NO jobs are created.
- **Omitted / null / empty** — run every agent in the caller's org.

For each selected agent, its linked tests are launched as one job. Agents
with no linked tests or an unverified connection are reported under
``skipped`` instead of failing the batch. Subject to the normal per-org
concurrency queue, so over-limit jobs come back ``queued``.

Auth accepts a JWT (frontend) or an `sk_` API key (programmatic clients).
Returns one ``runs`` entry per launched agent with ``agent_name``,
``agent_uuid``, ``task_id``, and ``status``.
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

Get the status of an agent test run.

Requires either a JWT (frontend) or an `sk_` API key, plus org
ownership of the run. Unauthenticated access to a completed run is only
possible once it is made public, via the share-token endpoint in the public
router.

Returns the current status and, if done, the test results.
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
    task_id="task_id",
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

**task_id:** `str` 
    
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

