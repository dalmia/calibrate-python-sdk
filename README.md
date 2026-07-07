# Calibrate Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fdalmia%2Fcalibrate-python-sdk)
[![pypi](https://img.shields.io/pypi/v/calibrate-sdk)](https://pypi.python.org/pypi/calibrate-sdk)

The Calibrate Python SDK provides convenient, typed access to the Calibrate
agent evaluation platform API. Authenticate with an API key (`sk_…`) scoped
to your organization to run agent tests and poll their results.


## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Pre Requisites](#pre-requisites)
- [Reference](#reference)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)

## Documentation

API reference documentation is available [here](${PUBLIC_API_BASE_URL}/public-api/docs).

## Installation

```sh
pip install calibrate-sdk
```

## Pre-requisites

You need to have a Calibrate API key. You can get the API key from the [UI](https://calibrate.artpark.ai/workspace-settings?tab=api-keys).

## Reference

A full reference for this library is available [here](https://github.com/dalmia/calibrate-python-sdk/blob/HEAD/./reference.md).

## Quick Start

```python
from calibrate import Calibrate

client = Calibrate(api_key="sk_...")

# List the agents in your organization
agents = client.agents.list()

# Kick off a test run for an agent and poll for the result
run = client.agent_tests.run(agent_uuid="<agent-uuid>")
result = client.agent_tests.get_run(task_id=run.task_id)
```


## Usage

Instantiate and use the client with the following:

```python
from calibrate import Calibrate

client = Calibrate(
    api_key="<value>",
)

client.agents.resolve(
    names=[
        "my-agent",
        "support-bot"
    ],
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from calibrate import Calibrate
from calibrate.environment import CalibrateEnvironment

client = Calibrate(
    environment=CalibrateEnvironment.DEFAULT,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from calibrate import AsyncCalibrate

client = AsyncCalibrate(
    api_key="<value>",
)


async def main() -> None:
    await client.agents.resolve(
        names=[
            "my-agent",
            "support-bot"
        ],
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from calibrate.core.api_error import ApiError

try:
    client.agents.resolve(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from calibrate import Calibrate

client = Calibrate(...)
response = client.agents.with_raw_response.resolve(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.agents.resolve(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from calibrate import Calibrate

client = Calibrate(..., timeout=20.0)

# Override timeout for a specific method
client.agents.resolve(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from calibrate import Calibrate

client = Calibrate(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

