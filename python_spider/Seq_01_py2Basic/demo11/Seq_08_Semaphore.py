# coding=utf-8
import multiprocessing
import time


def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + " acquire")
    time.sleep(i)
    print(multiprocessing.current_process().name + " release")
    s.release()


# 1、Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。
if __name__ == "__main__":
    s = multiprocessing.Semaphore(3)
    for i in range(9):
        p = multiprocessing.Process(target=worker, args=(s, i * 2))
        p.start()
