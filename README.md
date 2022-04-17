<div align="center">
<a href="https://sinkaroid.github.io/badut"><img width="470" src="https://cdn.discordapp.com/attachments/952117487166705747/965183519728996392/badot.png" alt="badut"></a>

<h4 align="center">Python HTTP client designed to be simple</h4>

<p align="center">
	<a href="https://github.com/sinkaroid/badut/actions/workflows/build.yml"><img src="https://github.com/sinkaroid/badut/workflows/Build%20and%20docs/badge.svg"></a>
	<a href="https://codeclimate.com/github/sinkaroid/badut/maintainability"><img src="https://api.codeclimate.com/v1/badges/7857ca410413961c42f6/maintainability" /></a>
</p>

A zero-dependency HTTP library designed to be simple and async context.

<a href="https://github.com/sinkaroid/badut/blob/master/CONTRIBUTING.md">Contributing</a> •
<a href="https://sinkaroid.github.io/badut">Documentation</a> •
<a href="https://github.com/sinkaroid/badut/issues/new/choose">Report Issues</a>
</div>

---

> You enjoy using [requests](https://requests.readthedocs.io/en/master/) or [httpx](https://github.com/encode/httpx) for HTTP client, wanna try [badut](https://sinkaroid.github.io/badut/) ?
## Features
Badut is a very lightweight library, yet it handle the most of HTTP client needs.
- Zero Dependencies
- Connection Timeouts
- JSON Parsing
- Follow Redirects
- And more coming soon..

## Prerequisites
<table>
	<td><b>NOTE:</b> Python 3.7 or above</td>
</table>

## Installation
`pip install badut / pipenv install badut`

Or manual clone this repository

## Quick example
- GET request
```py
import asyncio
from badut import Badut

client = Badut(json=True, timeout=5)

async def main():
    res = await client.get("https://api.github.com/users/sinkaroid")
    print(res)
    
asyncio.run(main())
```

- POST request
```py
async def posting():
    res = await client.post("https://httpbin.org/anything",
        data={"Title": "Hello Badut", "Name": "adalah sy"})
    print(res)
    
asyncio.run(posting())
```

## Example with authentication
Some API requires additional authentication
```py
import asyncio
from badut import Badut

client = Badut(json=True, timeout=5,
    headers={
        "User-Agent": "Badut/1.0.1",
        "authorization": "Bot YouRNicET0k3nFr0mDisc0rd.XuIwOw.IXcORO2fO5XXSmugSombong",
    },
)

async def fetch_discord():
    res = await client.get("https://discord.com/api/v9/users/456298243618504707")
    print(res)
    
asyncio.run(fetch_discord())
```

## Documentation

The documentation can be found [https://sinkaroid.github.io/badut](https://sinkaroid.github.io/badut)

## Pronunciation 
<details>
<summary>See why badut exists..</summary>

> [`id_ID`](https://www.localeplanet.com/java/id-ID/index.html) • **/ba·dut/** — pelawak (dalam pertunjukan dan sebagainya);  
You created an Python HTTP module, meanwhile [requests](https://requests.readthedocs.io/en/master/) and [httpx](https://github.com/encode/httpx) is exist and those libs is more powerful  

> <img width="470" src="https://cdn.discordapp.com/attachments/952117487166705747/965142744542642186/membadut.png" alt="badut">
</details>