import asyncio

import aiohttp
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector

target = "https://api64.ipify.org"
target2 = "https://web.telegram.org/a/"
schema = 'socks5'
url = '185.155.233.153'
url2 = '89.117.250.154'
port = '50101'
username = 'loslyusar'
password = 'uKFgqacpvp'
proxy = f'{schema}://{username}:{password}@{url2}:{port}'


async def fetch(url):
    connector = ProxyConnector.from_url(proxy)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()


print(asyncio.run(fetch(target)))
