# configparser

## `Option` Search Path

`ConfigParser` uses a multistep search process when looking for an option.

- (1) If the `option` name appears in the `vars` dictionary passed to `get()`, the value from `vars` is returned.
- (2) If the `option` name appears in **the specified section**, the value from that section is returned.
- (3) If the `option` name appears in the `DEFAULT` section, that value is returned.
- (4) If the `option` name appears in the `defaults` dictionary passed to the constructor, that value is returned.
- (5) If the name is not found in any of those locations, `NoOptionError` is raised.



```txt
[DEFAULT]    # 第3优先级
username = tester
password = 123456

[sect]       # 第2优先级
username = admin
password = abcdef

parser = configparser.ConfigParser(defaults=DEFAULTS)    # 第4优先级 defaults参数
parser.read("with-defaults.ini")                         # 第2和第3优先级
value = parser.get("sect", name, vars=vars)              # 第1优先级 var参数
```

下面的代码只是为了展示各种配置的优先级顺序；如果明白了优先级顺序，代码实在不用细看。

```txt
[DEFAULT]
file-only = value from DEFAULT section
init-and-file = value from DEFAULT section
from-section = value from DEFAULT section
from-vars = value from DEFAULT section

[sect]
section-only = value from section in file
from-section = value from section in file
from-vars = value from section in file
```

```python
import configparser

# Define the names of the options
option_names = [
    "from-default",
    "from-section",
    "section-only",
    "file-only",
    "init-only",
    "init-and-file",
    "from-vars",
]

# Initialize the parser with some defaults.
DEFAULTS = {
    "from-default": "value from defaults passed to init",
    "init-only": "value from defaults passed to init",
    "init-and-file": "value from defaults passed to init",
    "from-section": "value from defaults passed to init",
    "from-vars": "value from defaults passed to init",
}

def show_option_info(parser):
    defaults = parser.defaults()
    for name in option_names:
        if name in defaults:
            print("\t{:<15} = {!r}".format(name, defaults[name]))
    print("="*66)

def main():
    parser = configparser.ConfigParser(defaults=DEFAULTS)

    print("Defaults before loading file:")
    show_option_info(parser)

    # Load the configuration file
    parser.read("with-defaults.ini")

    print("Defaults after loading file:")
    show_option_info(parser)

    # Define some local overrides.
    vars = {"from-vars": "value from vars"}

    # Show the values of all the options
    print("Option loopup:")
    for name in option_names:
        value = parser.get("sect", name, vars=vars)
        print("\t{:<15} = {!r}".format(name, value))
    print("="*66)

    # Show error message for options that do not exist.
    print("Error cases:")
    try:
        print("No such option:", parser.get("sect", "no-option"))
    except configparser.NoOptionError as err:
        print(err)

    try:
        print("No such section:", parser.get("no-sect", "no-option"))
    except configparser.NoSectionError as err:
        print(err)


if __name__ == "__main__":
    main()

```

Output:

```txt
$ python configparser_defaults.py 
Defaults before loading file:
	from-default    = 'value from defaults passed to init'
	from-section    = 'value from defaults passed to init'
	init-only       = 'value from defaults passed to init'
	init-and-file   = 'value from defaults passed to init'
	from-vars       = 'value from defaults passed to init'
==================================================================
Defaults after loading file:
	from-default    = 'value from defaults passed to init'
	from-section    = 'value from DEFAULT section'
	file-only       = 'value from DEFAULT section'
	init-only       = 'value from defaults passed to init'
	init-and-file   = 'value from DEFAULT section'
	from-vars       = 'value from DEFAULT section'
==================================================================
Option loopup:
	from-default    = 'value from defaults passed to init'
	from-section    = 'value from section in file'
	section-only    = 'value from section in file'
	file-only       = 'value from DEFAULT section'
	init-only       = 'value from defaults passed to init'
	init-and-file   = 'value from DEFAULT section'
	from-vars       = 'value from vars'
==================================================================
Error cases:
No option 'no-option' in section: 'sect'
No section: 'no-sect'
```
