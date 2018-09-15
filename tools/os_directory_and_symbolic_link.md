# os の Directory and Symbolic Links

## Creating and Deleting Directories

Several functions are available for working with **directories** on the file system, including functions for **creating directories**, **listing their contents**, and **removing directories**.

Two sets of functions are available for **creating** and **deleting directories**. When creating a new directory with `mkdir()`, all of the parent directories must already exist. When a directory is removed with `rmdir()`, only the leaf directory (the last part of the path) is actually removed. In contrast, `makedirs()` and `removedirs()` operate on all of the nodes in the path. `makedirs()` will create any parts of the path that do not exist, and `removedirs()` will remove all of the parent directories, as long as they are empty.


```python
import os

if __name__ == "__main__":
    dir_name = "os_directories_example"

    print("Creating", dir_name)
    os.makedirs(dir_name)
    input("Press Enter to continue...")

    filename = os.path.join(dir_name, "example.txt")
    print("Creating", filename)
    with open(filename, "wt") as f:
        f.write("example file")
    input("Press Enter to continue...")

    print("Cleaning up")
    os.unlink(filename)
    os.rmdir(dir_name)

```

## Working with Symbolic Links

Use `symlink()` to **create a symbolic link** and `readlink()` to **read a link** and determine the original file pointed to by the link. The `lstat()` function is like `stat()`, but it operates on **symbolic links**.

```python
import os

if __name__ == "__main__":
    link_name = "/tmp/" + os.path.basename(__file__)

    print("Creating link {} -> {}".format(link_name, __file__))
    os.symlink(__file__, link_name)
    input("Press Enter to continue...")

    stat_info = os.lstat(link_name)
    print("Permissions:", oct(stat_info.st_mode))

    print("Points to:", os.readlink(link_name))

    # Clean up
    os.unlink(link_name)

```














