# argparse

URL: https://www.pythonforbeginners.com/argparse/argparse-tutorial
URL: https://pymotw.com/3/argparse/

## What: What is it?

The argparse module includes tools for building command line argument and option processors. 

And `argparse` will figure out how to parse those out of `sys.argv`. 

> `argparse`是对`sys.argv`的进一步封装

The `argparse` module also automatically generates **help** and **usage** messages and
issues errors when users give the program invalid arguments.

> `argparse`能够自动生成help和usage文档。

## Why: Why use it?

The `argparse` module makes it easy to write user-friendly command-line interfaces. 

## Use Step

The first step when using `argparse` is to **create a parser object** and tell it what arguments to expect. The parser can then be used to process the command-line arguments when the program runs.

### Setting Up a Parser

The constructor for the parser class (`ArgumentParser`) takes several arguments to set up the `description` used in the help text for the program and other global behaviors or settings.

```python
import argparse
parser = argparse.ArgumentParser(
    description='This is a sample program',
)
```

### Defining Arguments

argparse is a complete argument processing library. Arguments can trigger different **actions**, specified by the `action` argument to `add_argument()`. Supported actions include storing the argument, storing a constant value, counting the number of times an argument is seen, and calling a callback to use custom processing instructions.

The default `action` is to **store the argument value**. If a `type` is provided, the value is converted to that type before it is stored. If the `dest` argument is provided, the value is saved using that name when the command-line arguments are parsed.

### Parsing a Command-Line

After all of the arguments are defined, parse the command-line by passing a sequence of argument strings to `parse_args()`. By default, the arguments are taken from `sys.argv[1:]`, but any list of strings can be used. The options are processed using the GNU/POSIX syntax, so option and argument values can be mixed in the sequence.

The return value from `parse_args()` is a `Namespace` containing the arguments to the command. The object holds the argument values as attributes, so if the argument’s `dest` is set to "`myoption`", the value is accessible as `args.myoption`.

## Concept

When you run the "`ls`" command without any options, it will default displaying the
contents of the current directory.

> 这段讲出一个知识点：默认值 defalut value

If you run "`ls`" on a different directory that you currently are in, you would type
"`ls directory_name`". The "`directory_name`" is a "**positional argument**", which means that the program know what to do with the value. 

> 这段讲出一个知识点：positional argument

To get more information about a file we can use the "`-l`" switch. The "`-l`" is knowns as an "**optional argument**"

> 这段讲出一个知识点：optional argument

If you want to display the help text of the `ls` command, you would type "`ls --help`"

> 这段讲出一个知识点：查看帮助

## arguments
- arguments name
    - positional arguments (required)
    - optional arguments
        - short option: `-v`
        - long option: `--verbose`
- help
- type
- action
    - store
    - store_true: if the option is specifed, then assign the value "True" to the argument
- default
- dest

### Argument Actions
Any of six built-in actions can be triggered when an argument is encountered.

- `store`: Save the value, after optionally converting it to a different type. This is **the default action** taken if none is specified explicitly.
- `store_const`: Save a value defined as part of the argument specification, rather than a value that comes from the arguments being parsed. This is typically used to implement command-line flags that are not Booleans.
- `store_true` / `store_false`: Save the appropriate Boolean value. These actions are used to implement Boolean switches.
- `append`: Save the value to a list. Multiple values are saved if the argument is repeated.
- `append_const`: Save a value defined in the argument specification to a list.
- `version`: Prints version details about the program and then exits.

## Demo

```python
import argparse

# Setting Up a Parser
parser = argparse.ArgumentParser(
    description="This a sample program"
)

# Defining Arguments
parser.add_argument(
    "uid", 
    action="store", 
    type=int,
    help="please input user id"
)
parser.add_argument(
    "-u", 
    "--username", 
    action="store",
    help="please input username"
)
parser.add_argument(
    "-p", 
    "--password", 
    action="store", 
    type=str, 
    default="123456",
    help="please input password"
)
parser.add_argument(
    "--married", 
    action="store_true", 
    default=False,
    help="please input whether you're married"
)
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s 1.0"
)

# Parsing a Command-Line
args = parser.parse_args()
print("args = {!r}".format(args))

uid = args.uid
username = args.username
password = args.password
married = args.married
print("uid = {!r}".format(uid))
print("username = {!r}".format(username))
print("password = {!r}".format(password))
print("married = {!r}".format(married))

```

Output:

```bash
$ python test.py 111 -u="tom" -p="abc"
args = Namespace(married=False, password='abc', uid=111, username='tom')
uid = 111
username = 'tom'
password = 'abc'
married = False

$ python test.py 111 -u="tom" --married
args = Namespace(married=True, password='123456', uid=111, username='tom')
uid = 111
username = 'tom'
password = '123456'
married = True

```

