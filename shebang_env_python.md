# Why do people write the `#!/usr/bin/env python` shebang on the first line of a Python script?

URL: https://stackoverflow.com/questions/2429511/why-do-people-write-the-usr-bin-env-python-shebang-on-the-first-line-of-a-pyt


If you have several versions of Python installed, `/usr/bin/env` will ensure the interpreter used is the first one on your environment's `$PATH`. The alternative would be to hardcode something like `#!/usr/bin/python`; that's ok, but less flexible.

In Unix, **an executable file** that's meant to be interpreted can indicate what **interpreter** to use by having a `#!` at the start of the first line, followed by **the interpreter** (and any flags it may need).

If you're talking about other platforms, of course, this rule does not apply (but that "shebang line" does no harm, and will help if you ever copy that script to a platform with a Unix base, such as Linux, Mac, etc).

This applies when you run it in Unix by making it executable (`chmod +x myscript.py`) and then running it directly: `./myscript.py`, rather than just `python myscript.py`.

In computing, a **shebang** (also called a hashbang, hashpling, pound bang, or crunchbang) refers to the characters "`#!`" when they are the first two characters in an interpreter directive as the first line of a text file. In a Unix-like operating system, the program loader takes the presence of these **two characters** as **an indication** that **the file is a script**, and tries to execute **that script** using the **interpreter** specified by the rest of the first line in the file.

In order to run the python script, we need to tell the shell three things:

1. That the file is a script
2. Which interpreter we want to execute the script
3. The path of the interpreter

The shebang `#!` accomplishes (`1.`). The shebang begins with a `#` because the `#` character is a comment marker in many scripting languages. The contents of the shebang line are therefore automatically ignored by the interpreter.

The `env` command accomplishes (2.) and (3.). 

A common use of the `env` command is to launch interpreters, by making use of the fact that `env` will search `$PATH` for the command it is told to launch. Since the shebang line requires **an absolute path** to be specified, and since the location of various interpreters (perl, bash, python) may vary a lot, it is common to use:
```
#!/usr/bin/env perl
```
instead of trying to guess whether it is `/bin/perl`, `/usr/bin/perl`, `/usr/local/bin/perl`, `/usr/local/pkg/perl`, `/fileserver/usr/bin/perl`, or `/home/MrDaniel/usr/bin/perl` on the user's system...

On the other hand, `env` is almost always in `/usr/bin/env`. (Except in cases when it isn't; some systems might use `/bin/env`, but that's a fairly rare occassion and only happens on non-Linux systems.)

Correct usage for Python 3 scripts is:

```python
#!/usr/bin/env python3
```
This defaults to version `3.latest`. For Python 2.7.latest use `python2` in place of `python3`.

The following **should NOT be used** (except for the rare case that you are writing code which is compatible with both Python 2.x and 3.x):
```python
#!/usr/bin/env python
```
The reason for these recommendations, given in [PEP 394](https://www.python.org/dev/peps/pep-0394/#recommendation), is that `python` can refer either to `python2` or `python3` on different systems. It currently refers to `python2` on most distributions, but that is likely to change at some point.
















