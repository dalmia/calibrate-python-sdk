# Calibrate Python SDK

Python client for [Calibrate](https://calibrate.artpark.ai), a framework for evaluating AI agents which let you move from slow, manual testing to a fast, automated, and repeatable testing process for your entire agent stack.

## Installation

```sh
pip install calibrate-python-sdk
```

## Usage

```python
from calibrate_python_sdk import Calibrate

client = Calibrate(api_key="sk_your_api_key") # get the API key from the UI

agents = client.agents.list()
```
