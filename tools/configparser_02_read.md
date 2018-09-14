# configparser

## Reading Configuration Files

Use the `read()` method of `ConfigParser` to read the configuration file.

```txt
# This is a simple example with comments.
[bug_tracker]
url = http://localhost:8080/bugs/
username = admin
; You should not store passwords in plain text
; configuration files.
password = SECRET
```

```python
from configparser import ConfigParser

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read("simple.ini")

    print(parser.get("bug_tracker", "url"))

```

Output:

```txt
$ python configparser_read.py

http://localhost:8080/bugs/
```

## Unicode Configuration Data

**Configuration files** containing **Unicode data** should be read using the proper encoding value. The following example file changes the `password` value of the original input to contain Unicode characters and is encoded using `UTF-8`.

```txt
[bug_tracker]
url = http://localhost:8080/bugs/
username = admin
password = 没有密码
```

The file is opened with the appropriate decoder, converting the UTF-8 data to native Unicode strings.

```python
from configparser import ConfigParser

if __name__ == "__main__":
    parser = ConfigParser()
    # Open the file with the corrent encoding
    parser.read("unicode.ini", encoding="utf-8")

    password = parser.get("bug_tracker", "password")

    print("Password:", password)
    print("Password:", password.encode("utf-8"))
    print("Type    :", type(password))
    print("repr()  :", repr(password))

```

The value returned by `get()` is a Unicode string. To print it safely, the string must be re-encoded as UTF-8.

```txt
$ python configparser_unicode.py 

Password: 没有密码
Password: b'\xe6\xb2\xa1\xe6\x9c\x89\xe5\xaf\x86\xe7\xa0\x81'
Type    : <class 'str'>
repr()  : '没有密码'
```

## Accessing Configuration Settings

`ConfigParser` includes methods for examining the structure of the parsed configuration, including listing the `sections` and `options`, and getting their values. The following configuration file includes two `sections` for separate web services.

```txt
[bug_tracker]
url = http://localhost:8080/bugs/
username = test
password = 123456

[wiki]
url = http://localhost:8080/wiki/
username = wiki
password = abcdef
```

The next sample program exercises some of the methods for looking at the configuration data, including `sections()` , `options()` , and `items()` .

Both `sections()` and `options()` return **lists of strings**, while `items()` returns **a list of tuples** containing the name–value pairs.

```python
from configparser import ConfigParser

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read("multisection.ini")

    for section_name in parser.sections():
        print("Section: ", section_name)
        print("\tOptions:", parser.options(section_name))
        for name, value in parser.items(section_name):
            print("\t{} = {}".format(name, value))
        print()

```

Output:

```txt
$ python configparser_structure.py

Section:  bug_tracker
	Options: ['url', 'username', 'password']
	url = http://localhost:8080/bugs/
	username = test
	password = 123456

Section:  wiki
	Options: ['url', 'username', 'password']
	url = http://localhost:8080/wiki/
	username = wiki
	password = abcdef
```
