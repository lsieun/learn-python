# aiohttp server

URL: https://aiohttp.readthedocs.io/en/stable/web_quickstart.html

## Getting Started

A **request handler** must be a `coroutine` that accepts a `Request` instance as its only parameter and returns a `Response` instance:

```python
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")
```

Next, create an `Application` instance and register the request handler on a particular HTTP method and path:

```python
app = web.Application()
app.add_routes([web.get('/', hello)])
```

After that, run the application by run_app() call:

```python
web.run_app(app)
```

That’s it. Now, head over to `http://localhost:8080/` to see the results.

Full Code:

```python
#!/usr/bin/env python3
# Last modified: 2018-08-24 12:19:37
from aiohttp import web

async def handle(request: web.Request) -> web.Response:
    method = request.method
    text = "Hello World - {}".format(method)
    return web.Response(text=text)

def main():
    app = web.Application()
    app.add_routes([
        web.get("/", handle)
    ])
    web.run_app(app)

if __name__ == '__main__': 
    main()

```

## Response

### Response: json data

It is a common case to return `JSON` data in response, `aiohttp.web` provides a shortcut for returning JSON – `aiohttp.web.json_response()`:

```python
#!/usr/bin/env python3
# Last modified: 2018-08-24 12:42:34
from aiohttp import web

async def handle(request: web.Request):
    data = {"some": "data"}
    return web.json_response(data)

def main():
    app = web.Application()
    app.add_routes([
        web.get("/", handle)
    ])
    web.run_app(app)

if __name__ == '__main__': 
    main()

```

## Request

### Request: form data

index.html

```html
<form action="http://localhost:8080/login" method="post" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

    <label for="login">Login</label>
    <input id="login" name="login" type="text" value="" autofocus/>
    <label for="password">Password</label>
    <input id="password" name="password" type="password" value=""/>

    <input type="submit" value="login"/>
</form>
```

Full Code:

```python
#!/usr/bin/env python3
# Last modified: 2018-08-24 12:58:04
from aiohttp import web

async def do_login(request: web.Request) -> web.Response:
    data = await request.post()
    login = data["login"]
    password = data["password"]
    text = "Hello {}, your password is {}".format(login, password)
    return web.Response(text = text)

def main():
    app = web.Application()
    app.add_routes([
        web.post("/login", do_login)
    ])
    web.run_app(app)

if __name__ == '__main__': 
    main()

```

## Routes

**Wildcard(通配符) HTTP method** is also supported by `route()` or `RouteTableDef.route()`, allowing **a handler** to serve incoming requests on a path having **any HTTP method**:

```python
app.add_routes[web.route('*', '/path', all_handler)]
```

### 第一种注册路由的方式 + variable path

```python
#!/usr/bin/env python3
# Last modified: 2018-08-24 10:32:37
from aiohttp import web

async def handle(request: web.Request) -> web.Response:
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, {}".format(name)
    return web.Response(text=text)

if __name__ == '__main__': 
    app = web.Application()
    app.add_routes([
        web.get("/", handle),
        web.get("/{name}", handle)
    ])

    web.run_app(app)

```

### 第二种注册路由的方式

```python
#!/usr/bin/env python3
# Last modified: 2018-08-24 10:44:18
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def handle(request: web.Request) -> web.Response:
    return web.Response(text="Hello World :)")

def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__': 
    main()

```


handler
application: routes -> handler
web.run_app











