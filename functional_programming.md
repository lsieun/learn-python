# Functional Programming

URL: https://www.dataquest.io/blog/introduction-functional-programming-python/  

While the ability to pass in **functions** as **arguments** is not unique to Python, it is a recent development in programming languages. Functions that allow for this type of behavior are called **first-class functions**. Any language that contains first-class functions can be written in a functional style.

There are a set of important **first-class functions** that are commonly used within the **functional paradigm**. These functions take in a **Python iterable**, and, like `sorted()`, apply **a function** for each element in the list. Over the next few sections, we will examine each of these functions, but they all follow the general form of `function_name(function_to_apply, iterable_of_elements)`.

> 从数学的“函数”角度去理解，而不是从编程的“函数”(function)去理解。  
> 数学意义的“函数”是将一个集合通过某种映射关系形成另外一个集合。  
> 所以，对于functional programming来说，需要两样东西： （1）原始集合；（2）映射关系。

## The Map Function

The first function we'll work with is the `map()` function. The `map()` function takes in **an iterable** (ie. list), and creates **a new iterable object**, **a special `map` object**. The new object has the first-class function applied to every element.

```python
# Pseudocode for map.
def map(func, seq):
    # Return `Map` object with
    # the function applied to every
    # element.
    return Map(
        func(x)
        for x in seq
    )
```

Here's how we could use map to add 10 or 20 to every element in a list:

```python
values = [1, 2, 3, 4, 5]

# Note: We convert the returned map object to
# a list data structure.
add_10 = list(map(lambda x: x + 10, values))
add_20 = list(map(lambda x: x + 20, values))

print(add_10)
>> [11, 12, 13, 14, 15]

print(add_20)
>> [21, 22, 23, 24, 25]
```

Note that it's important to cast the return value from `map()` as a `list` object. Using the returned map object is difficult to work with if you're expecting it to function like a list. **First**, printing it does not show each of its items, and **secondly**, you can only iterate over it once.

```python
values = [1, 2, 3, 4, 5]

obj = map(lambda x: x + 10, values)

print(type(obj))
>> <class 'map'>

print(obj)
>> <map object at 0x7f557917f860>

for item in obj:
   print(item, end=",")
  
>> 11,12,13,14,15,

for item in obj:
   print(item, end=",")
 
>> 
In [12]: 

```

## The Filter Function

The second function we'll work with is the `filter()` function. The `filter()` function takes in **an iterable**, creates **a new iterable object** (again, a special `map` object), and **a first-class function** that must return a `bool` value. The new map object is a filtered iterable of all elements that returned True.

```python
# Pseudocode for filter.
def filter(evaluate, seq):
    # Return `Map` object with
    # the evaluate function applied to every
    # element.
    return Map(
        x for x in seq
        if evaluate(x) is True
    )
```

Here's how we could filter odd or even values from a list:

```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Note: We convert the returned filter object to
# a list data structure.
even = list(filter(lambda x: x % 2 == 0, values))
odd = list(filter(lambda x: x % 2 == 1, values))

print(even)
>> [2, 4, 6, 8, 10]

print(odd)
>> [1, 3, 5, 7, 9]
```

## The Reduce Function

The last function we'll look at is the `reduce()` function from the `functools` package. The `reduce()` function takes in **an iterable**, and then reduces **the iterable** to **a single value**. **Reduce** is different from `filter()` and `map()`, because `reduce()` takes in **a function** that has **two input values**.

Here's an example of how we can use `reduce()` to sum all elements in a list.

```python
from functools import reduce

values = [1, 2, 3, 4]

summed = reduce(lambda a, b: a + b, values)
print(summed)
>> 10
```

![](https://dq-content.s3.amazonaws.com/263/s5_reduce_function.svg)

An interesting note to make is that you do not have to operate on the second value in the lambda expression. For example, you can write a function that always returns the first value of an iterable:

```python
from functools import reduce

values = [1, 2, 3, 4, 5]

# By convention, we add `_` as a placeholder for an input
# we do not use.
first_value = reduce(lambda a, _: a, values)
print(first_value)
>> 1
```

## Rewriting with list comprehensions

Because we eventually convert to **lists**, we should rewrite the `map()` and `filter()` functions using **list comprehension** instead. This is the more pythonic way of writing them, as we are taking advantage of the Python syntax for making lists. Here's how you could translate the previous examples of `map()` and `filter()` to **list comprehensions**:

```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map.
add_10 = [x + 10 for x in values]
print(add_10)
>> [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Filter.
even = [x for x in values if x % 2 == 0]
print(even)
>> [2, 4, 6, 8, 10]
```

From the examples, you can see that we don't need to add the **lambda expressions**. If you are looking to add map(), or filter() functions to your own code, this is usually the recommended way. 



