# configparser

## Modifying Settings

While `ConfigParser` is primarily intended to be configured by reading settings from files, settings can also be populated by calling `add_section()` to create **a new section**, and `set()` to add or change **an option**.

```python
import configparser

parser = configparser.SafeConfigParser()

parser.add_section("bug_tracker")
parser.set("bug_tracker", "url", "http://localhost:8080/bugs")
parser.set("bug_tracker", "username", "admin")
parser.set("bug_tracker", "password", "123456")

for section in parser.sections():
    print("Section: {}".format(section))
    for name, value in parser.items(section):
        print("\t{} = {}".format(name, value))

```

Output:

```txt
$ python configparser_populate.py 
Section: bug_tracker
	url = http://localhost:8080/bugs
	username = admin
	password = 123456
```

To remove **sections** and **options** from a `ConfigParser` , use `remove_section()` and `remove_option()` respectively.

```python
from configparser import ConfigParser

def show_config_info(parser):
    for section in parser.sections():
        print("Section: {}".format(section))
        for name, value in parser.items(section):
            print("\t{} = {}".format(name, value))

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read("multisection.ini")

    print("Read values:\n")
    show_config_info(parser)

    parser.remove_option("bug_tracker", "password")
    parser.remove_section("wiki")

    print("\nModified values:\n")
    show_config_info(parser)

```

Output:

```txt
$ python configparser_remove.py 

Read values:

Section: bug_tracker
	url = http://localhost:8080/bugs/
	username = test
	password = 123456
Section: wiki
	url = http://localhost:8080/wiki/
	username = wiki
	password = abcdef

Modified values:

Section: bug_tracker
	url = http://localhost:8080/bugs/
	username = test
```

## Saving Configuration Files

Once a `ConfigParser` is populated with the desired data, it can be saved to **a file** by calling the `write()` method. 

The `write()` method takes **a file-like object** as `argument`. It writes the data out in the INI format so it can be parsed again by the `ConfigParser` .

```python
import configparser
import sys

if __name__ == "__main__":
    parser = configparser.ConfigParser()

    parser.add_section("bug_tracker")
    parser.set("bug_tracker", "url", "http://localhost:8080/bugs")
    parser.set("bug_tracker", "username", "admin")
    parser.set("bug_tracker", "password", "123456")

    parser.write(sys.stdout)
    with open("myconfig.ini", "w") as f:
        parser.write(f)

```

