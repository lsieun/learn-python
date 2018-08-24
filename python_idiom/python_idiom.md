# Writing idiomatic python

## Control Flow And Function

But at a deeper level, the reasoning is based on the difference between **equality** and **identity** . Using `==` determines if two objects **have the same value** (as defined by their `_eq` attribute). Using `is` determines if the two objects are **actually the same object**.

Note the use of `is not` : comparisons against `None` (a singleton in Python) should always use `is` or `is not` , not `==` (from PEP8).

bytes:
bool: Flase
object: None
int(number): 0
tutple: ()
dict: {}
list: []


One of the lesser known facts about Python’s `for` loop is that it can include an `else` clause. The `else` clause is executed after the iterator is exhausted, unless the loop was ended prematurely due to a `break` statement.

## Working with data

### List: list comprehensions

Bad Code: `code/list_comprehension_bad_code.py`

```python
num_list = range(10)
some_list = list()
for num in num_list:
    if is_prime(num):
        some_list.append(num + 5)
```

Good Code: `code/list_comprehension_good_code.py`

```python
num_list = range(10)
some_list = [
    num + 5
    for num in num_list
    if is_prime(num)
]
```

### List: `* operator`

Bad Code: `code/asterisk_operator_bad_code.py`

```python
some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, rest) = some_list[0], some_list[1], some_list[2:]
print(rest)
(first, middle, last) = some_list[0], some_list[1:-1], some_list[-1]
print(middle)
(head, penultimate, last) = some_list[:-2], some_list[-2], some_list[-1]
print(head)
```

Good Code: `code/asterisk_operator_good_code.py`

```python
some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, *rest) = some_list
print(rest)
(first, *middle, last) = some_list
print(middle)
(*head, penultimate, last) = some_list
print(head)
```

















