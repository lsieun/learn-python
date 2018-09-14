# getpass: Secure Password Prompt

The `getpass()` function prints a prompt, then reads input from the user until the user
presses the enter key. The input is returned as a string to the caller.

```python
import getpass

try:
    p = getpass.getpass()
except Exception as err:
    print("Error:", err)
else:
    print("You entered: {}".format(p))

```

Output:

```txt
$ python getpass_defaults.py
Password: 
You entered: tomcat
```

