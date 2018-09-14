# readline: The GNU readline Library

The `readline` module provides an interface to **the GNU readline library**. It can be used to enhance **interactive command-line programs** to make them easier to use—for example, by adding command-line text completion, or “tab completion.”

> 这段的三个意思：
> （1）Python的readline module是对GNU readline library的一个API接口  
> （2）Python的readline module的作用是让程序更容易使用  
> （3）它的一个显著功能就是tab completion

The GNU libraries needed for `readline` are not available on all platforms by default. If your system does not include them, you may need to recompile the Python interpreter to enable the module, after installing the dependencies. A stand-alone version of the library is also distributed from the Python Package Index under the name `gnureadline` . The examples in this section first try to import `gnureadline` , and then fall back to `readline` .

> 这里讲述了readline的两个版本：  
> （1）readline  
> （2）gnureadline

## Configuring readline

There are two ways to configure the underlying `readline` library: by using **a configuration file** or by using the `parse_and_bind()` function. 

> 这里介绍了配置readline的两种方式：  
> （1）通过配置文件  
> （2）通过parse_and_bind()方法

**Configuration options** include the key-binding to invoke **completion**, **editing modes** (`vi` or `emacs`), and many other values. Refer to the documentation for the GNU readline library for details.

> 具体的配置选项，这里列举了两个：  
> （1）tab completion  
> （2）使用vi或emacs模式编辑  

The easiest way to enable tab completion is through a call to `parse_and_bind()`. Other options can be set at the same time. This example changes the editing controls to use `vi` mode instead of the default of emacs . To edit the current input line, press `ESC` and then use the normal `vi` navigation keys, such as `j` , `k` , `l` , and `h`.

> 这里先介绍parse_and_bind()的方式进行readline配置

```python
try:
    import gnureadline as readline
except ImportError:
    import readline

readline.parse_and_bind("tab: complete")         # 配置tab completion
readline.parse_and_bind("set editing-mode vi")   # 配置vi 编辑模式

while True:
    line = input('Prompt ("stop" to quit):')
    if line == "stop":
        break
    print("ENTERED: {!r}".format(line))

```

The same configuration can be stored as instructions in **a file** read by the library with a single call. If `myreadline.rc` contains.

> 这是第二种配置方式，通过文件进行配置。

```txt
# Turn on tab completion.
tab: complete
# Use vi editing mode instead of emacs.
set editing-mode vi
```

```python
try:
    import gnureadline as readline
except ImportError:
    import readline

readline.read_init_file("myreadline.rc")


while True:
    line = input('Prompt ("stop" to quit):')
    if line == "stop":
        break
    print("ENTERED: {!r}".format(line))

```

## Completing Text

The next program has a built-in set of possible commands and uses `tab completion` when the user is entering instructions.

> 下面的例子是通过tab键实现代码补全功能。
> 目前，我还不是特别理解下面的代码。

```python
try:
    import gnureadline as readline
except ImportError:
    import readline

import logging

LOG_FILENAME = "tmp/completer.log"
logging.basicConfig(
    format="%(message)s",
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

class SimpleCompleter:
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text
            # so build a match list
            if text:
                self.matches = [
                    s
                    for s in self.options
                    if s and s.startswith(text)
                ]
                logging.debug("%s matches: %s", repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug("(empty input) matches: %s", self.matches)

        # Return the state'th item from the match list,
        # if that many items are present
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug("complete(%s, %s) => %s", repr(text), state, repr(response))
        return response

def input_loop():
    line = ""
    while line != "stop":
        line = input('Prompt ("stop" to quit):')
        print("Dispatch {}".format(line))

# Register the completer function
OPTIONS = ["start", "stop", "list", "print"]
readline.set_completer(SimpleCompleter(OPTIONS).complete)

# Use the tab key for completion
readline.parse_and_bind("tab: complete")

# Prompt the user for text
input_loop()

```

The `SimpleCompleter` class keeps a list of “options” that are candidates for autocompletion. The `complete()` method for an instance is designed to be registered with `readline` as **the source of completions**. The arguments are a `text` string to complete and a `state` value that indicates how many times the function has been called with the same text. The function is called repeatedly, with the `state` being incremented upon each call. It should return a string if there is a candidate for that `state` value or `None` if there are no more candidates. The implementation of `complete()` in the previous listing looks for a set of matches when state is `0` , and then returns all of the candidate matches one at a time on subsequent calls.

