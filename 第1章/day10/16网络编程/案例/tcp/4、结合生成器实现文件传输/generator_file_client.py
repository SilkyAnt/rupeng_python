#1、导入包
import sys
import socket
client=None
def getClient():
    # 2、创建客户端的socket对象
    global  client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = socket.gethostname()
    # 3、绑定
    client.connect((host,9999))
    print("客户端连接上服务端:")
    return client
def sendFile():
    n=1
    global client
    getClient()
    for w in getFile("1.mp4"):
        client.sendall(w)
        print(n)
        n=n+1
    client.close()
#读取文件的生成器
def getFile(filename):
       f=open(filename,mode="rb")
       fc=f.read(1024*1000)
       f.flush()
       yield  fc
       while fc:
           fc=f.read(1024*1000)
           f.flush()
           yield fc
       f.close()
sendFile()

