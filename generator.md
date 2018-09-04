# Generator

包含两部分内容：

- Generator Functions
- Generator Expression

## Generator Functions

```python
def gen_squares(n):
    print("in gen_squares function")
    i = 0
    while i < n:
        yield i*i
        print("next i")
        i += 1


if __name__ == '__main__':
    g = gen_squares(4)
    print("type(g) = {}".format(type(g)))
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

```

Output:

```txt
type(g) = <class 'generator'>
in gen_squares function
0
next i
1
next i
4
next i
9
next i
Traceback (most recent call last):
  File "test.py", line 17, in <module>
    print(g.__next__())
StopIteration

```

Code Review:

```python
g = gen_squares(4)
print("type(g) = {}".format(type(g)))  # type(g) = <class 'generator'>
print(g.__next__())
```

When a generator function is called, it returns **a generator object** but does not begin any execution until the `__next__()` method is called the first time. At that time, the function starts executing and runs until the `yield` is reached.

> 这段话理解出三个意思即可：  
> （1）调用generator function生成generator object  
> （2）generator object并不会直接运行，需要调用`__next__()`后，function才会运行  
> （3）在function内部，遇到`yield`会暂时停下来返回数据  

When the interpreter encounters the `yield` statement, it keeps a record of the current state of the function and returns the value that is yielded. Once the next value is requested via the `__next__()` method, the internal state is loaded and the function continues from where it left off.

> 这一段是从interpreter的角度来说的，说明了yield、__next__()和internal state之间的关系。

Once the generator reaches its end, it raises the same exception as iterators do. The generator returned by the generator function is also an iterator.

> generator到达结尾的时候，会抛出StopIteration异常。  

**Generators** are a great way to simplify the creation of **iterators** since a generator is a function that produces a sequence of results and follows the interface for collections that can be iterated over as per the Python implementation of the iterator pattern. In the case of **a generator function**, the Python internals take care of the **iterator protocol** for you.

## Generator Expression

Much like we used **list comprehensions** as a shorthand to create iterators, there is a special shorthand for **generators** called **generator expressions**.

> 第一个观点：与list comprehensions做对比，引出概念generator expression。

Look at the example **generator expression** that follows. It is simply an alternative for **the generator function** we defined earlier.

> 第二个观点：generator expression是generator function的alternative

```python
g = (x*x for x in range(4))
```

**Generator expressions** can be used as **arguments** to certain functions that consume iterators, like the `max()` functions.

> 第三个观点：generator expression可以作为function的argument。

```python
print(max((x*x for x in range(4))))
```

This prints the number 9.

With Python, we can drop the **parentheses** around a generator if there is **only one argument** in the calling function.

> 第四个观点：作为function的argument时，如果只有一个参数，可以省略掉小括号。

```python
print(max(x*x for x in range(4)))
```

This is a little bit neater.


