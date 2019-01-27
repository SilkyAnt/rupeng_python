# -*- coding: UTF-8 -*-
import thread
import sys
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 3,))
    thread.start_new_thread(print_time, ("Thread-2", 7,))
    thread.start_new_thread(print_time, ("Thread-3", 11,))
except:
    print("Error: unable to start thread")
    print(sys.exc_info()[0])
    sys.exit(0)

# 下面这两行还不能删掉，这是让主线程一直在等待，如果删掉，程序直接退出
while 1:
    pass
