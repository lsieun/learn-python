#get请求方式2
import urllib.request

url = "http://www.baidu.com"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)

if response.status == 200:
    data = response.read()
    print(data.decode("utf-8"))
