# os の Examining the File System Contents

## `os.listdir()`

To prepare a `list` of the contents of a directory on the file system, use `os.listdir()`.

The return value is a list of all of the named members of the directory given. No distinction is made among **files**, **subdirectories**, and **symlinks**.

```python
import os
import sys

if __name__ == "__main__":
    dir_name = sys.argv[1]
    lst = os.listdir(dir_name)
    for item in lst:
        print(item)

```

## `os.walk()`

The function `walk()` traverses a directory recursively. For each subdirectory, it generates **a tuple** containing **the directory path**, **any immediate subdirectories of that path**, and **a list containing the names of any files in that directory**.

```python
import os
import sys

if __name__ == "__main__":
    # If we are not given a path to list, use /tmp
    if len(sys.argv) == 1:
        root = "/tmp"
    else:
        root = sys.argv[1]

    for dir_name, sub_dirs, files in os.walk(root):
        print(dir_name)
        # Make the subdirectory names stand out with /.
        sub_dirs = [n + "/" for n in sub_dirs]
        # Mix the directory contents together.
        sub_dirs.sort()
        files.sort()
        contents = sub_dirs + files
#        contents.sort()
        # Show the contents
        for c in contents:
            print("\t{}".format(c))
        print()

```

## `os.scandir()`

If more information is needed than the names of the files, it is likely to be more efficient to use `scandir()` than `listdir()`: More information is collected in one system call when the directory is scanned.

`scandir()` returns a sequence of `DirEntry` instances for the items in the directory. This object has several attributes and methods for accessing metadata about the file.

```python
import os
import sys

if __name__ == "__main__":
    dir_name = sys.argv[1]
    for entry in os.scandir(dir_name):
        if entry.is_dir():
            typ = "dir"
            pass
        elif entry.is_file():
            typ = "file"
            pass
        elif entry.is_symlink():
            typ = "link"
            pass
        else:
            typ = "unknown"
            pass
        print("{name:<15} {typ}".format(
            name=entry.name,
            typ=typ,
        ))

```


