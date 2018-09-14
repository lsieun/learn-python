# string module

## capwords

```python
import string

if __name__ == "__main__":
    s = "The quick brown fox jumped over the lazy dog"
    print(s)
    print(string.capwords(s))

```

```txt
The quick brown fox jumped over the lazy dog
The Quick Brown Fox Jumped Over The Lazy Dog
```


## Constants

The `string` module includes a number of constants related to ASCII and numerical character sets.

```python
import inspect
import string

def is_str(value):
    return isinstance(value, str)


if __name__ == "__main__":
    for name, value in inspect.getmembers(string, is_str):
        if name.startswith("_"):
            continue
        print("{} = {}".format(name, value))

```

Output:

```txt
ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
ascii_lowercase = abcdefghijklmnopqrstuvwxyz
ascii_uppercase = ABCDEFGHIJKLMNOPQRSTUVWXYZ
digits = 0123456789
hexdigits = 0123456789abcdefABCDEF
octdigits = 01234567
printable = 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
whitespace =
```








