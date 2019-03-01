import threading
import time

count = 2
# 锁的概念
lock = threading.Lock()


class saleTick(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global count
        # 加锁
        lock.acquire()
        if count >= 1:
            time.sleep(2)
            count -= 1
            print("{}我已经买到票了，余票是：{}".format(self.name, count))
        else:
            print("{}没有买到票，余票是：{}".format(self.name, count))
        # 解锁
        lock.release()


thread1 = saleTick("p1")
thread2 = saleTick("p2")
thread3 = saleTick("p3")
thread4 = saleTick("p4")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
