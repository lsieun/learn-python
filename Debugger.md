# Python Debugger

参考URL： https://pymotw.com/3/pdb/

## 1、What is PDB?

`pdb` implements an interactive debugging environment for Python programs.

> pdb是一个交互式调试环境 for Python programs。

它能做什么：

- variable: 可以**查看**variable的value，可以**修改**variable的value
- execution: watch program execution step-by-step

## 2、如何学习PDB?

PDB是一个对Python程序进行交互式的调试环境（an interactive debugging environment）。所谓“交互式”，就是：你输入一个**命令**，它（PDB）对你的命令进行响应（echo）。

这就涉及到：

- （1）如何启动PDB（有4种方法）
- （2）如何使用PDB（即，使用**命令**与PDB交互，每个命令能达到什么效果）


## 3、如何启动PDB

### 3.1、启动PDB的四种方式：

- Script mode
- Postmortem mode
- Run mode
- **Trace mode** (最重要))

### 3.2、前三种Mode

Script Mode

```
python -m pdb buggy.py
```

Postmortem Mode

```
pdb.pm()
```

Run Mode

```
pdb.run('some.expression()')
```

### 3.3、Trace Mode

```
pdb.set_trace()
```

Convenient to stick in development and test code. 这种方式使用起来很方便。


```python
def divide_one_by(divisor):
    import pdb; pdb.set_trace()
    return 1 / divisor

if __name__ == '__main__':
        divide_one_by(0)
```


## 4、如何使用PDB？

如何使用PDB的本质在于使用“命令”。

使用“命令”，分两个步骤学习：

- （1）What： 有哪些命令可以使用
- （2）How：  如何使用命令

### 4.1、有哪些命令

一个简洁命令清单

| Command   | Description                                  |
| --------- | -------------------------------------------- |
| `n`       | execute next line                            |
| `c`       | complete execution                           |
| `l`       | list 3 lines before and after current line   |
| `s`       | step into function call                      |
| `b`       | show list of all break points                |
| `b[int]`  | set break point at line number(eg. `b10`)    |
| `b[func]` | break at function name                       |
| `cl`      | clear all break points                       |
| `cl[int]` | clear break point at line number(eg. `cl10`) |
| `p`       | print                                        |


查看PDB命令的help文档

在Python Debugger中，输入`h`或`help`，查看pdb的帮助

```
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

```

再通过`help <topic>`查看特定命令的帮助，例如：

```
(Pdb) h c
c(ont(inue))
        Continue execution, only stop when a breakpoint is encountered.
```

## 4.2、如何使用命令

The interface for the debugger is **a small command language** that lets you 

- move around the call stack, 
- examine and change the values of variables, and 
- control how the debugger executes the program. 

The interactive debugger uses `readline` to accept commands, and supports **tab completion** for **commands**, **filenames**, and **function names**. **Entering a blank line re-runs the previous command again**, unless it was a `list` operation.

### Navigating the Execution Stack (Where Am I?)

- `where`(w): showing the current location in the frame stack.
- `list`(l): displaying code in your current execution context. 显示11行内容
- `list <line_no>`: lines around that `<line_no>` line
- `list <first>, <last>`: the first and last lines to include in its output.
- `longlist`(ll): prints the source for the current function or frame
- `source`:  loads and prints the full source for an arbitrary class, function, or module.
- `up`(u): moves towards older frames on the stack. 
- `down`(d): moves towards newer frames.

Where Am I?

- `where`(w): showing the current location in the frame stack.
- `list`(l): displaying code in your current execution context. 显示11行内容

Frame Stack Control

`up`, `down`: navigating the frame statck

### Examining Variables on the Stack (Displaying things)

- `args` or `a`: print values of current function's argument
- `p`: evaluates an expression given as argument and prints the result
- `pp`: pretty print

Similarly, prefixing an expression with `!` passes it to the Python interpreter to be evaluated. This feature can be used to execute arbitrary Python statements, including **modifying variables**. 

Modifying Variables

`!`-prefix: pass directly to interpreter, used often to modify variable

```
!divisor=1
```

### Stepping Through a Program (Execution Control)

- `step` (s): execute the current line and then stop at the next execution point – either the first statement inside a function being called or the next line of the current function.
- `next`(n): like `step`, but does not enter functions called from the statement being executed. 
- `until`: commlike `next`, except it explicitly continues until execution reaches a line in the same function with a line number higher than the current value. 
- `until <line_no>`: To let execution run until a specific line. It is most useful for navigating within a function for skipping over long blocks.
- `return`: It continues executing until the function is about to execute a return statement, and then it pauses, providing time to look at the return value before the function returns.
step, next, continue, until, return



### Breakpoints

- `break`(b): setting break points, including the line number, file, and function where processing should pause.
- `break <lineno>`: To set a breakpoint on a specific line of the current file
- `break <func_name>`: Breakpoints can also be set to the first line of a function by specifying the function name
- `break <file_name.py>:<line_no>`: To specify a breakpoint in another file
- `break`: To list the breakpoints currently set, use `break` without any arguments. 
- `continue`(c): tells the debugger to keep running the program until the next breakpoint

### Managing Breakpoints

- `disable <break_id>`: turn off a breakpoint
- `enable <break_id>`: turn on a breakpoint
- `clear <break_id>`: delete a breakpoint entirely.
- `clear`: delete all breakpoints
- `tbreak <line_no>`: **A temporary breakpoint** is automatically cleared the first time program execution hits it. 

