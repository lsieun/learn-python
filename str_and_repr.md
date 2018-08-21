# What does !r do in str() and repr()?

URL: https://stackoverflow.com/questions/38418070/what-does-r-do-in-str-and-repr

 In python, there are **two fairly natural choices** to get a string representation of something ... `str` and `repr`.  
 
 - `str` is generally a little more human friendly, 
 - `repr` is generally more precise. 
  
  Perhaps the [official documentation](https://docs.python.org/3/reference/datamodel.html#object.__repr__) is the best place to go looking for the difference:


In `str.format`, `!s` chooses to use `str` to format the object whereas `!r` chooses `repr` to format the value.

The difference can easily be seen with strings (as `repr` for a string will include outer quotes).:

```python
>>> 'foo {}'.format('bar')
'foo bar'
>>> 'foo {!r}'.format('bar')
"foo 'bar'"
```
What the difference between these two methods really depends critically on the objects being formatted. For many objects (e.g. those that don't override the `__str__` method), there will be no difference in the formatted output.

```python
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "This is Dog, its name is {} and its age is {}".format(self.name, self.age)

    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)

if __name__ == '__main__': 
    dog = Dog("little dog", 1)
    print("{!r}".format(dog))
    print("{!s}".format(dog))
    print("{}".format(dog))

```

Output:
```txt
This is Dog, its name is little dog and its age is 1
Name: little dog, Age: 1
Name: little dog, Age: 1
```
