# encoding=utf-8
import Queue

queue = Queue.LifoQueue(10)
print(queue.maxsize)
queue.put("a")
queue.put("b")
queue.put("c")
queue.put("d")
while not queue.empty():
    print(queue.get())
