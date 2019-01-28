# coding=utf-8
import multiprocessing
import time


def worker_with(lock, f):
    fs = open(f, "a+")
    fs.write('Lock acquired via with\n')
    fs.write('1\n')
    time.sleep(1)
    fs.write('2\n')
    fs.write('3\n')
    fs.close()


def read_file(f, lock):
    fs = open(f, "r")
    print(fs.read())


# 你会发现，会出现读取的文件的内容和文件中的内容不一致，这是因为，
# 当写进程还没写完，读进程就开始读取文件了。所以，要加一把锁，
# 只有写进程对文件操作完毕，才可以让读进程读取文件
if __name__ == "__main__":
    f = "file.txt"
    lock = multiprocessing.Lock()
    w = multiprocessing.Process(target=worker_with, args=(lock, f))
    w.start()
    r = multiprocessing.Process(target=read_file, args=(f, lock))
    r.start()
    w.join()
    r.join()
