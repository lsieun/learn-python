# Coroutine (4)

## 万物有始：协程最核心的思想

谈到并发，人最关注的是“千万不能堵着（block）”，要千方百计让CPU转起来，这样concurrency才能上去。

协程的思想本质上就是控制流的主动让出和恢复机制。在现代语言里，可以实现协程思想的方法很多，这些实现间并无高下之分，所区别的就是是否适合应用场景。参考URL：https://blog.youxu.info/2014/12/04/coroutine/

协程最早来自高性能计算领域的成功案例，协作式调度相比抢占式调度而言，可以在牺牲公平性时换取吞吐。

## 应用层面：协程解决了什么问题？

协程诞生解决的是**低速IO**和**高速的CPU**的协调问题。

## 从未来的角度来看，协程是不是未来的趋势？

协程并不是未来的趋势，只是一种解决问题的思维方式而已，它并不能解决所有的问题。

但是协程真的改进了IO操作的用户体验。协程不是趋势，它是一个在历史中被挖掘出来的、对现有问题的一个有用的补充。

## 学习Coroutine的思路

- 思维层面：想达成的目标是什么？协和的思想本质是什么？
    - 目标：千万不能堵着（block），要千方百计让CPU转起来，这样concurrency才能上去。
    - 思想本质：协程的思想本质上就是控制流的主动让出和恢复机制。
- 汇编层面：如何实现协程？
- 代码层面：如何编写协程程序？
    - 体会subroutine和coroutine的区别
- 应用层面：优点／缺点，优点决定其应用


## 其它

有时候总觉得 gevent 这类协程库是被 python 的 GIL 逼出来的，如果原生线程支持足够好，协程的必要性可能并不一定很大。




EventLoop是一个程序结构，用于等待和发送消息和事件。简单说，就是在程序中设置两个线程：一个负责程序本身的运行，称为"主线程"；另一个负责主线程与其他进程（主要是各种I/O操作）的通信，被称为"Event Loop线程"（可以译为"消息线程"）。








Coroutines and concurrency are largely orthogonal. Coroutines are a general control structure whereby flow control is cooperatively passed between two different routines without returning.

The '`yield`' statement in Python is a good example. It creates a coroutine. When the '`yield` ' is encountered the current state of the function is saved and control is returned to the calling function. The calling function can then transfer execution back to the yielding function and its state will be restored to the point where the 'yield' was encountered and execution will continue.




