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

### Dict: dict get

Bad Code:

```python
log_severity = None
if 'severity' in configuration:
    log_severity = configuration['severity']
else :
    log_severity = 'Info'
```

Good Code:

```python
log_severity = configuration.get('severity', 'Info')
```

### Dict: dict comprehensions

BadCode: `code/dict_comprehension_bad_code.py`

```python
user_email = {}
for user in users_list:
    if user.email:
        user_email[user.name] = user.email
```

Good Code: `code/dict_comprehension_good_code.py`

```python
user_email = {
    user.name : user.email
    for user in users_list
    if user.email
}
```

### String: string format

Bad Code:

```python
def get_formatted_user_info_worst(user):
    # Tedious to type and prone to conversion errors
    return 'Name: ' + user.name + ', Age: ' + \
           str(user.age) + ', Sex: ' + user.sex

def get_formatted_user_info_slightly_better(user):
    # No visible connection between the format string placeholders
    # and values to use. Also, why do I have to know the type?
    # Don't these types all have __str__ functions?
    return 'Name: %s, Age: %i, Sex: %c' % (user.name, user.age, user.sex)
```

Good Code:

```python
def get_formatted_user_info(user):
    # Clear and concise. At a glance I can tell exactly what
    # the output should be. Note: this string could be returned
    # directly, but the string itself is too long to fit on the
    # page.
    output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)
    return output
```

### String: `"".join`

Bad Code:

```python
result_list = ['True', 'False', 'File not found']
result_string = ''
for result in result_list:
    result_string += result
```

Good Code:

```python
result_list = ['True', 'False', 'File not found']
result_string = ''.join(result_list)
```

### String: chain functions

When applying a simple sequence of transformations on some datum(数据；资料), chaining the
calls in a single expression is often more clear than creating a temporary variable
for each step of the transformation. Too much chaining, however, can make your
code harder to follow. “**No more than three chained functions**” is a good rule of
thumb.

Bad Code:

```python
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip()
formatted_book_info = formatted_book_info.upper()
formatted_book_info = formatted_book_info.replace(':', ' by')
```

Good Code: `code/string_chain_functions.py`

```python
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip().upper().replace(':', ' by')
```


Use `''.startswith()` and `''.endswith()` instead of `string slicing` to check for prefixes or suffixes.

Object type comparisons should always use `isinstance()` instead of comparing types directly.

Yes: `if isinstance(obj, int):`

No:  `if type(obj) is type(1):`





