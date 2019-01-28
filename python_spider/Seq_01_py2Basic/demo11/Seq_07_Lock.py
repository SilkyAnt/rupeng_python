import multiprocessing
import time


def worker_with(lock, f):
    try:
        lock.acquire()
        fs = open(f, "a+")
        fs.write('Lock acquired via with\n')
        fs.write('1\n')
        time.sleep(1)
        fs.write('2\n')
        fs.write('3\n')
        fs.close()
    finally:
        lock.release()


def read_file(f, lock):
    try:
        lock.acquire()
        fs = open(f, "r")
        print(fs.read())
    finally:
        lock.release()


if __name__ == "__main__":
    f = "file.txt"
    lock = multiprocessing.Lock()
    w = multiprocessing.Process(target=worker_with, args=(lock, f))
    w.start()
    r = multiprocessing.Process(target=read_file, args=(f, lock))
    r.start()
    w.join()
    r.join()
