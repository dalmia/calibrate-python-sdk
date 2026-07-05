<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from calibrate import Calibrate


with Calibrate(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as c_client:

    res = c_client.agents.resolve(names=[])

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from calibrate import Calibrate

async def main():

    async with Calibrate(
        api_key_auth="<YOUR_API_KEY_HERE>",
    ) as c_client:

        res = await c_client.agents.resolve_async(names=[])

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->