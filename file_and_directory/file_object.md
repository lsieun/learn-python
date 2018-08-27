# File Object

URL: http://www.bogotobogo.com/python/python_files.php

The `open()` function returns a **file object**, which has methods and attributes for getting information about and manipulating a stream of characters.

```python
>>> file = open('Alone.txt')
>>> file.mode
'r'
>>> file.name
'Alone.txt'
>>> file.encoding
'cp1252'
```

If we specify the encoding:

```python
>>> # -*- coding: utf-8 -*-
>>> file = open('Alone.txt', encoding='utf-8')
>>> file.encoding
'utf-8'
>>> str = file.read()
>>> str
'나 혼자 (Alone) - By Sistar\n추억이 이리 많을까 넌 대체 뭐할까\n아직 난 이래 혹시 돌아 올까 봐\n'
```

The first line was **encoding declaration** which needed to make the Python aware of Korean.

The `name` attribute reflects the name we passed in to the `open()` function when we opened the file. The `encoding` attribute reflects the encoding we passed in to the `open()` function. If we didn't specify the encoding when we opened the file, then the encoding attribute will reflect `locale.getpreferredencoding()`. The `mode` attribute tells us in which mode the file was opened. We can pass an optional `mode` parameter to the `open()` function. We didn't specify a `mode` when we opened this file, so Python defaults to '`r`', which means open for reading only, in text mode. The file mode serves several purposes; different modes let us **write** to a file, **append** to a file, or open a file in **binary** mode.

## Wrapping Up

file object API:

- `file.name`
- `file.mode`
- `file.encoding`