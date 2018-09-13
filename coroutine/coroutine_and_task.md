# Coroutines as Tasks

## The Task Concept

In **concurrent programming**, one typically subdivides **problems** in to "`tasks`".

Tasks have a few essential features:

- Independent control flow
- Internal state
- Can be scheduled(suspend/resumed)
- Can communicate with other tasks

Claim: **Coroutines** are **tasks**.

## Are Coroutines Tasks?

Let's look at the essential parts.

Coroutines have their own **control flow**. A coroutine is just a sequence of statements like any other Python function.

```python
@coroutine
def grep(pattern):
    print("Looking for {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print(line)
```

Coroutines have their own **internal state**, such as `pattern` and `line` local variables in above code. The **local variables** live as long as the coroutine is active. They establish an execution environment.

Coroutines can **communicate**. The `.send()` method sends **data** to **a coroutine**. `yield expression` receive input.

Coroutines can be **suspended** and **resumed**:
- `yield` suspends execution
- `send()` resumes execution
- `close()` terminates execution










