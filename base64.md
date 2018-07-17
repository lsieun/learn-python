
## Base64 ##

```python
import base64

# 加密
origin_str = "你好"
data = origin_str.encode("UTF8")
encoded_bytes = base64.b64encode(data)
base64_str = encoded_bytes.decode("UTF8")
print(base64_str) # 5L2g5aW9

# 解密
data = base64_str.encode("UTF8")
decoded_bytes = base64.b64decode(data)
dest_str = decoded_bytes.decode("UTF*")
print(dest_str) # 你好
```

