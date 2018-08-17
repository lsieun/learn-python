# gevent

URL: http://www.gevent.org/  
gevent tutorial: http://sdiehl.github.io/gevent-tutorial/

## 1、What is gevent?

`gevent` is **a coroutine-based Python networking library** that uses `greenlet` to provide a high-level synchronous API on top of the `libev` or `libuv` event loop.

> gevent是基于greenlet的。

**Greenlets** all run inside of the OS process for the main program but are scheduled cooperatively. **Only one greenlet** is ever running at any given time.

> 多个greenlet之间是协作运行的，但只有一个greenlet是处于运行状态的。

## 2、Getting Started

The core idea of **concurrency** is that **a larger task** can be broken down into **a collection of subtasks** which are scheduled to run simultaneously or asynchronously, instead of one at a time or synchronously. **A switch** between the two subtasks is known as a **context switch**.

> 并发的核心思想就是：大任务可以拆分成一系列的小任务，然后多个小任务同时运行。  
> 多个小任务之间的switch，称为context switch。  

**A context switch** in gevent is done through **yielding**. In this example we have two contexts which yield to each other through invoking `gevent.sleep(0)`.

> context switch是通过yield来实现的。

### 2.1、Hello World

```python
import gevent

def foo():
    print("Running in foo")
    gevent.sleep(0)
    print("Explicit context switch to foo again")

def bar():
    print("Explicit context to bar")
    gevent.sleep(0)
    print("Implicit context switch back to bar")

if __name__ == '__main__':
    g1 = gevent.spawn(foo)
    g2 = gevent.spawn(bar)
    print("type(g1) = %s" % type(g1))
    print("type(g2) = %s" % type(g2))
    gevent.joinall([g1, g2])
```

输出：
```txt
type(g1) = <class 'gevent.greenlet.Greenlet'>
type(g2) = <class 'gevent.greenlet.Greenlet'>
Running in foo
Explicit context to bar
Explicit context switch to foo again
Implicit context switch back to bar
```

代码解读：

- `gevent.sleep(0)` : Put the current greenlet to sleep for at least `seconds`
    - `def sleep(seconds=0, ref=True)`
- `gevent.spawn(foo)` : Create a new class `Greenlet` object and schedule it to run. This can be used as `gevent.spawn` or `Greenlet.spawn`.
    - `spawn = Greenlet.spawn`
    - `def spawn(cls, *args, **kwargs)`
- `gevent.joinall([g1, g2])` : Wait for the ``greenlets`` to finish.
    - `def joinall(greenlets, timeout=None, raise_error=False, count=None)`

The real power of **gevent** comes when we use it for network and IO bound functions which can be cooperatively scheduled. Gevent has taken care of all the details to ensure that your network libraries will implicitly yield their greenlet contexts whenever possible. 

> 当用于网络或IO密集型的函数时，gevent才真正发挥它的效用。

### 2.2、Multiple task

Another somewhat synthetic example defines a task function which is non-deterministic (i.e. its output is not guaranteed to give the same result for the same inputs). In this case the side effect of running the function is that the task pauses its execution for a random number of seconds.

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

输出：
```txt
Synchronous:
task 1 done
task 2 done
task 3 done
task 4 done
task 5 done
task 6 done
task 7 done
task 8 done
task 9 done
Asynchronous:
task 1 done
task 3 done
task 4 done
task 6 done
task 7 done
task 9 done
task 0 done
task 2 done
task 5 done
task 8 done
```

代码解读：

```python
def synchronous():
    for i in range(1,10):
        task(i)
```

In the `synchronous` case all the tasks are run sequentially, which results in the main programming blocking ( i.e. pausing the execution of the main program ) while each task executes.

```python
def asynchrounous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)
```
The important parts of the program are the `gevent.spawn` which wraps up the given function inside of a Greenlet thread. The list of initialized greenlets are stored in the array `threads` which is passed to the `gevent.joinall` function which blocks the current program to run all the given greenlets. The execution will step forward only when all the greenlets terminate.

The important fact to notice is that the order of execution in the async case is essentially random and that the total execution time in the async case is much less than the sync case. In fact the maximum time for the synchronous case to complete is when each tasks pauses for 0.002 seconds resulting in a 0.02 seconds for the whole queue. In the async case the maximum runtime is roughly 0.002 seconds since none of the tasks block the execution of the others.

### 2.3、Network Request

In a more common use case, asynchronously fetching data from a server, the runtime of `fetch()` will differ between requests, depending on the load on the remote server at the time of the request.

```python
import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests
import time

def fetch(url):
    r = requests.get(url)
    status_code = r.status_code
    print("%s %s" % (status_code, url))

def synchronous(url_list):
    for url in url_list:
        fetch(url)

def asynchronous(url_list):
    threads = [gevent.spawn(fetch, url) for url in url_list]
    gevent.joinall(threads)

def cost_time(func, url_list):
    start_time = time.time()
    func(url_list)
    end_time = time.time()
    diff_time = end_time - start_time
    print("Cost time: %s" % diff_time)

if __name__ == '__main__':
    url_list = [
        "https://www.baidu.com",
        "https://www.sina.com.cn",
        "https://www.taobao.com",
        "https://www.jd.com"
    ]
    print("Synchronous:")
    cost_time(synchronous, url_list)
    print("Asynchronous:")
    cost_time(asynchronous, url_list)
```

输出：
```txt
Synchronous:
200 https://www.baidu.com
200 https://www.sina.com.cn
200 https://www.taobao.com
200 https://www.jd.com
Cost time: 1.247446060180664
Asynchronous:
200 https://www.baidu.com
200 https://www.sina.com.cn
200 https://www.taobao.com
200 https://www.jd.com
Cost time: 0.8907566070556641
```

代码解读：

- `gevent.monkey.patch_socket()` : Replace the standard socket object with gevent's cooperative sockets.


### 2.4、Monkeypatching

If you noticed above we invoked the command `monkey.patch_socket()`. This is a purely side-effectful command to modify the standard library's socket library.

```python
import socket
print(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)
```

输出结果：
```txt
<class 'socket.socket'>
After monkey patch
<class 'gevent._socket3.socket'>
<built-in function select>
After monkey patch
<function select at 0x7f49c841af28>
```

Python's runtime allows for most objects to be modified at runtime including modules, classes, and even functions. This is generally an astoudingly bad idea since it creates an "implicit side-effect" that is most often extremely difficult to debug if problems occur, nevertheless in extreme situations where a library needs to alter the fundamental behavior of Python itself **monkey patches** can be used. In this case gevent is capable of patching most of the blocking system calls in the standard library including those in socket, ssl, threading and select modules to instead behave cooperatively.

For example, the Redis python bindings normally uses regular tcp sockets to communicate with the redis-server instance. Simply by invoking `gevent.monkey.patch_all()` we can make the redis bindings schedule requests cooperatively and work with the rest of our gevent stack.

This lets us integrate libraries that would not normally work with gevent without ever writing a single line of code. While monkey-patching is still evil, in this case it is a "useful evil".

## 3、Data Structures

### 3.1、Events

Events are a form of asynchronous communication between Greenlets.

```python
import gevent
from gevent.event import Event

evt = Event()

def setter():
    '''After 3 seconds, wake all threads waiting on the value of evt'''
    print("A: Hey wait for me, I have to do something")
    gevent.sleep(3)
    print("OK! I'm done")
    evt.set()

def waiter():
    '''After 3 seconds the get call will unblock'''
    print("I'll wait for you")
    evt.wait() # blocking
    print("It's about time")

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
    ])

if __name__ == '__main__': main()
```

Output:
```txt
A: Hey wait for me, I have to do something
I'll wait for you
I'll wait for you
I'll wait for you
I'll wait for you
I'll wait for you
OK! I'm done
It's about time
It's about time
It's about time
It's about time
It's about time
```

Code:

- `Event` : A synchronization primitive that allows one greenlet to wake up one or more others.
- `evt.wait()` : Block until the internal flag is true.
    - `def wait(self, timeout=None)`
- `evt.set()` : Set the internal flag to true.
    - `def set(self)`

### 3.2、Queue

`Queues` are ordered sets of data that have the usual `put` / `get` operations but are written in a way such that they can be safely manipulated across Greenlets.

For example if one Greenlet grabs an item off of the queue, the same item will not be grabbed by another Greenlet executing simultaneously.

```python
import gevent
from gevent.queue import Queue

tasks = Queue()

def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print("Worker %s got task %s" % (n, task))
        gevent.sleep(0)

    print("Quitting time!")

def boss():
    for i in range(1, 25):
        tasks.put_nowait(i)

gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'nancy')
])

```

Output:

```txt
Worker steve got task 1
Worker john got task 2
Worker nancy got task 3
Worker steve got task 4
Worker john got task 5
Worker nancy got task 6
Worker steve got task 7
Worker john got task 8
Worker nancy got task 9
Worker steve got task 10
Worker john got task 11
Worker nancy got task 12
Worker steve got task 13
Worker john got task 14
Worker nancy got task 15
Worker steve got task 16
Worker john got task 17
Worker nancy got task 18
Worker steve got task 19
Worker john got task 20
Worker nancy got task 21
Worker steve got task 22
Worker john got task 23
Worker nancy got task 24
Quitting time!
Quitting time!
Quitting time!
```

Code:

- `Queue` : Create a queue object with a given maximum size.
- `tasks.put_nowait(i)` : Put an item into the queue without blocking.
    - `def put_nowait(self, item)`
- `tasks.get()` : Remove and return an item from the queue.
    - `def get(self, block=True, timeout=None)`



