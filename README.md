# Calibrate Python SDK

Python client for [Calibrate](https://calibrate.artpark.ai), a framework for evaluating AI agents which let you move from slow, manual testing to a fast, automated, and repeatable testing process for your entire agent stack.

## Installation

```sh
pip install calibrate-python-sdk
```

## Usage

```python
from calibrate_python_sdk import Calibrate

client = Calibrate(token="sk_your_api_key")

agents = client.agents.list()
```

This SDK is generated from Calibrate's public API with [Fern](https://buildwithfern.com).
