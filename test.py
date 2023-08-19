import asyncio

import aiohttp

target = "https://api64.ipify.org"
target2 = "https://web.telegram.org/a/"
schema = 'http'
url = '185.155.233.153'
url2 = '89.117.250.154'
port = '50100'
username = 'loslyusar'
password = 'uKFgqacpvp'
proxy = f'{schema}://{username}:{password}@{url2}:{port}'


async def main():
    async with aiohttp.ClientSession() as sess:
        async with sess.get(target, proxy=proxy) as request:
            response = await request.text()
            print(response)

asyncio.run(main())
