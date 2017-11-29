import urllib.parse
import urllib.request

url = 'http://www.baidu.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data.encode("utf-8"), headers)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf-8"))