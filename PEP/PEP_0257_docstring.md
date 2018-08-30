# PEP 257 -- Docstring Conventions

URL: https://www.python.org/dev/peps/pep-0257/

## What is a Docstring?

A `docstring` is **a string literal** that occurs as the first statement in a `module`, `function`, `class`, or `method` definition. Such a docstring becomes the `__doc__` special attribute of that object.

For consistency, always use `"""triple double quotes"""` around docstrings. Use `r"""raw triple double quotes"""` if you use any backslashes in your docstrings. For Unicode docstrings, use `u"""Unicode triple-quoted strings"""`.

## One-line Docstrings

```python
def function(a, b):
    """Do X and return a list."""
```

## Multi-line Docstrings

Multi-line docstrings consist of 
- **a summary line** just like a one-line docstring, followed by 
- **a blank line**, followed by 
- **a more elaborate description**. 

不同类型的Docstring

- `class`: Insert **a blank line** after all docstrings (one-line or multi-line) that document a class -- generally speaking, the class's methods are separated from each other by a single blank line, and the docstring needs to be offset from the first method by a blank line. 
- `class`: The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its `__init__` method. Individual methods should be documented by their own docstring.
- `module`: The docstring for a module should generally list the classes, exceptions and functions (and any other objects) that are exported by the module, with a one-line summary of each. 
- `function` or `method`: The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.


