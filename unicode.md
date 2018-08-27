# How is unicode represented internally in Python?

URL: https://www.python.org/dev/peps/pep-0393/
URL: https://stackoverflow.com/questions/26079392/how-is-unicode-represented-internally-in-python

I'm assuming you want to know about **CPython**, the standard implementation. Python 2 and Python 3.0-3.2 use either UCS2 or UCS4 for Unicode characters, meaning it'll either use 2 bytes or 4 bytes for each character. Which one is picked is a compile-time option.

`\u2049` is then represented as either `\x49\x20` or `\x20\x49` or `\x49\x20\x00\x00` or `\x00\x00\x20\x49` depending on the native byte order of your system and if UCS2 or UCS4 was picked. ASCII characters in a unicode string still use 2 or 4 bytes per character too.

**Python 3.3** switched to a new internal representation, using the most compact form needed to represent all characters in a string. Either 1 byte, 2 bytes or 4 bytes are picked. ASCII and Latin-1 text uses just 1 byte per character, the rest of the BMP characters require 2 bytes and after that 4 bytes is used.

To know whether you have a "narrow" (UCS2) or "wide" (UCS4) build, examine `sys.maxunicode`. `65535` means narrow, `1114111` means wide.

```python
import sys
print(sys.maxunicode)
```

There has been NO CHANGE in Unicode internal representation between Python 2.X and 3.X.

It's definitely NOT UTF-16. **UTF-anything is a byte-oriented EXTERNAL representation**.

Each code unit (character, surrogate, etc) has been assigned a number from range(0, 2 ** 21). This is called its "ordinal".



