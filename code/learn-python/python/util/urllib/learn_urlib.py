#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#urllib
#from urllib import request,parse
#3.x的标准写法
import urllib.request
import urllib.parse
#from bs4 import BeautifulSoup

#百度首页
url = "http://www.baidu.com"
#发起request请求，得到返回对象
resp = urllib.request.urlopen(url)
if resp.status == 200:
    print("访问成功")
    #获取成功
    #data = resp.read()#原生格式
    data = resp.read().decode("utf-8")#解析之后的格式
    print(data)
    #soup = BeautifulSoup(data)#未能找到BeautifulSoup的包
    #print(soup.title)#获取标签和里面的值
    #print(soup.title.string)#只获取标签里的值



