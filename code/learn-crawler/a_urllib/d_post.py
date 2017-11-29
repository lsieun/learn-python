import urllib.request
import urllib.parse

values = {"name":"张三","age":"10"}
encodeValues = urllib.parse.urlencode(values)
url = "http://www.baidu.com"
req = urllib.request.Request(url,encodeValues.encode("utf-8"))
response = urllib.request.urlopen(req)

if response.status == 200:
    data = response.read()
    print(data.decode("utf-8"))