# Asyncio

URL: https://knowpapa.com/asyncio/

## AsyncIO之名

The word `Asyncio` is made of two terms: `Async` + `I/O`.

“Async” is about **concurrency**. **Concurrency** is about doing more than one thing at a time.

> Async（异步）是关于并发(concurrency)的。  
> 所谓“并发”，就是同一时间做件事情。  

The `I/O` term there means that we use `Asyncio` to handle **I/O bound tasks** and not CPU bound tasks. “Bound task” means the thing that you are waiting on.

> IO部分则表示处理等待IO的任务。  
> 我感觉自己没有很好的理解bound task。

If you are doing, for instance, a lot of math processing, you are waiting on the processor – which is **a CPU bound task**. If on the other hand, you are waiting on say a result from the network or result from the database or an input from the user, the task is **I/O bound**.

> cpu bound task 和 i/o bound task 举例

Combining the two, `Asyncio` is the new tool to provide **concurrency** particularly for **some I/O bound task**. Concurrency ensures that you do not have to wait for I/O bound results. Asyncio is not useful if the CPU is already busy (CPU bound).

> Asyncio是为I/O bound task提供concurrency功能。

Let’s for a moment consider a simple request-response. The code below fetches the content of a given URL and sends its text as a response.

```python
import requests

def get_content(url):
    response = requests.get(url)
    return response.txt
```

Every time this code is called, it tries to fetch the response and till the time it has not received the response, it blocks all program execution. This is a bad thing. You don’t want such a wait time on say a high traffic server.

## Definitions

The `asyncio` module provides a framework that revolves around **the event loop**. An event loop basically waits for something to happen and then acts on the event. It is responsible for handling such things as I/O and system events. **Asyncio actually has several loop implementations available to it**. The module will default to the one most likely to be the most efficient for the operating system it is running under; however you can explicitly choose the event loop if you so desire. An event loop basically says “when event A happens, react with function B”.

> asyncio是围绕event loop来实现的framework。

Think of a server as it waits for someone to come along and ask for a resource, such as a web page. If the website isn’t very popular, the server will be idle for a long time. But when it does get a hit, then the server needs to react. This reaction is known as event handling. When a user loads the web page, the server will check for and call one or more event handlers. Once those event handlers are done, they need to give control back to the event loop. To do this in Python, `asyncio` uses **coroutines**.

> asyncio在event loop和event handler之间控制流的让出使用的是coroutine。

**A coroutine** is a special function that can give up control to its caller without losing its state. A coroutine is a consumer and an extension of a generator. One of their big benefits over threads is that they don’t use very much memory to execute. Note that when you call a coroutine function, it doesn’t actually execute. Instead it will return a coroutine object that you can pass to the event loop to have it executed either immediately or later on.

> 调用coroutine function，并不会直接执行，而是返回一个coroutine对象。 
> 这个coroutine对象可以放到event loop上执行。 

One other term you will likely run across when you are using the `asyncio` module is `future`. A `future` is basically an object that represents the result of work that hasn’t completed. **Your event loop** can watch `future` objects and wait for them to finish. When a `future` finishes, it is set to done. Asyncio also supports **locks** and **semaphores**.

> 我的理解：（1）future对应了coroutine的对应结果；（2）future也是由event loop来改变其状态的。

The last piece of information I want to mention is the `Task`. A `Task` is a wrapper for a `coroutine` and a subclass of `Future`. You can even schedule a `Task` using **the event loop**.

## async and await

The `async` and `await` keywords were added in Python 3.5 to define a native **coroutine** and make them a distinct type when compared with a generator based coroutine. 

In Python 3.4, you would create a coroutine like this:

```python
# Python 3.4 coroutine example
import asyncio
@asyncio.coroutine
def my_coro():
    yield from func()
```

This decorator still works in Python 3.5, but the `types` module received an update in the form of a `coroutine` function which will now tell you if what you’re interacting with is a native coroutine or not. Starting in Python 3.5, you can use `async def` to syntactically define a coroutine function. So the function above would end up looking like this:

```python
import asyncio
async def my_coro():
    await func()
```

When you define a coroutine in this manner, you cannot use `yield` inside the coroutine function. Instead it must include a `return` or `await` statement used for returning values to the caller. Note that the `await` keyword can only be used inside an `async def` function.

The `async` / `await` keywords can be considered an API to be used for asynchronous programming. The asyncio module is just a framework that happens to use `async` / `await` for programming asynchronously. There is actually a project called `curio`(https://github.com/dabeaz/curio) that proves this concept as a separate implementation of an event loop thats uses `async` / `await` underneath the covers.


## A Coroutine Example

A fairly common task that you will want to complete is downloading a file from some location, whether that be an internal resource or a file on the Internet. Usually you will want to download more than one file. So let’s create a pair of coroutines that can do that:

```python
import asyncio
import os
import urllib.request

async def download_coroutine(url):
    """
    A coroutine to download the specified url
    """
    filename = os.path.basename(url)
    r = urllib.request.urlopen(url)

    with open(filename, 'wb') as f:
        while True:
            chunk = r.read(1024)
            if not chunk:
                break
            f.write(chunk)
    msg = 'Finish downloading {filename}'.format(filename=filename)
    return msg

async def main(urls):
    """
    Creates a group of coroutines and waits for them to finish
    """
    coroutines = [download_coroutine(url) for url in urls]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())

if __name__ == '__main__': 
    urls = [
        "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
    ]

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))
    finally:
        event_loop.close()

```

Output:

```txt
Finish downloading f1040es.pdf
Finish downloading f1040a.pdf
Finish downloading f1040sb.pdf
Finish downloading f1040ez.pdf
Finish downloading f1040.pdf
```

Code:


- `asyncio.get_event_loop()` : Return an asyncio event loop.
- `event_loop.run_until_complete(main(urls))` : Run until the Future is done.
    - `run_until_complete(future)`
    - If the argument is a coroutine, it is wrapped in a `Task`.
    - Return the Future's result, or raise its exception.
- `asyncio.wait(coroutines)` : Wait for the **Futures** and **coroutines** given by `fs` to complete.
    - `wait(fs, *, loop=None, timeout=None, return_when='ALL_COMPLETED')`
    - The sequence futures must not be empty.
    - Returns two sets of Future: (done, pending).

In this code, we import the modules that we need and then create our first coroutine using the `async` syntax. This coroutine is called `download_coroutine` and it uses Python’s `urllib` to download whatever URL is passed to it. When it is done, it will return a message that says so.

The other coroutine is our `main` coroutine. It basically takes a list of one or more URLs and queues them up. We use `asyncio`’s `wait` function to wait for the coroutines to finish. Of course, to actually start the coroutines they need to be added to the event loop. We do that at the very end where we get an event loop and then call its `run_until_complete` method. You will note that we pass in the `main` coroutine to the event loop. This starts running the `main` coroutine which queues up the second coroutine and gets it going. This is known as a **chained coroutine**.

## Tasks

`Tasks` are a subclass of a `Future` and a wrapper around a **coroutine**. They give you **the ability to keep track of when they finish processing**. Because they are a type of `Future`, other coroutines can wait for a task and you can also grab the result of a task when it’s done processing. Let’s take a look at a simple example:

```python
import asyncio
import time

async def my_task(seconds):
    """
    A task to do for a number of seconds
    """
    print("This is taking {} seconds to complete".format(seconds))
    time.sleep(seconds)
    return 'task finished'

if __name__ == '__main__': 
    loop = asyncio.get_event_loop()
    try:
        print("task creation started")
        task_obj = loop.create_task(my_task(seconds=2))
        loop.run_until_complete(task_obj)
    finally:
        loop.close()
    print("The task's result was: {}".format(task_obj.result()))

```

Output:

```txt
task creation started
This is taking 2 seconds to complete
The task's result was: task finished
```

Code:

- `loop.create_task` : 
    - `create_task(coro)`
    - Schedule a coroutine object.
    - Return a task object.

Here we create an asynchronous function that accepts the number of seconds it will take for the function to run. This simulates a long running process. Then we create our event loop and then create a `task` object by calling the event loop object’s `create_task` function. The `create_task` function accepts **the function** that we want to turn into a `task`. Then we tell the event loop to run until the task completes. At the very end, we get the result of the task since it has finished.

**Tasks** can also be canceled very easily by using their `cancel` method. Just call it when you want to end a task. Should a task get canceled when it is waiting for another operation, the `task` will raise a `CancelledError`.

## how does asyncio provide asynchronicity?

`asyncio` uses a **single-threaded approach** and starts **an event loop** using a call to `asyncio.get_event_loop()`. This loop switches tasks at optimal(最适宜的) times. Most often this switching occurs when the program experiences I/O blocking, but `asyncio` can also be used to handle event driven code or to schedule a code to run at a specific future time. This is what makes it extremely useful for handling real-time updates.

Let’s look at a small piece of asyncio code.

```python
import asyncio
import aiohttp

@asyncio.coroutine
def get_content(url):
    response = yield from aiohttp.get(url)
    return (yield from response.text())
```

Here `aiohttp` is an asynchronous client and server which has some useful features web sockets, middleware and signals.

We are `yield`ing the task of getting the page to `aiohttp`. Python 3.5 has further refined this syntax as follows.

```python
import aiohttp
async def get_content(url):
    response = await aiohttp.get(url)
    return (await response.text())
```

So now instead of using the `coroutine` decorator, you simply use the keyword ‘`async`’. Similarly, instead of saying `yield from` you say ‘`await`’.

This is much more concise and takes away all the confusion there was to the difference between ‘`yield`’ and ‘`yield from`’. So now anywhere you see the word `async`, you know the function will run **asynchronously**. The ‘pausing’ is done by using the ‘`await`’ keyword.

You then use the above code with `asyncio` by running a loop as follows:

```python
import aiohttp
async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return (await resp.text())

import asyncio
loop = asyncio.get_event_loop()
content = loop.run_until_complete(
    get_content("https://httpbin.org/get")
)
print(content)
```

This, in turn, is the core concept behind asyncio.

One more thing. What do you do if you need to get the result of an `async` function in your normal synchronous code?

You use `asyncio.Future()`. A `Future` represents the result of a function that is yet to complete. The `asyncio` event loop can watch for a Future object’s state, thus allowing your normal synchronous code to wait for the blocking part to finish some work.

Here’s an example that shows this.











