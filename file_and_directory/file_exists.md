# How to Check if a File Exists in Python

URL: https://dbader.org/blog/python-check-if-file-exists

### `os.path.exists()`

```python
>>> import os.path
>>> os.path.exists('mydirectory/myfile.txt')
True
>>> os.path.exists('does-not-exist.txt')
False
>>> os.path.exists('mydirectory')
True
```

As you just saw, calling `os.path.exists()` will return `True` for **files** and **directories**. If you want to ensure that a given path points to **a file** and **not to a directory**, you can use the `os.path.isfile()` function:

```python
>>> import os.path
>>> os.path.isfile('mydirectory/myfile.txt')
True
>>> os.path.isfile('does-not-exist.txt')
False
>>> os.path.isfile('mydirectory')
False
```

With both functions it’s important to keep in mind that they will only check if a file **exists**—and not if the program actually has **access** to it. If verifying access is important then you should consider simply opening the file while looking out for an I/O exception (IOError) to be raised.


## `pathlib.Path.exists()` (Python 3.4+)

```python
>>> import pathlib
>>> path = pathlib.Path('myfile.txt')
>>> path.exists()
True
>>> path.is_file()
True
```

The key difference is that `pathlib` provides a cleaner **object-oriented interface** for working with the file system. You’re no longer dealing with plain `str` objects representing file paths—but instead you’re handling `Path` objects with relevant methods and attributes on them.


## Summary: Checking if a File Exists in Python

**What’s the preferred way to check if a file exists using Python?**

In most cases where you need a file existence check I’d recommend you use the built-in `pathlib.Path.exists()` method on Python 3.4 and above, or the  `os.path.exists()` function on Python 2.









