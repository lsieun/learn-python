# What’s New In Python 3.0

URL: https://docs.python.org/3/whatsnew/3.0.html

## Print Is A Function

```python
Old: print "The answer is", 2*2
New: print("The answer is", 2*2)

Old: print x,           # Trailing comma suppresses newline
New: print(x, end=" ")  # Appends a space instead of a newline

Old: print              # Prints a newline
New: print()            # You must call the function!

Old: print >>sys.stderr, "fatal error"
New: print("fatal error", file=sys.stderr)

Old: print (x, y)       # prints repr((x, y))
New: print((x, y))      # Not the same as print(x, y)!
```

## A New Approach To String Formatting

A new system for built-in string formatting operations replaces the `%` string formatting operator. (However, the `%` operator is still supported; **it will be deprecated in Python 3.1 and removed from the language at some later time.**) Read PEP 3101 for the full scoop. https://www.python.org/dev/peps/pep-3101