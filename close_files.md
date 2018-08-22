# Why should I close files in Python? 

URL： https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python

从五个角度来理解不关闭文件造成的影响：

- 第一个角度：Code，良好的编程习惯
- 第二个角度：Python implementation，如果在Code层面不关闭file handle，那么Python implementation是否能够帮助关闭文件呢？
- 第三个角度：Disk，从磁盘的角度来查看File内容
- 第四个角度：Memory，从内存的角度来看性能
- 第五个层面：OS， 从系统的角度来看对操作文件的约束

For the most part, not closing files is a bad idea, for the following reasons:

## 第1个角度：Code

It is sloppy programming.

> Moral: Clean up after yourself. :)

## 第2个角度：Python implementation

It is a matter of good programming practice. 

> 还是回归第一条，关闭文件，本质上是个编程好习惯的问题。

If you don't close them yourself, some Pythons will close files automatically when they are no longer referenced, while others will not and it's up to the O/S to close files when the Python interpreter exits.

Even for the Pythons that will close files for you, the timing is not guaranteed: it could be immediately, or it could be seconds/minutes/hours/days later.

In some versions of Python, that might be the instant they are no longer being used; in others, it might not happen for a long time. Under some circumstances, it might not happen at all.

It puts your program in the garbage collectors hands - though the file in theory will be auto closed, it may not be closed. Python 3 and Cpython generally do a pretty good job at garbage collecting, but not always, and other variants generally suck at it.

> 原本的情况下，关闭文件应该是由你来做的事情；如果你不做，那关闭文件的事情只能交给garbage collector之手了，由它来做。对于Python3和CPython来说，它们对于garbage collecting的工作做的很好。但对于其它的variants就不一定能做的那么好了。

In current versions of CPython the file will be closed because CPython uses **reference counting** as its primary garbage collection mechanism but **that's an implementation detail, not a feature of the language**. Other implementations of Python aren't guaranteed to work this way. For example IronPython, PyPy, and Jython don't use reference counting and therefore won't close the file.

It's bad practice to rely on CPython's garbage collection implementation because it makes your code less portable. You might not have resource leaks if you use CPython, but if you ever switch to a Python implementation which doesn't use reference counting you'll need to go through all your code and make sure all your files are closed properly.

## 第3个角度：Disk

When writing to a file, the data may not be written to disk until the file is closed. When you say "`output.write(...)`", the data is often cached in memory and doesn't hit the hard drive until the file is closed. The longer you keep the file open, the greater the chance that you will lose data.

For the most part, many changes to files in python do not go into effect until after the file is closed, so if your script edits, leaves open, and reads a file, it won't see the edits.

> 写入数据，但文件不关闭，打开文件时，无法看到文件的变化。

## 第4个角度：Memory

It can slow down your program. Too many things open, and thus more used space in the RAM, will impact performance.

## 第5个角度：OS

Since your operating system has strict limits on how many file handles can be kept open at any one instant, it is best to get into the habit of closing them when they aren't needed and not wait for "maid service" to clean up after you.

Also, some operating systems (Windows, in particular) treat open files as locked and private. While you have a file open, no other program can also open it, even just to read the data. This spoils backup programs, anti-virus scanners, etc.

There are limits on the number of files you can have open - typically something like 512-4096. If you neglect to close your files you'll eventually get to the point where you cannot open new file descriptors (files, sockets, etc) You can easily get into this type of situation if you're crawling a directory of files and operating on each one. However, in most cases once a file descriptor object is out of scope it'll automatically be closed. However, depending on that behavior is sloppy.


