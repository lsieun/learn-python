# gevent

URL: http://www.gevent.org/
gevent tutorial: http://sdiehl.github.io/gevent-tutorial/

## What is gevent?

`gevent` is **a coroutine-based Python networking library** that uses `greenlet` to provide a high-level synchronous API on top of the `libev` or `libuv` event loop.

```python
import gevent

def foo():
    print("Running in foo")
    gevent.sleep(0)
    print("Explicit context switch to foo again")


def bar():
    print("Explicit contenxt to bar")
    gevent.sleep(0)
    print("Implicit context switch to bar again")

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
])
```

```python
import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print("Started Polling: %s" % tic())
    select.select([],[],[], 2)
    print("Ended Polling: %s" % tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print("Started Polling: %s" % tic())
    select.select([],[],[], 2)
    print("Ended Polling: %s" % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3)
])
```

```python
import gevent
import random

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0,2) * 0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchrounous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

print("Synchronous:")
synchronous()

print("Asynchronous:")
asynchrounous()

```

```python
import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests

def fetch(pid):
    r = requests.get("https://httpbin.org/get")
    txt = r.text
    print("Process %s: %s" % (pid, txt))
    return txt

def synchronous():
    for i in range(10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print("Synchronous:")
synchronous()

print("Asynchronous:")
asynchronous()

```

```python
from gevent import monkey
monkey.patch_socket()

import gevent
import requests
import time

url_list = ['https://www.baidu.com', 'https://www.sina.com.cn', 'https://cn.bing.com']

def fetch_url(pid, url):
    r = requests.get(url)
    status_code = r.status_code
    print("Fetch Url: %s %s %s" % (pid, status_code, url))

def synchronous():
    index = 0
    for url in url_list:
        index += 1
        fetch_url(index, url)

def asynchronous():
    index = 0
    threads = []
    for url in url_list:
        index += 1
        thread = gevent.spawn(fetch_url, index, url)
        threads.append(thread)
    gevent.joinall(threads)


def cost_time(func):
    start = time.time()
    func()
    print("Asynchronous time: %s" % (time.time()-start))
    
    
print("Synchronous:")
cost_time(synchronous)

print("Asynchronous:")
cost_time(asynchronous)

```


