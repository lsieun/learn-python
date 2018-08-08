
```python
import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
socket.socket = socks.socksocket

url = "https://httpbin.org/get"

r = requests.get(url)
status_code = r.status_code
print(status_code)
txt = r.text
print(txt)

```