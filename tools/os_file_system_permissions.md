# os の Managing File System Permissions

## 1、os.stat()：查看文件的metadata

Detailed information about a file can be accessed using `stat()` or `lstat()` (for checking the status of something that might be a symbolic link).

```python
import os
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) == 1:
        filename = __file__
        pass
    else:
        filename = sys.argv[1]
        pass

    stat_info: os.stat_result = os.stat(filename)

    print("os.stat({}):".format(filename))
    print("\tSize:", stat_info.st_size)
    print("\tPermissions:", oct(stat_info.st_mode))
    print("\tOwner:", stat_info.st_uid)
    print("\tDevice:", stat_info.st_dev)
    print("\tCreated:", time.ctime(stat_info.st_ctime))
    print("\tLast modified:", time.ctime(stat_info.st_mtime))
    print("\tLast accessed:", time.ctime(stat_info.st_atime))

```

Output:

```txt
$ python os_stat.py 
os.stat(os_stat.py):
	Size: 631
	Permissions: 0o100664
	Owner: 1000
	Device: 64770
	Created: Sat Sep 15 04:41:30 2018
	Last modified: Sat Sep 15 04:41:30 2018
	Last accessed: Sat Sep 15 04:41:34 2018
```

## 2、os.chmod()：修改文件的权限

On Unix-like systems, **file permissions** can be changed using `chmod()`, with the mode being passed as an integer. Mode values can be constructed using constants defined in the `stat` module. The next example toggles the user’s execute permission bit.

```python
import os
import stat

if __name__ == "__main__":
    filename = "os_stat_chmod_example.txt"

    if os.path.exists(filename):
        os.unlink(filename)
    with open(filename, "wt") as f:
        f.write("contents")

    # Determine which permission are already set using stat.
    existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

    if not os.access(filename, os.X_OK):
        print("Adding execute permission")
        new_permissions = existing_permissions | stat.S_IXUSR
    else:
        print("Removing execute permission")
        # Use xor to remove the user execute permission
        new_permissions = existing_permissions ^ stat.S_IXUSR

    os.chmod(filename, new_permissions)

```

## 3、os.access()：查看文件的权限

Use the function `access()` to test the access rights that a process has for a file.

```python
import os

if __name__ == "__main__":
    print("Testing:", __file__)
    print("Exists:", os.access(__file__, os.F_OK))
    print("Readable:", os.access(__file__, os.R_OK))
    print("Writable:", os.access(__file__, os.W_OK))
    print("Executable:", os.access(__file__, os.X_OK))

```

```txt
$ python os_access.py 
Testing: os_access.py
Exists: True
Readable: True
Writable: True
Executable: False
```


