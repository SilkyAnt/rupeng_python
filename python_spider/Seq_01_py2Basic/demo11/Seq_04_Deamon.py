# coding=utf-8
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


"""
在这里，调用的时候增加了设置deamon，最后的主进程（即父进程）打印输出了一句话。
运行结果：Main process Ended!结果很简单，因为主进程没有做任何事情，直接输出一句话结束，
所以在这时也直接终止了子进程的运行。这样可以有效防止无控制地生成子进程。
如果这样写了，你在关闭这个主程序运行时，就无需额外担心子进程有没有被关闭了。
不过这样并不是我们想要达到的效果呀，能不能让所有子进程都执行完了然后再结束呢？
那当然是可以的，只需要加入join()方法即可。
"""

if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()
    print 'Main process Ended!'
