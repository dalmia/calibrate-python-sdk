# Calibrate Python SDK

Python client for [Calibrate](https://calibrate.artpark.ai), a framework for evaluating AI agents which let you move from slow, manual testing to a fast, automated, and repeatable testing process for your entire agent stack.

## Installation

```sh
pip install calibrate-sdk
```

Or with `uv`:

```sh
uv add calibrate-sdk
```

## Pre-requisites

You need to have a Calibrate API key. You can get the API key from the [UI](https://calibrate.artpark.ai/workspace-settings?tab=api-keys).

## Usage

```python
from calibrate import Calibrate

client = Calibrate(api_key="your_api_key")

agents = client.agents.list()
```

For self-hosted Calibrate deployments, you can pass `base_url` to point the client at your API instance:

```python
from calibrate import Calibrate

client = Calibrate(
    base_url="https://api.calibrate.your-domain.com",
    api_key="your_api_key",
)

agents = client.agents.list()
```
