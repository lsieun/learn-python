# asyncio.gather vs asyncio.wait

URL: https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait

`asyncio.wait` is more low level than `asyncio.gather`.

As the name suggests, `asyncio.gather` mainly focuses on **gathering the results**. it waits on a bunch of futures and return their results in a given order.

`asyncio.wait` **just waits on the futures**. and instead of giving you the results directly, it gives done and pending tasks. **you have to mannually collect the values**.






