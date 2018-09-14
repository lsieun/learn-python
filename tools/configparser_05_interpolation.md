# configparser

## Combining Values with Interpolation

`ConfigParser` provides a feature called `interpolation` that can be used to **combine values**. The retrieval of values containing **standard Python format strings** triggers this `interpolation` feature. Each of the options named within the value being fetched is replaced with its value in turn, until no more substitutions are necessary.

> 这段话的意思：  
> （1）ConfigParser有一个特性叫interpolation。  
> （2）要触发interpolation特性，需要使用到standard Python format strings。

```txt
[bug_tracker]
protocol = http
server = localhost
port = 8080
url = %(protocol)s://%(server)s:%(port)s/bugs/
username = admin
password = abcdef
```

`Interpolation` is performed by default each time `get()` is called. To retrieve the original value, without interpolation, pass a `True` value in the `raw` argument.

```python
from configparser import ConfigParser

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read("interpolation.ini")

    origin_value = parser.get("bug_tracker", "url")
    parser.set("bug_tracker", "port", "9090")
    altered_value = parser.get("bug_tracker", "url")
    raw_value = parser.get("bug_tracker", "url", raw=True)

    print("Origin value: {}".format(origin_value))
    print("Altered port value: {}".format(altered_value))
    print("Without interpolation: {}".format(raw_value))

```

```txt
$ python configparser_interpolation.py

Origin value: http://localhost:8080/bugs/
Altered port value: http://localhost:9090/bugs/
Without interpolation: %(protocol)s://%(server)s:%(port)s/bugs/
```



```txt

```

```python

```








