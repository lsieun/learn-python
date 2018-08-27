# File Read

URL: http://www.bogotobogo.com/python/python_files.php


Alone.txt

```txt
나 혼자 (Alone) - By Sistar
추억이 이리 많을까 넌 대체 뭐할까
아직 난 이래 혹시 돌아 올까 봐
```

## read()

```python
>>> file = open('Alone.txt', encoding='utf-8')
>>> str = file.read()
>>> str
'나 혼자 (Alone) - By Sistar\n추억이 이리 많을까 넌 대체 뭐할까\n아직 난 이래 혹시 돌아 올까 봐\n'
>>> file.read()
''
```

Reading the file again does not raise an exception. Python does not consider reading past end-of-file to be an error; it simply returns an empty string.

```python
>>> file.read()
''
```

Since we're still at the end of the file, further calls to the stream object's `read()` method simply return an empty string.

```python
>>> file.seek(0)
0
```

The `seek()` method moves to a specific byte position in a file.

```python
>>> file.read(10)
'나 혼자 (Alon'
>>> file.seek(0)
0
>>> file.read(15)
'나 혼자 (Alone) - '
>>> file.read(1)
'B'
>>> file.read(10)
'y Sistar\n추'
>>> file.tell()
34
```

The `read()` method can take **an optional parameter**, **the number of characters to read**. We can also read one character at a time. The `seek()` and `tell()` methods always count **bytes**, but since we opened this file as text, the `read()` method counts **characters**. Korean characters require multiple bytes to encode in UTF-8. The English characters in the file only require one byte each, so we might be misled into thinking that the `seek()` and `read()` methods are counting the same thing. But that's only true for some characters.

## Reading lines one by one

A line of text is a sequence of characters delimited by what exactly? Well, it's complicated, because text files can use several different characters to mark the end of a line. Every operating system has its own convention. Some use a carriage return character(`\r`), others use a line feed character(`\n`), and some use both characters(`\r\n`) at the end of every line.

However, Python handles line endings automatically by default. Python will figure out which kind of line ending the text file uses and and it will all the work for us.

```python
# line.py

lineCount = 0
with open('Daffodils.txt', encoding='utf-8') as file:
    for line in file:
        lineCount += 1
        print('{:<5} {}'.format(lineCount, line.rstrip())) 
```

If we run it:

```txt
C:\TEST> python line.py
1     I wandered lonely as a cloud
2     That floats on high o'er vales and hills,
3     When all at once I saw a crowd,
4     A host, of golden daffodils;
```

1. Using the `with` pattern, we safely open the file and let Python close it for us.

2. To read a file one line at a time, use a `for` loop. That's it. Besides having explicit methods like `read()`, **the stream object** is also an iterator which spits out a single line every time we ask for a value.

3. Using the `format()` string method, we can print out the line number and the line itself. The format specifier `{:<5}` means print this argument left-justified within 5 spaces. The `line` variable contains the complete line, carriage returns and all. The `rstrip()` string method removes **the trailing whitespace**, including **the carriage return characters**.








