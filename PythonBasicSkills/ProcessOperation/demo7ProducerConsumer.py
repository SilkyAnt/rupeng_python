import threading
import time

condition = threading.Condition()
products = 2
class Producer(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        while 1:
            global condition,products
            condition.acquire()
            if products < 6:
                products += 1
                print("{}生产一个产品，产品总数为{}" .format(self.name,products))
                #我已经生产出一个产品,通知你来消费
                condition.notify()
            else:
                print("产品总数够用，{}暂时不生产" .format(self.name))
                #等待消费者来消费产品
                condition.wait()
            condition.release()
            time.sleep(2)

class Consumer(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        while 1:
            global condition, products
            condition.acquire()
            if products > 1:
                products -= 1
                print("{}消费了一个产品，产品总数为{}" .format(self.name,products))
                #通知生产者，我已经消费一个产品
                condition.notify
            else:
                print("产品总数{}不足，{}暂时停止消费" .format(products,self.name))
                #产品不足，等待对方去生产产品
                condition.wait()
            condition.release()
            time.sleep(3)

p1 = Producer("P1")
p2 = Producer("P2")
p1.start()
p2.start()

c1 = Consumer("C1")
c2 = Consumer("C2")
c3 = Consumer("C3")
c4 = Consumer("C4")
c5 = Consumer("C5")
c6 = Consumer("C6")
c7 = Consumer("C7")
c8 = Consumer("C8")
c9 = Consumer("C9")
c10 = Consumer("C10")
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
c7.start()
c8.start()
c9.start()
c10.start()