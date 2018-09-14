# logging

## Logging Components

The `logging` system consists of **four** interacting types of objects. 

- **Logger**: Each module or application that wants to log some activity uses a `Logger` instance to add information to the logs.
- **LogRecord**: Invoking the `logger` creates a `LogRecord` , which holds the information in memory until it is processed. 
- **Handler**: A `Logger` may have a number of `Handler` objects configured to receive and process log records. 
- **Formatter**: The `Handler` uses a `Formatter` to turn the log records into output messages.

> Logger -> LogRecord -> Handler -> Formatter

## Logging to a File

Most applications are configured to log to a **file**. Use the `basicConfig()` function to set up **the default handler** so that debug messages are written to a file.

```python
import logging

LOG_FILENAME = "logging_example.out"
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG
)

logging.debug("This message should go to the log file")

with open(LOG_FILENAME, "rt") as f:
    body = f.read()

print("FILE:")
print(body)

```

## Verbosity Levels

Another useful feature of the logging API is the ability to produce different messages at **different log levels**. 

The log message is shown only if the handler and the logger are configured to emit messages of that level or higher. For example, if a message is `CRITICAL` , and the logger is set to `ERROR` , the message is generated (50 > 40). If a message is a `WARNING` , and the logger is set to produce only messages set to `ERROR` , the message is not generated (30 < 40).



| Level    | Value |
| -------- | ----- |
| CRITICAL | 50    |
| ERROR    | 40    |
| WARNING  | 30    |
| INFO     | 20    |
| DEBUG    | 10    |
| UNSET    | 0     |


```python
import logging
import sys

LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

```


Output:

```txt
python3 logging_level_example.py info

INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

The word `root` was embedded in all of the previous log messages because the code uses **the root logger**.

## Naming Logger Instances

An easy way to tell where a specific log message originates is to use **a separate logger object** for each module; **log messages** sent to **a logger** include **the name of that logger**.

The following example illustrates logging from different modules in a way that **makes it easy to trace the source of the message**.

```python
import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger("package1.module1")
logger2 = logging.getLogger("package2.module2")

logger1.warning("This message comes from one module")
logger2.warning("This message comes from another module")

```

Output:

```txt
$ python logging_module_example.py 

WARNING:package1.module1:This message comes from one module
WARNING:package2.module2:This message comes from another module
```














