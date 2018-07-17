
## MD5 ##

```python
import hashlib

origin_str = "你好"
data = origin_str.encode("UTF8")
md5_str = hashlib.md5(data).hexdigest()
print(md5_str)
```


