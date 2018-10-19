import time
import threading
def showTime(name,delayTime):
    count = 1
    while count<= 6:
        time.sleep(delayTime)
        count = count + 1
        print("执行体的名字{},当前时间{}" .format(name,time.ctime(time.time())))
'''
#执行如下四个方法需要的时间是：(1+2+3+4)*6=60 秒
showTime("showTime1",1)
showTime("showTime2",2)
showTime("showTime3",3)
showTime("showTime4",4)
'''

#用多线程的方法执行
class myThread(threading.Thread):
    def __init__(self,name,delayTime):
        threading.Thread.__init__(self)
        self.name = name
        self.delayTime = delayTime
    def run(self):
        print("{}多少线程开始执行" .format(self.name))
        showTime(self.name,self.delayTime)
        print("{}多线程执行结束" .format(self.name))

myThread1 = myThread("showTime1",1)
myThread2 = myThread("showTime2",2)
myThread3 = myThread("showTime3",3)
myThread4 = myThread("showTime4",4)

myThread1.start()
myThread2.start()
myThread3.start()
myThread4.start()