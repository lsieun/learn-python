# Opening Files

URL: http://www.bogotobogo.com/python/python_files.php

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

To open a file, we use built-in `open()` function:

```python
myfile = open('mydir/myfile.txt', 'w')
```

The `open()` function takes a `filename` as an argument. Here the filename is `mydir/myfile.txt`, and the next argument is a processing `mode`. The `mode` is usually the string '`r`' to open text input (this is the default mode), '`w`' to create and open open for text output. The string '`a`' is to open for appending text to the end. The mode argument can specify additional options: adding a '`b`' to the mode string allows for binary data, and adding a `+` opens the file for both input and output.












