# How to check if an object is a generator object in python?

URL: https://stackoverflow.com/questions/6416538/how-to-check-if-an-object-is-a-generator-object-in-python/6416571#6416571

You can use GeneratorType from types:

```python
>>> import types
>>> types.GeneratorType
<class 'generator'>
>>> gen = (i for i in range(10))    # generator expression
>>> gen
<generator object <genexpr> at 0x7f6c05b1fca8>
>>> isinstance(gen, types.GeneratorType)
True
>>> def foo():                      # generator function
...     for i in range(10):
...         yield i
... 
>>> gen = foo()
>>> gen
<generator object foo at 0x7f6c05b1fd00>
>>> isinstance(gen, types.GeneratorType)
True

```

Use `inspect` module `isgenerator` and `isgeneratorfunction`.

```python
>>> import inspect
>>> gen = (i for i in range(10))    # generator expression
>>> gen
<generator object <genexpr> at 0x7f6c0520d2b0>
>>> inspect.isgenerator(gen)
True
>>> inspect.isgeneratorfunction(gen)
False
>>> def foo():                      # generator function
...     for i in range(10):
...         yield i
... 
>>> gen = foo()
>>> inspect.isgenerator(gen)
True
>>> inspect.isgeneratorfunction(gen)
False
>>> inspect.isgeneratorfunction(foo)
True
```












