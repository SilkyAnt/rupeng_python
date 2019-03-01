# 装饰器是把一个函数作为参数的函数
# 常常用于扩展已有函数,即不改变当前函数状态下增加功能
import time


def countTime(f):
    def wrapper(*args, **kwargs):
        begin = time.time()
        f(*args, **kwargs)
        end = time.time()
        print(end - begin)

    return wrapper


@countTime
def forDemo():
    for i in range(1, 10000):
        for j in range(1, 10000):
            pass


forDemo()
