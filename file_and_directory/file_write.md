# File Write

## write()

We can write to files in much the same way that we read from them. First, we **open** a file and get a file object, then we use methods on the stream object to **write** data to the file, then **close** the file.

The method `write()` writes a string to the file. There is no return value. Due to buffering, the string may not actually show up in the file until the `flush()` or `close()` method is called.

To open a file for writing, use the `open()` function and specify the `write` mode. There are **two file modes for writing** as listed in the earlier table:

1. `write` mode will overwrite the file when the `mode='w'` of the `open()` function.

2. `append` mode will add data to the end of the file when the `mode='a'` of the `open()` function.

We should always close a file as soon as we're done writing to it, to release the file handle and ensure that the data is actually written to disk. As with reading data from a file, we can call the stream object's `close()` method, or we can use the `with` statement and let Python close the file for us.

```python
>>> with open('myfile', mode='w', encoding='utf-8') as file:
	file.write('Copy and paste is a design error.')

>>> with open('myfile', encoding='utf-8') as file:
	print(file.read())
	
Copy and paste is a design error.
>>> 
>>> with open('myfile', mode='a', encoding='utf-8') as file:
	file.write('\nTesting shows the presence, not the absence of bugs.')

>>> with open('myfile', encoding='utf-8') as file:
	print(file.read())

Copy and paste is a design error.	
Testing shows the presence, not the absence of bugs.
```







