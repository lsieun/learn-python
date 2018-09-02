# Functional Programming

URL: https://www.dataquest.io/blog/introduction-functional-programming-python/  

## Comparing object-oriented to functional

Within the **class**, there are the familiar concepts of **methods** and **properties**. The **properties** set and retrieve the `state` of the object, and the **methods** manipulate that `state`.

```python
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
    
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)
```

```python
# example_file.txt contains 100 lines.
lc = LineCounter('example_file.txt')
print(lc.lines)
>> []
print(lc.count())
>> 0

# The lc object must read the file to
# set the lines property.
lc.read()
# The `lc.lines` property has been changed.
# This is called changing the state of the lc
# object.
print(lc.lines)
>> [['Hello world!', ...]]
print(lc.count())
>> 100
```

The **ever-changing state** of **an object** is both its **blessing** and **curse**. To understand why a changing state can be seen as a negative, we have to introduce an alternative. The alternative is to build the line counter as a series of **independent functions**.

> ever-changing 不断变化的

```python
def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read('example_log.txt')
lines_count = count(example_lines)
```

## Working with **pure functions**

The concepts behind **functional programming** requires **functions** to be `stateless`, and rely **only** on their `given inputs` to produce `an output`.

The functions that meet the above criteria are called **pure functions**.

```python
# Create a global variable `A`.
A = 5

def impure_sum(b):
    # Adds two numbers, but uses the
    # global `A` variable.
    return b + A

def pure_sum(a, b):
    # Adds two numbers, using
    # ONLY the local function inputs.
    return a + b

print(impure_sum(6))
>> 11

print(pure_sum(4, 6))
>> 10
```

The benefit of using **pure functions** over **impure (non-pure) functions** is the reduction of **side effects**. 

