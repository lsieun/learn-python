# sys の Runtime Environment

`sys` provides **low-level APIs** for interacting with **the system** outside of an application, by accepting **command-line arguments**, **accessing user input**, and passing messages and status values to the user.

> sys是Python application与OS进行交互的low-level API。  

## 1、Command-Line Argument：程序运行之前，OS为program提供的输入参数

**The arguments** captured by **the interpreter** are processed there; they are not passed to **the program being run**. **Any remaining options and arguments**, including **the name of the script itself**, are saved to `sys.argv` in case the program does need to use them.

> 这段的有三个意思：  
> （1）`python sys_argv.py`，其中的arguments会被Python Interpreter收到；  
> （2）但是，Python Interpreter并不会把这些arguments主动传给当前运行的程序；  
> （3）在当前程序中，如果想获得这些arguments，可以通过调用sys.argv来获取到。

```python
import sys

if __name__ == "__main__":
    print("Arguments:", sys.argv)

```

In the third example shown here, the `-u` option is understood by **the interpreter**; it is not passed to the program being run.

```txt
$ python sys_argv.py 
Arguments: ['sys_argv.py']

$ python sys_argv.py -v foo bar
Arguments: ['sys_argv.py', '-v', 'foo', 'bar']

$ python -u sys_argv.py 
Arguments: ['sys_argv.py']
```

## 2、Input and Output Streams：程序运行过程中，OS与program之间的数据双向流动

Following the Unix paradigm, Python programs can access **three file descriptors** by default.

```python
import sys

if __name__ == "__main__":
    print("STATUS: Reading from stdin", file=sys.stderr)

    data = sys.stdin.read()

    print("STATUS: Writing data to stdout", file=sys.stderr)

    sys.stdout.write(data)
    sys.stdout.flush()

    print("STATUS: Done", file=sys.stderr)

```

- `stdin` is **the standard way to read input**, usually from a console but also from other programs via a pipeline. 
- `stdout` is **the standard way to write output** for a user (to the console) or to be sent to the next program in a pipeline. 
- `stderr` is intended for use with **warning or error messages**.

Output:

```txt
$ echo "Hello World!" | python sys_stdio.py 

STATUS: Reading from stdin
STATUS: Writing data to stdout
Hello World!
STATUS: Done
```

## 3、Returning Status：程序运行结束后，program向OS返回自己运行的终止状态

To return **an exit code** from a program, pass **an integer value** to `sys.exit()`.

**A nonzero value** means the program exited with **an error**.

```python
import sys

if __name__ == "__main__":
    exit_code = int(sys.argv[1])
    sys.exit(exit_code)

```

Output:

```txt
$ python sys_exit.py 0 ; echo "Exited $?"

Exited 0

$ python sys_exit.py 1 ; echo "Exited $?"

Exited 1
```


