# Linux Python3.6.4安装 #

## 1、下载  ##

	https://www.python.org/downloads/source/

## 2、解压 ##

	tar -zxvf Python-3.6.4.tgz

## 3、准备编译环境 ##

	yum install gcc

## 4、准备安装依赖包  ##

python的pip需要依赖这两个包：zlib、openssl。

	yum install zlib* openssl*

## 5、预编译 ##

	./configure --prefix=/usr/local/Python-3.6.4 --enable-optimizations

## 6、编译 ##

	make 

## 7、安装 ##

	make install

## 8、配置系统环境变量 ##

	vi ~/.bashrc 

内容如下：

	PYTHON_HOME=/usr/local/Python-3.6.4
	PATH=$PATH:$PYTHON_HOME/bin

重新加载配置文件：

	source ~/.bashrc

注意：

	/etc/profile：整个系统的环境变量配置文件
	~/.bashrc：当前用户的环境变量配置文件

进行python shell

	python3

退出python

	exit()



## 9、安装IPython ##

	pip3 install ipython

> 至此结束
