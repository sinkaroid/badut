import asyncio
from badut import Badut
import pytest

client = Badut(json=True, timeout=5)

@pytest.mark.asyncio
async def posting():
    res = await client.post(
        "https://httpbin.org/anything",
        data={"Title": "Hello Badut", "Name": "dari badut"},
    )
    print(res)

asyncio.run(posting())
