# A guide to Python's function decorators

URL: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

In the context of **design patterns**, **decorators** dynamically alter the functionality of a function, method or class without having to directly use subclasses. This is ideal when you need to extend the functionality of functions that you don't want to modify. We can implement the decorator pattern anywhere, but Python facilitates the implementation by providing much more expressive features and syntax for that.

> 在设计模式中，decorators是dynamically alter the functionality of a function.  
> Python对于decorators提供了简洁的语法。

Essentially, decorators work as wrappers, modifying the behavior of the code before and after a target function execution, without the need to modify the function itself, augmenting the original functionality, thus decorating it.

> decorator的本质

## 1、What you need to know about functions

Before diving in, there are some prerequisites that should be clear. **In Python, functions are first class citizens**, they are objects and that means we can do a lot of useful stuff with them.

### 1.1、Assign functions to variables

```python
def greet(name):
    return "hello " + name

greet_someone = greet
print(greet_someone("John"))

# Outputs: hello John
```

### 1.2、Define functions inside other functions

```python
def greet(name):
    def get_message():
        return "Hello "
    
    result = get_message() + name
    return result

print(greet("John"))

# Outputs: Hello John
```

### 1.3、Functions can be passed as parameters to other functions

```python
def greet(name):
    return "Hello " + name

def call_func(func):
    other_name = "John"
    return func(other_name)

print(call_func(greet))

# Outputs: Hello John
```

### 1.4、Functions can return other functions

In other words, functions generating other functions.

```python
def compose_great_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_great_func()
print(greet())

# Outputs: Hello there!
```

### 1.5、Inner functions have access to the enclosing scope

Another thing to note, Python only allows **read access to the outer scope** and not assignment.

```python
def compose_great_func(name):
    def get_message():
        return "Hello there " + name + "!"

    return get_message

greet = compose_great_func("John")
print(greet())

# Outputs: Hello there John!
```

## 2、Composition of Decorators

**Function decorators are simply wrappers to existing functions**. Putting the ideas mentioned above together, we can build a decorator. In this example let's consider a function that wraps the string output of another function by `p` tags.

```python
def get_text(name):
    return "Hello {}, Welcome to this tutorial!".format(name)

def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorator(get_text)
print(my_get_text("John"))

# Outputs: <p>Hello John, Welcome to this tutorial!</p>
```

That was our first decorator. A function that takes another function as an argument, generates a new function, augmenting the work of the original function, and returning the generated function so we can use it anywhere. To have `get_text` itself be decorated by `p_decorate`, we just have to assign `get_text` to the result of `p_decorate`.

```python
get_text = p_decorator(get_text)
print(get_text("John"))

# Outputs: <p>Hello John, Welcome to this tutorial!</p>
```

Another thing to notice is that our decorated function takes a name argument. All what we had to do in the decorator is to let the wrapper of get_text pass that argument.

> 这一点值得注意：要记得参数在“decorator”和“decorated function”之间的传递。

## 3、Python's Decorator Syntax

**Python makes creating and using decorators a bit cleaner and nicer** for the programmer through some **syntactic sugar**(语法糖)) To decorate `get_text` we don't have to `get_text = p_decorator(get_text)`. There is a neat shortcut for that, which is to mention **the name of the decorating function** before **the function to be decorated**. **The name of the decorator** should be perpended with an `@` symbol.

### 3.1、decorator syntax

```python
def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorator
def get_text(name):
    return "Hello {}, Welcome to this tutorial!".format(name)

print(get_text("John"))

# Outputs: <p>Hello John, Welcome to this tutorial!</p>
```

### 3.2、multitple decorators

Now let's consider we wanted to decorate our `get_text` function by 2 other functions to wrap a `div` and `strong` tag around the string output.

```python
def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

def strong_decorator(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorator(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper
```

With the basic approach, decorating get_text would be along the lines of

```python
get_text = div_decorator(p_decorator(strong_decorator(get_text)))
```

With Python's decorator syntax, same thing can be achieved with much more expressive power.

```python
@div_decorator
@p_decorator
@strong_decorator
def get_text(name):
    return "Hello {}, Welcome to this tutorial!".format(name)

print(get_text("John"))

# Outputs: <div><p><strong>Hello John, Welcome to this tutorial!</strong></p></div>
```

One important thing to notice here is that **the order of setting our decorators** matters. If the order was different in the example above, the output would have been different.

> 重要的一点是：decorators的顺序会影响输出的结果。

完整代码如下：

```python
def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

def strong_decorator(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorator(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorator
@p_decorator
@strong_decorator
def get_text(name):
    return "Hello {}, Welcome to this tutorial!".format(name)

print(get_text("John"))

```

### 3.3、Decorating Methods

In Python, **methods** are functions that expect **their first parameter** to be **a reference to the current object**. We can build decorators for methods the same way, while taking `self` into consideration in the wrapper function.

> 这里将method和function两个概念做了区分：function是一个宽泛的概念，而method指在类里面定义的function。

```python
def p_decorator(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))
    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorator
    def get_fullname(self):
        return self.name + " " + self.family

if __name__ == '__main__':
    my_person = Person()
    print(my_person.get_fullname())

# Outputs: <p>John Doe</p>
```

A much better approach would be to make our decorator useful for functions and methods alike. This can be done by putting `*args` and `**kwargs` as parameters for the wrapper, then it can accept **any arbitrary number** of **arguments** and **keyword arguments**.

```python
def p_decorator(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorator
    def get_fullname(self):
        return self.name + " " + self.family

if __name__ == '__main__':
    my_person = Person()
    print(my_person.get_fullname())

# Outputs: <p>John Doe</p>
```

### 3.4、Passing arguments to decorators

Looking back at the example before the one above, you can notice how redundant the decorators in the example are. 3 decorators(`div_decorate`, `p_decorate`, `strong_decorate`) each with the same functionality but wrapping the string with different tags. We can definitely do much better than that. Why not have **a more general implementation** for one that takes the tag to wrap with as a string? Yes please!

```python
def tags(tag_name):
    def tag_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tag_decorator

@tags("p")
def get_text(name):
    return "Hello " + name

print(get_text("John"))
```

It took a bit more work in this case. Decorators expect to receive a function as an argument, that is why we will have to build a function that takes those extra arguments and generate our decorator on the fly. In the example above `tags`, is our decorator generator.

测试多个标签：

```python
def tags(tag_name):
    def tag_decorator(func):
        def func_wrapper(*args, **kwargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kwargs))
        return func_wrapper
    return tag_decorator

@tags("div")
@tags("p")
@tags("strong")
def get_text(name):
    return "Hello " + name

print(get_text("John"))

# Outputs: <div><p><strong>Hello John</strong></p></div>
```

### 3.5、Debugging decorated functions

At the end of the day, decorators are just wrapping our functions, in case of debugging that can be problematic since the wrapper function does not carry the `name`, `module` and `docstring` of **the original function**. Based on the example above if we do:

```python
print(get_text.__name__)

# Outputs: func_wrapper
```

The output was expected to be `get_text` yet, the attributes `__name__`,` __doc__`, and `__module__` of `get_text` got overridden by those of the `wrapper(func_wrapper)`. Obviously we can reset them within `func_wrapper` but Python provides a much nicer way.

**Functools to the rescue**

Fortunately Python includes the `functools` module which contains `functools.wraps`. `Wraps` is a decorator for updating the attributes of the wrapping `function(func_wrapper)` to those of the original `function(get_text)`. This is as simple as decorating `func_wrapper` by `@wraps(func)`. Here is the updated example:

```python
from functools import wraps

def tags(tag_name):
    def tag_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kwargs))
        return func_wrapper
    return tag_decorator

@tags("p")
def get_text(name):
    """return some text"""
    return "Hello " + name

print(get_text("John"))

print(get_text.__name__)    # get_text
print(get_text.__doc__)     # return some text
print(get_text.__module__)  # __main__

```

You can notice from the output that the attributes of `get_text` are the correct ones now.

## 4、Where to use decorators

The examples in this post are pretty simple relative to how much you can do with decorators. They can give so much power and elegance to your program. 

In general, **decorators are ideal for extending the behavior of functions that we don't want to modify**. 

For a great list of useful decorators I suggest you check out the [Python Decorator Library](https://wiki.python.org/moin/PythonDecoratorLibrary)