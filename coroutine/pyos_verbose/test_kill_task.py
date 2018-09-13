from system_call import GetTid, NewTask, KillTask
from event_loop import EventLoop
import time

def foo():
    print("foo: enter...")
    print("foo: yield GetTid()")
    my_tid = yield GetTid()
    print("foo: my_tid = {}".format(my_tid))
    count = 0
    while True:
        time.sleep(0.2)
        count += 1
        print("foo: in while loop {}".format(count))
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
    for _ in range(5):
        print("main: I'm in for loop. taskid = {}, index = {}.".format(my_tid, _))
        print("main: yield")
        yield

    print("main: yield KillTask(child_tid)")
    success = yield KillTask(child_tid)
    print("main: kill task success? {}".format(success))
    print("main: there is no yield, what's going to happen?")

if __name__ == "__main__":
    loop = EventLoop()
    loop.run_until_complete(main())

