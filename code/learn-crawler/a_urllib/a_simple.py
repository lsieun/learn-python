import urllib.request
import urllib.parse

response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print(html.decode('utf-8'))