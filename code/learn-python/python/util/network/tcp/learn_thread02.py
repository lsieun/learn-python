import threading


def run2(param1,param2):
    print("我是一个线程。。。" + param1)

#创建一个线程，需要指定线程运行的方法，并且给一个名称
#可以根据需求给定参数
thread2 = threading.Thread(target=run2,name="线程2",args=("123","456"))
thread2.start()