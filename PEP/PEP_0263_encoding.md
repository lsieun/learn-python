# PEP 263 -- Defining Python Source Code Encodings

URL: https://www.python.org/dev/peps/pep-0263/

> 这个PEP是在Python 2.3的版本上提出的，不知道对于Python3是否依然有效呢？

This PEP proposes to introduce a syntax to declare **the encoding of a Python source file**. 

## Defining the Encoding

Python will default to ASCII as standard encoding if no other encoding hints are given.

To define a source code encoding, **a magic comment** must be placed into the source files either as **first** or **second** line in the file, such as:

```python
# coding=<encoding name>
```

or (using formats recognized by popular editors):

```python
#!/usr/bin/python
# -*- coding: <encoding name> -*-
```

or:

```python
#!/usr/bin/python
# vim: set fileencoding=<encoding name> :
```

This declaration is not needed in Python 3 as UTF-8 is the default source encoding (see PEP 3120).

https://www.python.org/dev/peps/pep-3120/

Do not forget to verify if your text editor encodes properly your code in utf-8. Otherwise, you may have invisible characters that are not interpreted as utf-8.

