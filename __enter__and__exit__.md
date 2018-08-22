# Explaining Python's '__enter__' and '__exit__'

URL: https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit

## 示例：应用场景

Using these magic methods (`__enter__`, `__exit__`) allows you to implement objects which can be used easily with the `with` statement.

A useful example could be a database connection object (which then automagically closes the connection once the corresponding '`with`'-statement goes out of scope):

```python
class DatabaseConnection(object):

    def __enter__(self):
        # make a database connection and return it
        ...
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.dbconn.close()
        ...
```

## context manager

If you know what **context managers** are then you need nothing more to understand `__enter__` and `__exit__` magic methods. Lets see a very simple example.

In this example I am opening `myfile.txt` with help of `open` function. The `try/finally` block ensures that even if an unexpected exception occurs `myfile.txt` will be closed.

```python
fp = open("myfile.txt","r")
print("fp is closed?", fp.closed)

try:
    for line in fp.readlines():
        print(line)
finally:
    fp.close()

print("fp is closed?", fp.closed)
```

Output:

```txt
fp is closed? False
Hello

Python

World

fp is closed? 
```

Now I am opening same file with `with` statement:

```python
with open("myfile.txt", "r") as fp:
    print("fp is closed?", fp.closed)
    for line in fp.readlines():
        print(line)

print("fp is closed?", fp.closed)
```

Output:

```txt
fp is closed? False
Hello

Python

World

fp is closed? True
```

If you look at the code, I didn't close the file and there is no `try/finally` block. Because `with` statement automatically closes `myfile.txt`. You can even check it by calling `print(fp.closed)` attribute -- which returns `True`.

This is because the file objects (`fp` in my example) returned by `open` function has two built-in methods `__enter__` and `__exit__`. It is also known as **context manager**. `__enter__` method is called at the start of `with` block and `__exit__` method is called at the end. Note: `with` statement only works with objects that support the **context mamangement protocol** i.e. they have `__enter__` and `__exit__` methods. A class which implement both methods is known as **context manager class**.

Now lets define our own context manager class.

```python
class Log:
    def __init__(self, filename):
        self.filename = filename
        self.fp = None

    def logging(self, text):
        line = text + "\r\n"
        self.fp.write(line)

    def __enter__(self):
        print("__enter__")
        self.fp = open(self.filename, "a+")
        return self

    def __exit__(self, exc_type, exc_value, exc_trace):
        print("__exit__")
        self.fp.close()

if __name__ == '__main__': 
    with Log("myfile.txt") as logfile:
        print("Hello World")
        logfile.logging("Test1")
        logfile.logging("Test2")
        print("Hello Python")
```

Output:

```txt
__enter__
Hello World
Hello Python
__exit__
```

I hope now you have basic understanding of both `__enter__` and `__exit__` magic methods.

## invocation order

In addition to the above answers to exemplify(举例说明) **invocation order**, a simple run example

```python
class myclass:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, type, value, traceback):
        print("__exit__")

    def __del__(self):
        print("__del__")

    def info(self):
        print("Know Thyself")

if __name__ == '__main__': 
    with myclass() as mc:
        mc.info()
```

Output:

```txt
__init__
__enter__
Know Thyself
__exit__
__del__
```









