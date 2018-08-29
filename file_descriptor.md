# File Descriptor

OS Vs Process
OS Vs Descriptors
Process Vs File Descriptors

## OS Vs Process

How to see process created by specific user in Unix/linux

```bash
ps -u [username]
```

## OS Vs File Descriptors

The number of open files is limited by the operating system. 

On linux you can type `ulimit -n` to see what the limit is. When you run `ulimit -n` you should see a number. That's the current limit on number of open file descriptors (which includes files, sockets, pipes, etc) for the process. The ulimit command executed the `getrlimit(2)` system call to find out what the current value is.

Here's the key point: a process inherits its current limit from its parent process. So if you ran `ulimit -n 64` you would set that shell's limit of open file descriptors to 64. Any process that shell starts would have the same limit, unless that new process calls `setrlimit()` appropriately. A process can change its limits via the `setrlimit()` system call. 

For Example: To change mongodb's open file descriptor limit, you'd run `ulimit -n 2048` (or whatever large number your kernel allows) in a shell. You'd then use that shell to start `mongodb`. As a child process,  mongodb would inherit the (large) limit on open file descriptors.

To check change the limit of open file handles on Linux, you can use the Python module `resource`:

```python
import resource

# the soft limit imposed by the current configuration
# the hard limit imposed by the operating system.
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print("Soft limits is {}".format(soft))
print("Hard limits is {}".format(hard))

# For the following line to run, you need to execute the Python script as root.
resource.setrlimit(resource.RLIMIT_NOFILE, (3000, hard))


soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print("Soft limits is {}".format(soft))
print("Hard limits is {}".format(hard))

```

Output:

```txt
Soft limits is 1024
Hard limits is 4096
Soft limits is 3000
Hard limits is 4096
```

## Process Vs File Descriptor

On Linux, you can use `lsof` to show all files opened by a process.

To change the limits of a running process, you may use the utility command `prlimit`.
```bash
prlimit --pid 12345 --nofile=1024:1024
```
What that does internally is to call `setrlimit(2)`.


```python
import psutil

def display_files():
    proc: psutil.Process = psutil.Process()
    lst: list = proc.open_files()
    for item in lst:
        print(item)

if __name__ == '__main__':
    print("Before open:")
    display_files()

    print("After open:")
    f = open("log.txt")
    display_files()

    print("After close:")
    f.close()
    display_files()

```

```python
import os
import os.path
import time

def get_fds(pid):
    return os.listdir("/proc/{pid}/fd/".format(pid=pid))

def get_pos(pid, fd):
    filename = "/proc/{pid}/fdinfo/{fd}".format(pid=pid, fd=fd)
    with open(filename) as f:
        pos_line = f.readline()
        return int(pos_line[5:])

def get_size(pid, fd):
    return os.path.getsize(get_path(pid, fd))

class FdIsPipe(Exception): pass

def get_path(pid, fd):
    result: str = os.readlink("/proc/{pid}/fd/{fd}".format(pid=pid, fd=fd))
    if result.startswith("pipe:[") or result.startswith("anon_inode"):
        raise FdIsPipe(result)
    return result

def main(argv):
    pid = argv[1]
    print("pid = {}".format(pid))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
```

I actually have a argument in favour of using `with` :
if ever the program gets interrupted in an abnormal way, say by a system signal under Linux, the file won’t ever be written to disk.

```python
import os
import signal

with open("tmp.txt", "w") as f:
    f.write("Hello World\n")
    os.kill(os.getpid(), signal.SIGTERM)
```

