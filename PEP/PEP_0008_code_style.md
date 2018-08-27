# PEP 8 -- Style Guide for Python Code

URL: https://www.python.org/dev/peps/pep-0008/

- Code Layout
    - Indentation
    - Maximum Line Length
    - Should a Line Break Before or After a Binary Operator?
    - Blank Lines
    - Source File Encoding
    - Imports
    - Module Level Dunder Names: `__author__`,` __version__`
- String Quotes
- Whitespace in Expressions and Statements
- When to Use Trailing Commas
- Comments
    - Block Comments
    - Inline Comments
    - Documentation Strings https://www.python.org/dev/peps/pep-0257/
- Naming Conventions
- Programming Recommendations


isinstance(obj, int)



### Blank Lines

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Use blank lines in functions, sparingly, to indicate logical sections.


### Function and Method Arguments

Always use `self` for the first argument to instance methods.

Always use `cls` for the first argument to class methods.

## Programming Recommendations

Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).

Comparisons to singletons like `None` should always be done with `is` or `is not`, never the equality operators.

When implementing ordering operations with rich comparisons, it is best to implement all six operations (`__eq__`, `__ne__`, `__lt_`_, `__le__`, `__gt__`, `__ge__`) rather than relying on other code to only exercise a particular comparison.

Use string methods instead of the string module. String methods are always much faster and share the same API with unicode strings. 

Use `''.startswith()` and `''.endswith()` instead of `string slicing` to check for prefixes or suffixes.

Object type comparisons should always use `isinstance()` instead of comparing types directly.

Yes: `if isinstance(obj, int):`

No:  `if type(obj) is type(1):`







