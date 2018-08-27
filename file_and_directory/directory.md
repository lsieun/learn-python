# Directories

URL: http://www.bogotobogo.com/python/python_files.php

The module called `os` contains functions to get information on local directories, files, processes, and environment variables.

## `os.getcwd()`

The **current working directory** is a property that Python holds in memory at all times.

```python
>>> import os
>>> print(os.getcwd())
C:\Python32
>>> os.chdir('/test')
>>> print(os.getcwd())
C:\test
```

We used the `os.getcwd()` function to get the current working directory. 

Then, we used the `os.chdir()` function to change the current working directory.


## `os.path.join()`

`os.path` contains functions for manipulating filenames and directory names.

```python
>>> import os
>>> print(os.path.join('/test/', 'myfile'))
/test/myfile
>>> print(os.path.expanduser('~'))
C:\Users\K
>>> print(os.path.join(os.path.expanduser('~'),'dir', 'subdir', 'k.py'))
C:\Users\K\dir\subdir\k.py
```

## `os.path.split()`

`os.path` also contains functions to split full pathnames, directory names, and filenames into their constituent parts.

```python
>>> pathname = "/Users/K/dir/subdir/k.py"
>>> os.path.split(pathname)
('/Users/K/dir/subdir', 'k.py')
>>> (dirname, filename) = os.path.split(pathname)
>>> dirname
'/Users/K/dir/subdir'
>>> pathname
'/Users/K/dir/subdir/k.py'
>>> filename
'k.py'
>>> (shortname, extension) = os.path.splitext(filename)
>>> shortname
'k'
>>> extension
'.py'
```

## `glob.glob()`

The `glob` module is another tool in the Python standard library. It's an easy way to get the contents of a directory programmatically, and it uses the sort of **wildcards** that we may already be familiar with from working on the command line.

```python
>>> import glob
>>> os.chdir('/test')
>>> import glob
>>> glob.glob('subdir/*.py')
['subdir\\tes3.py', 'subdir\\test1.py', 'subdir\\test2.py']
```

The `glob` module takes a wildcard and returns the path of all files and directories matching the wildcard.


## `os.path.realpath()` - Absolute pathname

The `glob.glob()` function returned a list of relative pathnames. If you want to construct an absolute pathname - i.e. one that includes all the directory names back to the root directory or drive letter - then we'll need the `os.path.realpath()` function.

```python
>>> import os
>>> print(os.getcwd())
C:\test\subdir
>>> print(os.path.realpath('test1.py'))
C:\test\subdir\test1.py
```

## `os.path.expandvars()` - Env. variable

The `expandvars` function inserts environment variables into a filename.

```python
>>> import os
>>> os.environ['SUBDIR'] = 'subdir'
>>> print(os.path.expandvars('/home/users/K/$SUBDIR'))
/home/users/K/subdir
```



