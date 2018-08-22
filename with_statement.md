# Understanding Python's "with" statement

URL: https://sdqali.in/blog/2012/07/09/understanding-pythons-with-statement/

文章分成两部分内容：

- 第一部分内容讲What
- 第二部分内容讲How

## 1、What is it?

Python’s `with` statement provides a very convenient way of dealing with the situation where you have to do a setup and teardown to make something happen. A very good example for this is the situation where you want to gain a handler to a file, read data from the file and the close the file handler.

Without the `with` statement, one would write something along the lines of:

```python
file = open("/tmp/foo.txt")
data = file.read()
file.close()
```

There are **two annoying things** here. **First**, you end up forgetting to close the file handler. **The second** is how to handle exceptions that may occur once the file handler has been obtained. One could write something like this to get around this:

```python
file = open("/tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()
```

While this works well, it is unnecessarily verbose. This is where `with` is useful. The good thing about `with` apart from the better syntax is that it is very good handling exceptions. The above code would look like this, when using `with`:

```python
with open("/tmp/foo.txt") as file:
   data = file.read()
```

## 2、How does it work?

While this might look like magic, the way Python handles with is more clever than magic. The basic idea is that the statement after `with` has to evaluate an object that responds to an `__enter__()` as well as an `__exit__()` function.

After the statement that follows `with` is evaluated, the `__enter__()` function on the resulting object is called. The value returned by this function is assigned to the variable following `as`. After every statement in the block is evaluated, the `__exit__()` function is called.

This can be demonstrated with the following example:

```python
# with_example01.py

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")

def get_sample():
    return Sample()

with get_sample() as sample:
    print("Sample:", sample)
```

When executed, this will result in:

```txt
In __enter__()
Sample: Foo
In __exit__()
```

As you can see,

1. The `__enter__()` function is executed
2. The value returned by it - in this case "Foo" is assigned to `sample`
3. The body of the block is executed, thereby printing the value of `sample` ie. "Foo"
4. The `__exit__()` function is called.

What makes `with` really powerful is the fact that **it can handle exceptions**. You would have noticed that the `__exit__()` function for `Sample` takes three arguments - `type`, `value` and `trace`. These are useful in exception handling. Let’s see how this works by modifying the above example.

```python
# with_example02.py

class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("="*66)
        print("type:", type)
        print("value:", value)
        print("trace:", trace)
        print("="*66)

    def do_something(self):
        bar = 1 / 0
        return bar + 10

with Sample() as sample:
    sample.do_something()

```

Notice how in this example, instead of `get_sample()`, `with` takes `Sample()`. It does not matter, as long as the statement that follows `with` evaluates to an object that has an `__enter__()` and `__exit__()` functions. In this case, `Sample()`’s `__enter__()` returns the newly created instance of `Sample` and that is what gets passed to `sample`.

When executed:

```txt
==================================================================
type: <class 'ZeroDivisionError'>
value: division by zero
trace: <traceback object at 0x7f438666afc8>
==================================================================
Traceback (most recent call last):
  File "with_example02.py", line 19, in <module>
    sample.do_something()
  File "with_example02.py", line 15, in do_something
    bar = 1 / 0
ZeroDivisionError: division by zero
```

Essentially, if there are exceptions being thrown from anywhere inside the block, the `__exit__()` function for the object is called. As you can see, the `type`, `value` and the stack `trace` associated with the exception thrown is passed to this function. In this case, you can see that there was a `ZeroDivisionError` exception being thrown. People implementing libraries can write code that clean up resources, close files etc. in their `__exit__()` functions.

Thus, Python’s with is a nifty(有技巧的；灵便的) construct that makes code a little less verbose and makes cleaning up during exceptions a bit easier.

> 总结：  
> （1）with让代码更简洁 less verbose  
> （2）with可以处理exception

