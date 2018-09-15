# sys の Interpreter

## Interpreter Version and Implementation

```python
>>> import sys
>>> sys.version # Python Interpreter版本 和 编译器GCC版本 编译日期
'3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) \n[GCC 7.2.0]'

>>> sys.platform # The operating system platform used to build the interpreter
'linux'

>>> sys.implementation.name # Interpreter Implementation
'cpython'
>>> sys.implementation.version
sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
>>> sys.implementation.cache_tag
'cpython-36'
```

# Encoding of Interpreter and OS

To get **the name of the default Unicode encoding** that **the interpreter** is using, call `getdefaultencoding()`. This value is set during start-up, and cannot be changed during a session. 这里是Python Interpreter使用的Unicode encoding。

The **interpreter encoding default** and **the file system encoding** may be different for some operating systems, so there is a separate way to retrieve the file system setting. `getfilesystemencoding()` returns **an OS-specific value**.

```python
>>> sys.getdefaultencoding()
'utf-8'
>>> sys.getfilesystemencoding()
'utf-8'
```

## Install Location

The path to the actual interpreter program is available in `sys.executable` on all systems for which having a path to the interpreter makes sense.

`sys.prefix` refers to the parent directory of the interpreter installation. It usually
includes `bin` and `lib` directories for executables and installed modules, respectively.

```python
>>> sys.executable
'/home/john/Software/anaconda3/bin/python'
>>> sys.prefix
'/home/john/Software/anaconda3'
```

