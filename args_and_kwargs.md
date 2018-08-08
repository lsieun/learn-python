# `*args` and `**kwargs` in python explained

URL: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

Let me tell you that it is not necessary to write `*args` or `**kwargs`. Only the `*` (aesteric) is necessary. You could have also written `*var` and `**vars`. Writing `*args` and `**kwargs` is just a convention.

## 1、Using `*args` and `**kwargs` to define a function

`*args` and `**kwargs` are mostly used in **function definitions**. `*args` and `**kwargs` allow you to pass **a variable number of arguments** to a function. What does **variable** mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords.

> 此处是用于function definitions  
> 适用的情况：对于用户传入参数的个数是未知的。

### 1.1、Usage of `*args` 

 `*args` is used to send a **non-keyworded variable length argument list** to the function. Here’s an example to help you get a clear idea:

 ```python
def test_var_args(first_arg, *args):
    print("first normal arg:", first_arg)
    for arg in args:
        print("another arg through *args:", arg)

test_var_args("Apple", "Banana", "Watermelon", "Orange")
 ```

This produces the following result:

```
first normal arg: Apple
another arg through *args: Banana
another arg through *args: Watermelon
another arg through *args: Orange
```

### 1.2、Usage of `**kwargs`

`**kwargs` allows you to pass **keyworded** variable length of arguments to a function. You should use `**kwargs` if you want to handle **named arguments** in a function. 

```python
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s = %s" % (key, value))

greet_me(username="liusen", password="123456")
```

This produces the following result:

```
username = liusen
password = 123456
```

## 2、Using `*args` and `**kwargs` to call a function

So here we will see how to **call a function** using `*args` and `**kwargs`.

> 此处是用于call a function

Just consider that you have this little function:

```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)
```

Now you can use *args or **kwargs to pass arguments to this little function. 

### 2.1、Usage of `*args` 

```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

args = ("two", 3, 5)
test_args_kwargs(*args)
```

### 2.2、Usage of `**kwargs`

```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

kwargs = {"arg3":3, "arg2":"two", "arg1":5}
test_args_kwargs(**kwargs)
```

## 3、Order of using *args **kwargs and formal args

So if you want to use all three of these in functions then **the order** is

```python
some_func(fargs,*args,**kwargs)
```

## My Demo

```python
def func(host="localhost", port=1234):
    print("Host = %s" % host)
    print("Port = %s" % port)

if __name__ == '__main__':
    d = {
        "host":"192.168.80.1",
        "port":4567
    }
    func(**d)
```

输出：
```
Host = 192.168.80.1
Port = 4567
```

```python
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s = %s" % (key, value))

d = {
    "username": "liusen",
    "password": "123456"
}
greet_me(**d)
```
