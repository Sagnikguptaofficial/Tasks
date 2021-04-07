import aiohttp
import asyncio

import pickle
import random

with open ("quotes.pkl", "rb") as f:
    quotes = pickle.load(f)

numbers = random.sample(range(len(quotes)), k=15)

async def main():
    async with aiohttp.ClientSession() as session:
        for i in numbers[:10]:
            dat = {"val": i, "text": quotes[i]}
            async with session.post('http://127.0.0.1:8000/sendval/', json=dat) as resp:
                print(resp.status)
                print(await resp.text())
        await asyncio.sleep(3)

        for i in numbers[10:]:
            dat = {"val": i, "text": quotes[i]}
            async with session.post('http://127.0.0.1:8000/sendval/', json=dat) as resp:
                print(resp.status)
                print(await resp.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
