＃ encoding

URL: http://www.diveintopython3.net/strings.html

## 第一部分：各种encoding

character encoding(decryption key)

character --> character encoding --> bytes

## 第二部分：理想／形而上者 Unicode

Unicode: every character from every language

## 第三部分：理想的各种实现方式UTF-xx

- UTF32
    - advantage: 
    - disavantage:
- UTF16
    - advantage
    - disadvantage
- UTF8: 
    - a variable-length encoding system for Unicode
    - different characters take up a different number of bytes.

Also (and you’ll have to trust me on this, because I’m not going to show you the math), due to the exact nature of the bit twiddling, there are no byte-ordering issues. **A document encoded in utf-8 uses the exact same stream of bytes on any computer**.

> 这段应该是针对big endian和little endian来说，UTF8编码的字节流在任何电脑上都是一样的。

## 第四部分：Python对待字符串

In Python 3, all strings are sequences of Unicode characters. Bytes are not characters; bytes are bytes. Characters are an abstraction. A string is a sequence of those abstractions.

> 在Python3中（不是Python2），string是Unicode character的集合，character是对bytes的抽象。


