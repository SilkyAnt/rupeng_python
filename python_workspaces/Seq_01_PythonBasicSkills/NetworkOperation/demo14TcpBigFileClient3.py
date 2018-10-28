#使用TCP协议传输大文件到服务器   利用生成器
import socket
import time
client = None
f = None

def getTcpCliet():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clienthost = socket.gethostname()
    client.connect((clienthost, 9999))
    return client

def sendFile(filename,buffSize):
    getTcpCliet()
    global f
    f = open(filename,mode="rb")
    fcontent = f.read(1024*1024)
    yield fcontent
    n = 1
    while fcontent:
        #client.sendall(fcontent)
        fcontent = f.read(buffSize)
        yield fcontent
        n = n + 1
        #print(n)

def closeAll():
    f.close()
    client.close()

beginTime = time.time()
for w in sendFile("pycharm-professional-2018.2.1.exe",1024*1024):
    client.sendall(w)
closeAll()
endTime = time.time()
print(endTime-beginTime)