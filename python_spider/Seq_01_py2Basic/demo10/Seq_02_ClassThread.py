# encoding=utf-8
# 使用类包装的方法来创建多线程对象
import threading
import time
import sys


class Self_Thread(threading.Thread):
    def __init__(self, threadName, delay):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.delay = delay

    def run(self):
        count = 0
        while count < 5:
            time.sleep(self.delay)
            count += 1
            print("%s:%s" % (self.threadName, time.ctime(time.time())))


thread01 = Self_Thread("thread01", 3)
thread02 = Self_Thread("thread02", 7)
thread03 = Self_Thread("thread03", 11)
threads = []
threads.append(thread01)
threads.append(thread02)
threads.append(thread03)
for t in threads:
    t.start()
for t in threads:
    t.join()

'''
thread01.start()
thread02.start()
thread03.start()
#join:主线程等待对应线程执行完毕
thread01.join()
thread02.join()
thread03.join()
'''
