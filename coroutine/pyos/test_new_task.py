from system_call import SystemCall, GetTid, NewTask
from event_loop import EventLoop

def foo():
    __name__ = "foo"
    print("foo: enter...")
    print("foo: yield GetTid()")
    my_tid = yield GetTid()
    print("foo: my_tid = {}".format(my_tid))
    for _ in range(5):
        print("foo: I'm foo, taskid={}, index={}. yield".format(my_tid, _))
        yield

def main():
    __name__ = "main"
    print("main: enter...")
    print("main: yield GetTid()")
    my_tid = yield GetTid()
    print("main: my_tid = {}".format(my_tid))
    print("main: yield NewTask(foo())")
    child_tid = yield NewTask(foo())
    print("main: child_tid = {}".format(child_tid))
    for _ in range(10):
        print("main: I'm main, taskid={}, index={}. yield".format(my_tid, _))
        yield

if __name__ == "__main__":
    loop = EventLoop()
    loop.create_task(main())
    loop.mainloop()

