## 结束进程

Key Code:

```python
os.kill(os.getpid(), signal.SIGTERM)
```

Full Code:

```python
import os
import signal

with open("tmp.txt", "w") as f:
    f.write("Hello World\n")
    os.kill(os.getpid(), signal.SIGTERM)
```