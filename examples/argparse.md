# argparse #

## 示例代码 ##

```python
import argparse

if __name__ == '__main__':
    # setup commandline arguments
    parser = argparse.ArgumentParser(description='mitmweb parameter')
    parser.add_argument('--host', action="store", dest="host", default='localhost')
    parser.add_argument('--port', action="store", dest="port", default=8081, type=int)

    # parse arguments
    given_args = parser.parse_args()
    server_ip = given_args.host
    server_port = given_args.port

    print("server host = {}, server port = {}".format(server_ip, server_port))
```

调用：

	python test07.py --host 192.168.80.105 --port 70

> 火影忍者里有一句话：努力是不会骗人的。