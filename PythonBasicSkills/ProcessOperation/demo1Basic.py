import threading
print(threading.current_thread())
print(threading.current_thread().getName())
print(threading.current_thread().isAlive())
print(threading.current_thread().isDaemon())
print(threading.activeCount())

print(threading.enumerate())
for l in threading.enumerate():
    print(l.getName())
