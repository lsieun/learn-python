# threading

```python
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
```

## 从一个线程的角度出发

- 创建线程
    - `name`：线程名称
    - `target`：线程要执行的代码函数
    - `args`：代码函数需要的参数
    - `daemon`：是否是daemon状态运行

- 启动线程


## 从多个线程的角度出发

- 获取当前线程：threading.current_thread()
- 获取当前进程中所有线程：threading.enumerate()
- 多个线程之间的通信Signal：体现的是多线程之间的“协作”关系
    - Event: internal flag / set() clear() wait()
    - Condition
    - Barrier
- 对待资源(resource/data)的使用：体现的是多线程之间解决“有限资源”的冲突问题

程序是由“数据”和“算法”构成。算法，从现实生活中来说，它的作用是解决实际的问题，但从编译器或解释器的角度来说，它就是代码执行路径的描述。





