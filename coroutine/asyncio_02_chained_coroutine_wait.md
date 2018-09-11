# asyncio の Chaining Coroutines & await and asyncio.wait

## 1、Chaining Coroutines & await coroutine

**One coroutine** can start **another coroutine** and wait for the results, which makes it easier to decompose a task into reusable parts. The following example has two phases that must be executed in order, but that can run concurrently with other operations.

> 一个coroutine可以启动另一个coroutine。

The `await` keyword is used instead of adding the **new coroutines** to **the loop**. Because control flow is already inside of **a coroutine** being managed by **the loop**, it is not necessary to tell **the loop** to manage **the new coroutines**.

```python
import asyncio

async def outer():     # 直接加入event loop
    print("in outer")
    print("waiting for result1")
    result1 = await phase1()           # 这里使用了await coroutine
    print("waiting for result2")
    result2 = await phase2(result1)    # 这里使用了await coroutine
    return (result1, result2)

async def phase1():    # 间接加入event loop
    print("in phase1")
    return "result1"

async def phase2(arg): # 间接加入event loop
    print("in phase2")
    return "result2 derived from {}".format(arg)


if __name__ == "__main__":
    event_loop: asyncio.SelectorEventLoop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        print("return value: {!r}".format(return_value))
    finally:
        event_loop.close()

```

Output:

```txt
in outer
waiting for result1
in phase1
waiting for result2
in phase2
return value: ('result1', 'result2 derived from result1')
```

## 2、Chaining Coroutines & await asyncio.wait

```python
import asyncio
import os
from urllib import request

async def download_file(url: str) -> str:
    """
    a coroutine to download the specified url
    """
    filename = os.path.basename(url)
    resp = request.urlopen(url)

    with open(filename, "wb") as f:
        while True:
            chunk = resp.read(1024)
            if not chunk:
                break
            f.write(chunk)

    msg = "Finish downloading {filename}".format(filename=filename)
    return msg

async def main():
    """
    Create a group of coroutines and waits for them to finish
    """
    url_list = [
        "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
    ]
    coroutines = [download_file(url) for url in url_list]
    completed, pending = await asyncio.wait(coroutines)    # 这里使用了await asyncio.wait()
    for item in completed:
        print(item.result())


if __name__ == "__main__":
    event_loop: asyncio.SelectorEventLoop = asyncio.get_event_loop()
    try:
        coro = main()
        event_loop.run_until_complete(coro)
    finally:
        event_loop.close()

```

代码讲解： https://docs.python.org/3/library/asyncio-task.html

- `completed, pending = await asyncio.wait(coroutines)`:
    - `coroutine asyncio.wait(futures, *, loop=None, timeout=None, return_when=ALL_COMPLETED)`
    - Wait for the **Futures** and **coroutine** objects given by the sequence `futures` to complete. **Coroutines** will be wrapped in **Tasks**. Returns two sets of `Future`: `(done, pending)`.
    - The sequence `futures` must not be empty.
    - `timeout` can be used to control **the maximum number of seconds** to wait before returning. `timeout` can be an `int` or `float`. If `timeout` is not specified or `None`, there is no limit to the wait time.
    - `return_when` indicates when this function should return. It must be one of the following constants of the `concurrent.futures` module: `FIRST_COMPLETED`, `FIRST_EXCEPTION` and `ALL_COMPLETED`.
    - Usage: `done, pending = await asyncio.wait(fs)`



In this code, we create our first coroutine using the `async` syntax. This coroutine is called `download_file` and it uses Python’s `urllib` to download whatever URL is passed to it. When it is done, it will return a message(`msg`) that says so.

The second coroutine is our `main` coroutine. It basically takes a list of one or more URLs and queues them up. We use `asyncio`’s `wait` function to wait for the coroutines to finish. Of course, to actually **start the coroutines** they need to be added to **the event loop**. We do that at the very end where we get **an event loop** and then call its `run_until_complete` method. You will note that we pass in the `main` coroutine to **the event loop**. This starts running the `main` coroutine which queues up the second coroutine and gets it going. This is known as a **chained coroutine**.


> 这段的意思：  
> （1）coroutine需要放到event loop上才能运行  
> （2）main()方法是直接放到event loop的run_util_complete()方法上的  
> （3）download_file()并没有直接放到event loop上运行，而是在main()方法里调用了asyncio.wait()方法，从而使得download_file()能够在event loop上运行。这种方式称之为chained coroutine。  














