# aiohttp client

URL: https://aiohttp.readthedocs.io/en/stable/client_quickstart.html


## 1、Request

Don’t create a `session` per request. Most likely you need a `session` per `application` which performs all requests altogether.

More complex cases may require a `session` per `site`, e.g. one for Github and other one for Facebook APIs. Anyway making a session for every request is **a very bad idea**.

A session contains a connection pool inside. Connection reusage and keep-alives (both are on by default) may speed up total performance.

### 1.1、Request: Simple Get

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://httpbin.org/get")
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

### 1.2、Request: Get+query string

Key Code:
```python
session.get(url, params=params)
```

Full Code:
```python
import aiohttp
import asyncio

async def fetch(session, url, params):
    async with session.get(url, params=params) as resp:
        full_url = resp.url
        print("old url = {}".format(url))
        print("new url = {}\r\n".format(full_url))
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        params = {"username":"tom", "password":"123"}
        html = await fetch(session, "https://httpbin.org/get", params)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output: 

```txt
old url = https://httpbin.org/get
new url = https://httpbin.org/get?username=tom&password=123

{
  "args": {
    "password": "123", 
    "username": "tom"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/get?username=tom&password=123"
}
```

### 1.3、Request: Post+text

To send text with appropriate content-type just use `data` attribute.

Key Code:

```python
session.post(url, data=text)
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url, text):
    async with session.post(url, data=text) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://httpbin.org/post"
        text = "Hello World"
        html = await fetch(session, url, text)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```


Output: 注意Content-type字段的值。

```txt
{
  "args": {}, 
  "data": "Hello World", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "11", 
    "Content-Type": "text/plain; charset=utf-8", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": null, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

### 1.4、Request: Post+json

Key Code:

```python
session.post(url, json=json_dict)
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url, json_dict):
    async with session.post(url, json=json_dict) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        json_dict = {"username":"tom", "password":123}
        html = await fetch(session, "https://httpbin.org/post", json_dict)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
{
  "args": {}, 
  "data": "{\"username\": \"tom\", \"password\": 123}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "36", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": {
    "password": 123, 
    "username": "tom"
  }, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

By default `session` uses python’s standard `json` module for serialization. But it is possible to use different serializer. `ClientSession` accepts `json_serialize` parameter:

```python
import ujson

async with aiohttp.ClientSession(
        json_serialize=ujson.dumps) as session:
    await session.post(url, json={'test': 'object'})
```

> Note: `ujson` library is faster than standard `json` but slightly incompatible.

### 1.5、Request: Post+form string

Typically, you want to send some **form-encoded data** – much like an HTML form. To do this, simply pass a **dictionary** to the `data` argument. Your **dictionary of data** will automatically be **form-encoded** when the request is made.

Key Code:

```python
session.post(url, data=payload)
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url, payload):
    async with session.post(url, data=payload) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://httpbin.org/post"
        payload = {"username":"tom", "password":"123"}
        html = await fetch(session, url, payload)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "password": "123", 
    "username": "tom"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "25", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": null, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

### 1.6、Request: Post+form file

If you pass a **file object** as `data` parameter, aiohttp will stream it to the server automatically. 

Key Code:

```python
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

await session.post(url, data=files)
```

`myfile.txt`:

```txt
Hello World
Hello Python
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url, filename):
    files = {"file": open(filename, "rb")}
    async with session.post(url, data=files) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://httpbin.org/post"
        filename = "myfile.txt"
        html = await fetch(session, url, filename)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "Hello World\nHello Python\n"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "246", 
    "Content-Type": "multipart/form-data; boundary=ce419740d2f64afbb2aa78fbeb0850a7", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": null, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

### 1.7、Request: Post+form string+file

You can set the `filename` and `content_type` explicitly:

Key Code:

```python
url = 'http://httpbin.org/post'
data = FormData()
data.add_field('file',
               open('report.xls', 'rb'),
               filename='report.xls',
               content_type='application/vnd.ms-excel')

await session.post(url, data=data)
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url, filename):
    data = aiohttp.FormData()
    data.add_field("username", "tom")
    data.add_field("password", "123")
    data.add_field("file",
                  open(filename, "rb"),
                  filename="tom.txt")
    async with session.post(url, data=data) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://httpbin.org/post"
        filename = "myfile.txt"
        html = await fetch(session, url, filename)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "Hello World\nHello Python\n"
  }, 
  "form": {
    "password": "123", 
    "username": "tom"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "544", 
    "Content-Type": "multipart/form-data; boundary=59c58a5507af41308c278a7e6de63a37", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": null, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

### 1.8、Request: Post+binary

If you want to send data that is not form-encoded you can do it by passing a `bytes` instead of a `dict`. This data will be posted directly and content-type set to ‘`application/octet-stream`’ by default.

```python
import aiohttp
import asyncio

async def fetch(session, url, data):
    async with session.post(url, data=data) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        data = b"Hello World"
        html = await fetch(session, "https://httpbin.org/post", data)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
{
  "args": {}, 
  "data": "Hello World", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "11", 
    "Content-Type": "application/octet-stream", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": null, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

### 1.9、Request: Post+stream

`aiohttp` supports multiple types of streaming uploads, which allows you to send **large files** without reading them into memory.

Key Code:

```python
async def file_sender(file_name=None):
    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64*1024)
        while chunk:
            yield chunk
            chunk = await f.read(64*1024)

# Then you can use file_sender as a data provider:

async with session.post('http://httpbin.org/post',
                        data=file_sender(file_name='huge_file')) as resp:
    print(await resp.text())
```

Full Code:

```python
import aiohttp
import asyncio
import aiofiles

async def file_sender(filename=None):
    async with aiofiles.open(filename, "rb") as f:
        chunk = await f.read(10)
        while chunk:
            yield chunk
            chunk = await f.read(10)
 
async def fetch(session, url, filename):
    async with session.post(url, data=file_sender(filename)) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://httpbin.org/post"
        filename = "myfile.txt"
        html = await fetch(session, url, filename)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
{
  "args": {}, 
  "data": "Hello World\nHello Python\n", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Type": "application/octet-stream", 
    "Host": "httpbin.org", 
    "Transfer-Encoding": "chunked", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "json": null, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/post"
}
```

## 2、Response

### 2.1、Response: status code + encoding + text

Key Code:

```python
status_code = resp.status
await resp.text(encoding="utf8")
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        status_code = resp.status
        print("status code: {}\r\n".format(status_code))
        return await resp.text(encoding="utf8")

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://httpbin.org/get?username=tom")
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
status code: 200

{
  "args": {
    "username": "tom"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.6 aiohttp/3.3.2"
  }, 
  "origin": "111.199.84.60", 
  "url": "https://httpbin.org/get?username=tom"
}
```

### 2.2、Response: json data

Key Code:

```python
await resp.json()
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        d = await resp.json()
        print("type(d) = {}\r\n".format(type(d)))
        return d

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://httpbin.org/get")
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
type(d) = <class 'dict'>

{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'httpbin.org', 'User-Agent': 'Python/3.6 aiohttp/3.3.2'}, 'origin': '111.199.84.60', 'url': 'https://httpbin.org/get'}

```

### 2.3、Response: binary data

You can also access the **response body** as `bytes`, for non-text requests.

The `gzip` and `deflate` transfer-encodings are automatically decoded for you.


Key Code:

```python
await resp.read()
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.read()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://httpbin.org/get?username=tom")
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

Output:

```txt
b'{\n  "args": {\n    "username": "tom"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Host": "httpbin.org", \n    "User-Agent": "Python/3.6 aiohttp/3.3.2"\n  }, \n  "origin": "111.199.84.60", \n  "url": "https://httpbin.org/get?username=tom"\n}\n'
```

### 2.4、Response: stream data

While methods `read()`, `json()` and `text()` are very convenient you should use them carefully. **All these methods load the whole response in memory**. For example if you want to download several gigabyte sized files, these methods will load all the data in memory. Instead you can use the `content` attribute. It is an instance of the `aiohttp.StreamReader` class. The `gzip` and `deflate` transfer-encodings are automatically decoded for you.

It is not possible to use `read()`, `json()` and `text()` after explicit reading from `content`.

Key Code:

```python
with open(filename, 'wb') as fd:
    while True:
        chunk = await resp.content.read(chunk_size)
        if not chunk:
            break
        fd.write(chunk)
```

Full Code:

```python
import aiohttp
import asyncio

async def fetch(session, url, filename, chunk_size):
    async with session.get(url) as resp:
        with open(filename, "wb") as fd:
            while True:
                chunk = await resp.content.read(chunk_size)
                if not chunk:
                    break
                fd.write(chunk)

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://api.github.com/events"
        filename = "myfile.txt"
        chunk_size = 10
        html = await fetch(session, url, filename, chunk_size)
        print(html)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

```

