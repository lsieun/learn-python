# File close

It's important to close files as soon as we're done with them because open files consume system resources, and depending on the file mode, other programs may not be able to access them.

```python
>>> file.close()
>>> file.read()
Traceback (most recent call last):
  File "", line 1, in 
    file.read()
ValueError: I/O operation on closed file.
>>> file.seek(0)
Traceback (most recent call last):
  File "", line 1, in 
    file.seek(0)
ValueError: I/O operation on closed file.
>>> file.tell()
Traceback (most recent call last):
  File "", line 1, in 
    file.tell()
ValueError: I/O operation on closed file.
>>> file.close()
>>> file.closed
True
```

1. We can't read from a closed file; that raises an `IOError` exception.

2. We can't **seek** in a closed file either.

3. There's no current position in a closed file, so the `tell()` method also fails.

4. Calling the `close()` method on a stream object whose file has been closed does not raise an exception. It's just a **no-op**.

5. Closed stream objects do have one useful attribute: the `closed` attribute will confirm that the file is closed.














