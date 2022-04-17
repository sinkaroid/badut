import asyncio
from badut import Badut
import pytest

client = Badut(json=True, timeout=5)

@pytest.mark.asyncio
async def main():
    res = await client.get("https://api.github.com/users/sinkaroid")
    print(res)

asyncio.run(main())
