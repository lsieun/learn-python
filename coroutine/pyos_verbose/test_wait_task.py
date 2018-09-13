from system_call import GetTid, NewTask, WaitTask
from event_loop import EventLoop
import time

def foo():
    print("foo: enter...")
    print("foo: yield GetTid()")
    my_tid = yield GetTid()
    print("foo: my_tid = {}".format(my_tid))
    count = 0
    for _ in range(3):
        time.sleep(0.2)
        count += 1
        print("foo: in for loop {}".format(count))
        print("foo: yield")
        yield

def main():
    print("main: enter...")
    print("main: yield GetTid()")
    my_tid = yield GetTid()
    print("main: my_tid = {}".format(my_tid))
    print("main: yield NewTask(foo())")
    child_tid = yield NewTask(foo())
    print("main: child = {}".format(child_tid))

    print("main: yield WaitTask(child_tid)")
    success = yield WaitTask(child_tid)
    print("main: done")

if __name__ == "__main__":
    loop = EventLoop()
    loop.run_until_complete(main())

