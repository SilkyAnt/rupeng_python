import time
#未使用多线程
def showTime(name,delayTime):
    count = 1
    while count<= 6:
        time.sleep(delayTime)
        count = count + 1
        print("执行体的名字{},当前时间{}" .format(name,time.ctime(time.time())))

#执行如下四个方法需要的时间是：(1+2+3+4)*6=60 秒
showTime("showTime1",1)
showTime("showTime2",2)
showTime("showTime3",3)
showTime("showTime4",4)
