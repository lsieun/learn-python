# asyncio の event loop & coroutine

The `asyncio` module provides a framework that revolves around **the event loop**. **An event loop** basically waits for something to happen and then acts on the **event**. It is responsible for handling such things as I/O and system events. **Asyncio actually has several loop implementations available to it**. The module will default to the one most likely to be the most efficient for the operating system it is running under; however you can explicitly choose the event loop if you so desire. An event loop basically says “when event A happens, react with function B”.

> asyncio是围绕event loop来实现的framework。

Think of a server as it waits for someone to come along and ask for a resource, such as a web page. If the website isn’t very popular, the server will be idle for a long time. But when it does get a hit, then the server needs to react. This reaction is known as `event handling`. When a user loads the web page, the server will check for and call one or more event handlers. Once those **event handlers** are done, they need to give control back to **the event loop**. To do this in Python, `asyncio` uses **coroutines**.

> asyncio在event loop和event handler之间控制流的让出使用的是coroutine。


## 1、coroutine

「what is coroutine?」**A coroutine** is a special function that can give up control to its caller without losing its state. 

「coroutine优点」**One of their big benefits** over threads is that they **don’t use very much memory** to execute. 

「coroutine function返回值类型」Note that when you call **a coroutine function**, it doesn’t actually execute. Instead it will return a `coroutine` object that you can pass to **the event loop** to have it executed either immediately or later on.

以上是coroutine的概念，下面是coroutine的代码示例。

```python
async def my_coro():
    await func()
```

Note that the `await` keyword can only be used inside an `async def` function.

> 这句话的解读：
> （1）await关键字只能在async def function中使用。  
> （2）但是，async def function中可以不使用await关键字。

## 2、event loop

```python
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()
```

代码讲解：

- `asyncio.get_event_loop()`: 
    - `def get_event_loop()`: Return an asyncio event loop.
- `event_loop.run_until_complete()`：
    - `def run_until_complete(self, future)`: Run until the Future is done.
    - If **the argument** is a `coroutine`, it is wrapped in a `Task`.
    - Return the `Future`'s result, or raise its exception.
- `event_loop.close()`: 
    - `def close(self)`: Close the event loop.

检验`event_loop`的类型：

```python
isinstance(event_loop, asyncio.SelectorEventLoop) # True
```



## 3、最简单的demo

```python
import asyncio

async def coroutine():
    print("in coroutine")


if __name__ == "__main__":
    event_loop: asyncio.SelectorEventLoop = asyncio.get_event_loop()
    try:
        print("starting coroutine")
        coro = coroutine() # type(coro) = <class 'coroutine'>
        print("entering event loop")
        event_loop.run_until_complete(coro)
    finally:
        print("closing event loop")
        event_loop.close()

```

Output:

```txt
starting coroutine
entering event loop
in coroutine
closing event loop
```



## 4、下载文件的demo

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
    completed, pending = await asyncio.wait(coroutines)
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




