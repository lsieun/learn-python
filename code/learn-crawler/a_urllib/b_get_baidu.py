#get请求
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
if response.status == 200:
    data = response.read()
    print(type(data))
    print(data)
    print(data.decode("utf-8"))


