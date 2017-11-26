import threading

def run1():
    print("我是一个线程。。。")

#(1)创建一个线程，需要指定线程运行的方法，并且给一个名称
thread1 = threading.Thread(target=run1,name="线程1")
#(2)创建完线程之后,一定要启动
thread1.start()