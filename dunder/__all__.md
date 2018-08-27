# `__all__`

File: `foo.py`

```python
__all__ = ['bar', 'baz']

waz = 5
bar = 10
def baz():
    return 'baz'

```

These symbols can then be imported like so:

```python
from foo import *

print(bar)
print(baz)

# The following will trigger an exception, as "waz" is not exported by the module
print(waz)

```

If the `__all__` above is commented out, this code will then execute to completion, as the default behaviour of `import *` is to import all symbols that do not begin with an underscore, from the given namespace.

NOTE: `__all__` affects the `from <module> import *` behavior only. Members that are not mentioned in `__all__` are still accessible from outside the module and can be imported with `from <module> import <member>`.



