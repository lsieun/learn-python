# What is the Python Global Interpreter Lock (GIL)?

原文： https://realpython.com/python-gil/

The Python **Global Interpreter Lock** or `GIL`, in simple words, is a **mutex** (or a lock) that allows **only one thread** to hold the control of **the Python interpreter**.

> GIL是Global Interpreter Lock的缩写。  
> 在同一个时间内，只有一个线程可以拿到Python interpreter的控制权。

This means that **only one thread** can be in **a state of execution**(状态)) at **any point in time**(时间)). The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound(计算密集型) and multi-threaded code.

> 这也就意味着，在任何时间，只有一个线程是处于运行状态的。  
> bound，有“约束”的意思，CPU-bound是受“CPU约束”的意思，更进一步理解为“计算密集型”。

Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one CPU core, the GIL has gained a reputation as an “infamous” feature of Python.

> 由于GIL只允许一个线程同时运行，在多线程和多核CPU的情况下，Python不能充分利用系统的资源，因此GIL有一个不好的名声。  

## What problem did the GIL solve for Python?

Python uses **reference counting** for **memory management**. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory occupied by the object is released.

> Python在内存管理（memory management）中使用reference counting。  
> Python-->Memory management-->reference counting

The `GIL` is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. But it effectively makes any CPU-bound Python program single-threaded.

> GIL是解决并发情况下reference counting的计数问题。  
> Python-->Memory management(内存管理)-->reference counting（内存管理的方法）-->GIL（保证内存管理安全的方法）


The `GIL`, although used by interpreters for other languages like Ruby, is not the only solution to this problem. Some languages avoid the requirement of a GIL for **thread-safe memory management** by using approaches other than **reference counting**, such as **garbage collection**.

> 与reference counting并列的内存管理方法是garbage collection。

On the other hand, this means that those languages often have to compensate for the loss of single threaded performance benefits of a GIL by adding other performance boosting features like JIT compilers.


## Why was the GIL chosen as the solution?

A lot of extensions were being written for the existing C libraries whose features were needed in Python. To prevent inconsistent changes, these C extensions required a thread-safe memory management which the GIL provided.

> 这些C类库，需要一个thread-safe memory management。GIL能够提供。

The GIL is simple to implement and was easily added to Python. It provides a performance increase to single-threaded programs as only one lock needs to be managed.

> GIL容易实现，也容易与Python融合，并且能够为single-threaded programs提升性能。

C libraries that were not thread-safe became easier to integrate. And these C extensions became one of the reasons why Python was readily adopted by different communities.

As you can see, the GIL was a pragmatic solution to a difficult problem that the CPython developers faced early on in Python’s life.

## How to deal with Python’s GIL

If the GIL is causing you problems, here a few approaches you can try:

**Multi-processing vs multi-threading**: The most popular way is to use a multi-processing approach where you use multiple processes instead of threads. Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem.

**Alternative Python interpreters**: Python has multiple interpreter implementations. **CPython**, **Jython**, **IronPython** and **PyPy**, written in `C`, `Java`, `C#` and `Python` respectively, are the most popular ones. `GIL` exists only in the original Python implementation that is **CPython**. If your program, with its libraries, is available for one of the other implementations then you can try them out as well.

**Just wait it out**: While many Python users take advantage of the single-threaded performance benefits of GIL. The multi-threading programmers don’t have to fret(烦恼) as some of the brightest minds in the Python community are working to remove the `GIL` from **CPython**. One such attempt is known as the [Gilectomy](https://github.com/larryhastings/gilectomy).

