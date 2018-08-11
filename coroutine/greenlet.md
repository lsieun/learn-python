# greenlet

参考URL：https://greenlet.readthedocs.io/en/latest/
Github: https://github.com/python-greenlet/greenlet

## Introduction

A “`greenlet`” is **a small independent pseudo-thread**. 

> greentlet 是一个小的、独立的 pseudo-thread。  
> 这么写的目的是什么呢？ 对于编程人员，线程（thread）是一个熟知的概念；为了便于理解greenlet，在这里将greentlet称之为pseudo-thread(伪线程)。这种写作手法就是，通过一种我们所熟悉的事物，去认识一种新的事物。

Think about it as **a small stack of frames**; **the outermost (bottom) frame** is the initial function you called, and **the innermost frame** is the one in which the greenlet is currently paused. 

> 这里将greentlet理解为a small stack of frames。

You work with greenlets by **creating a number of such stacks** and **jumping execution between them**. Jumps are never implicit: **a greenlet must choose to jump to another greenlet**, which will cause **the former to suspend** and **the latter to resume where it was suspended**. Jumping between greenlets is called “**switching**”.

> 这里讲了如何使用greenlet进行工作：（1）创建一些greenlet；（2）在这些greenlet之间进行跳转(switching)。
> 在进行greenlets之间进行跳转(switching)的时候，会导致greenlet的状态（suspend/resume）发生变化。


When you create a greenlet, it gets **an initially empty stack**; when you first switch to it, it starts to run a specified function, which may call other functions, switch out of the greenlet, etc. When eventually the outermost function finishes its execution, the greenlet’s stack becomes empty again and the greenlet is “dead”. Greenlets can also die of an uncaught exception.

> 这里讲述了greenlet从“生“到”死“的过程。
> greenlet的“死”有两种方式：（1）执行结束；（2）发生异常。

For Example:

```python
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
```

输出：
```
12
56
34
```

The last line jumps to `test1`, which prints `12`, jumps to `test2`, prints `56`, jumps back into `test1`, prints `34`; and then `test1` finishes and `gr1` dies. At this point, the execution comes back to the original `gr1.switch()` call. **Note** that `78` is never printed.

## Parents

Let’s see **where execution goes when a greenlet dies**. Every greenlet has **a “parent” greenlet**. **The parent greenlet** is initially the one in which the greenlet was created (this can be changed at any time). **The parent is where execution continues when a greenlet dies**. This way, **greenlets are organized in a tree**. Top-level code that doesn’t run in a user-created greenlet runs in the **implicit “main” greenlet**, which is **the root of the tree**.

> 当greenlet执行结束的时候，控制流会到哪里呢？答案是parent greenlet。
> greenlets是一种树状的组织结构。树状结构的根(root)是main greenlet。

In the above example, both `gr1` and `gr2` have **the main greenlet** as **a parent**. Whenever one of them dies, the execution comes back to **the main greenlet**.

```python
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)

main_greenlet = greenlet.getcurrent()
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print(main_greenlet == gr1.parent)
print(main_greenlet == gr2.parent)
```

## Instantiation

`greenlet.greenlet` is the `greenlet` type, which supports the following operations:

- `greenlet(run=None, parent=None)`: Create a new greenlet object (without running it). `run` is the callable to invoke, and `parent` is the parent greenlet, which defaults to **the current greenlet**.
- `greenlet.getcurrent()`: Returns the current greenlet (i.e. the one which called this function).
- `greenlet.GreenletExit`: This special exception does not propagate to the parent greenlet; it can be used to kill a single greenlet.

The `greenlet` type can be subclassed, too. A greenlet runs by calling its `run` attribute, which is normally set when the greenlet is created; but for subclasses it also makes sense to define a `run` method instead of giving a `run` argument to the constructor.


## Switching

Switches between greenlets occur when the method `switch()` of a greenlet is called, in which case execution jumps to the greenlet whose `switch()` is called, or when a greenlet dies, in which case execution jumps to the parent greenlet. During a switch, **an object** or an exception is “sent” to **the target greenlet**; this can be used as a convenient way to pass information between greenlets. For example:

```python
from greenlet import greenlet

def test1(x, y):
    z = gr2.switch(x+y)
    print(z)

def test2(u):
    print(u)
    gr1.switch(42)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch("Hello", "World")
```

This prints “`hello world`” and `42`, with the same order of execution as the previous example. Note that the arguments of `test1()` and `test2()` are not provided when the greenlet is created, but only the first time someone switches to it.

Here are the precise rules for sending objects around:

- `g.switch(*args, **kwargs)`: Switches execution to the greenlet `g`, sending it the given arguments. As a special case, if `g` did not start yet, then it will start to run now.


## Methods and attributes of greenlets

- `g.switch(*args, **kwargs)`: Switches execution to the greenlet `g`. 
- `g.run`: The callable that `g` will run when it starts. After `g` started, this attribute no longer exists.
- `g.parent`: The parent greenlet. This is writeable, but it is not allowed to create cycles of parents.
- `g.gr_frame`: The current top frame, or None.
- `g.dead`: True if `g` is dead (i.e. it finished its execution).
- `bool(g)`: True if `g` is active, False if it is dead or not yet started.

## Greenlets and Python threads

Greenlets can be combined with Python threads; in this case, each thread contains an independent “main” greenlet with a tree of sub-greenlets. It is not possible to mix or switch between greenlets belonging to different threads.


