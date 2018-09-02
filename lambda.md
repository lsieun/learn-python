# The Lambda Expression

URL: https://www.dataquest.io/blog/introduction-functional-programming-python/

Instead of the `def` syntax for function declaration, we can use a **lambda expression** to write **Python functions**. The `lambda` syntax closely follows the `def` syntax, but it's not a 1-to-1 mapping. 

Here's an example of building a function that adds two integers:

```python
# Using `def` (old way).
def old_add(a, b):
    return a + b

# Using `lambda` (new way).
new_add = lambda a, b: a + b

old_add(10, 5) == new_add(10, 5)
>> True
```

The `lambda` expression takes in a **comma seperated** sequences of inputs (like `def`). Then, immediately following **the colon**, it returns **the expression** without using an explicit `return` statement. Finally, when assigning **the lambda expression** to **a variable**, it acts exactly like a Python function, and can be called using the the function call syntax: `new_add()`.

> 参数：以comma分隔 各个参数 
> colon：  分隔 参数 和 函数体
> 返回：不带有return without using an explicit return statement
> 调用：加上小括号

If we didn't assign `lambda` to a variable name, it would be called an **anonymous function**. These anonymous functions are extremely helpful, especially when using them as an input for another function. For example, the `sorted()` function takes in an optional `key` argument (a function) that describes how the items in a list should be sorted.

```python
unsorted = [('b', 6), ('a', 10), ('d', 0), ('c', 4)]

# Sort on the second tuple value (the integer).
print(sorted(unsorted, key=lambda x: x[1]))
>> [('d', 0), ('c', 4), ('b', 6), ('a', 10)]
```





