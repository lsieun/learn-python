# functools

## Writing Function Partials

Sometimes we want to use the behavior of a function, but decrease the number of arguments it takes. The purpose is to "save" one of the inputs, and create a new function that defaults the behavior using the saved input. Suppose we wanted to write a function that would always add 2 to any number:

```python
def add_two(b):
    return 2 + b 

print(add_two(4))
>> 6
```

The `add_two` function is similar to the general function, `$f(a,b) = a + b$`, only it defaults one of the arguments (`$a = 2$`). In Python, we can use the `partial` module from the `functools` package to set these **argument defaults**. The `partial` module takes in **a function**, and "freezes" any number of args (or kwargs), starting from the **first argument**, then returns a new function with **the default inputs**.

```python
from functools import partial

def add(a, b):
    return a + b


add_two = partial(add, 2)
add_ten = partial(add, 10)

print(add_two(4))
>> 6

print(add_ten(4))
>> 14
```

Partials can take in any function, including ones from **the standard library**.

```python
# A partial that grabs IP addresses using
# the `map` function from the standard library.
extract_ips = partial(
    map,
    lambda x: x.split(' ')[0]
)
lines = read('example_log.txt')
ip_addresses = list(extract_ip(lines))
```

example_log.txt

```txt
31.13.75.17 www.google.com
61.135.169.125 www.baidu.com
66.102.251.33 www.sina.com
```

Full Code:

```python
from functools import partial

def read(filename: str) -> list:
    with open(filename, "r") as f:
        return [line for line in f]


if __name__ == '__main__':
    extract_ips = partial(
        map,
        lambda x: x.split(" ")[0]
    )

    lines = read("example_log.txt")
    ip_addresses = list(extract_ips(lines))
    print(ip_addresses)

```

Output:

```txt
['31.13.75.17', '61.135.169.125', '66.102.251.33']
```