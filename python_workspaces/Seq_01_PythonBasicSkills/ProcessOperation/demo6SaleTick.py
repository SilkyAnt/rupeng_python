#使用多线程模拟售票过程
#4个窗口，每个串口的排队人数变化的，窗口的名字就是窗口1，窗口2。。。
#总的票数是20张
#规定每个窗口每次只能卖出一张
import threading
import random
import time
counts = 20
lock = threading.Lock()
class saleTicks(threading.Thread):
    def __init__(self,name,waitNums,selfTime):
        threading.Thread.__init__(self)
        self.name = name
        self.waitNums = waitNums
        self.selfTime = selfTime
    def run(self):
        global counts,lock
        while counts and self.waitNums:
            #time.sleep(self.selfTime)
            lock.acquire()
            if counts >= 1:
                counts -= 1
                print("{}卖出火车票,余票{},当前窗口排队人数{}" .format(self.name,counts,self.waitNums))
                self.waitNums -= 1
                lock.release()
            else:
                print("{}没有卖出火车票,余票{}".format(self.name, counts))
                lock.release()
        print(self.name,self.waitNums)


windowsList = []
for t in range(4):
    windowsList.append(saleTicks("窗口"+str(t+1),random.randrange(2,10),random.randrange(2,5)))
print(windowsList)
for value in windowsList:
    print("{}等待总人数是：{}" .format(value.name,value.waitNums))

for t in windowsList:
    t.start()
