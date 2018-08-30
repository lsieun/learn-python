# Formatted Output

URL: https://www.python-course.eu/python3_formatted_output.php
URL: https://pyformat.info/

There are **two formatting methods** can be found in the official Python documentation:

- **old style**: `'%s %s' % ('one', 'two')`
- **new style**: `'{} {}'.format('one', 'two')`

我觉得应该掌握这么几点：
- 输出不同类型的数据（字符串、整数、浮点数）
- 对齐（左对齐或右对齐）
- new style: positional argument Vs keyword argument

## print with seporator

We used `print` with **a comma** separated list of values to print out the results.

```python
>>> q = 459
>>> p = 0.098
>>> print(q, p, p * q)
459 0.098 44.982
```

All the values are separated by **blanks**, which is the default behaviour. We can **change the default value** to an arbitrary string, if we assign this string to the keyword parameter "`sep`" of the `print` function:

```python
>>> print(q, p, p * q, sep=",")
459,0.098,44.982
>>> print(q, p, p * q, sep=" :-) ")
459 :-) 0.098 :-) 44.982
```

## Old Style: Using `%`

The modulo operator "`%`" is overloaded by the string class to perform string formatting. Therefore, it is often called **string modulo** (or somethimes even called modulus) **operator**, though it has not a lot in common with the actual modulo calculation on numbers. 

Since **Python 2.6** has been introduced, the string method `format` should be used instead of **this old-style formatting**. Unfortunately, string modulo "`%`" is still available in Python3 and what is even worse, it is still widely used. That's why we cover it in great detail in this tutorial. You should be capable of understanding it, when you encounter it in some Python code. But it is very likely that one day this old style of formatting will be removed from the language. So you should get used to `str.format()`. 


## New Style: Using `.format()`

The general form of this method looks like this: 

```python
template.format(p0, p1, ..., k0=v0, k1=v1, ...)
```

There are **two kinds of arguments** for the `.format()` method. The list of arguments starts with zero or more positional arguments (p0, p1, ...), it may be followed by zero or more **keyword arguments** of the form `name=value`. 


### positional argument

```python
"Art: {0:5d}, Price per Unit: {1:6.2f}".format(453, 59.058)
```

### keyword argument

```python
>>> print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))
The capital of Ontario is Toronto
>>>
```

This case can be expressed with a dictionary as well, as we can see in the following code:
```python
>>> data = dict(province="Ontario",capital="Toronto")
>>> data
{'province': 'Ontario', 'capital': 'Toronto'}
>>> print("The capital of {province} is {capital}".format(**data))
The capital of Ontario is Toronto
```

### align

It's possible to left or right justify data with the `format` method. To this end, we can precede the formatting with a "`<`" (left justify) or "`>`" (right justify). We demonstrate this with the following examples: 

```python
>>> "{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99)
'Spam & Eggs:           6.99'
>>> "{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99)
'        Spam & Eggs:   6.99'
```

