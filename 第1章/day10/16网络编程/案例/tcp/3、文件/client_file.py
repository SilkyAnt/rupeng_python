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

def getFile(filename):
       getClient()
       n=0
       f=open(filename,mode="rb")
       fc=f.read(1024*1000)
       f.flush()
       print("客户端发送文件:")
       global client
       client.sendall(fc)
       while fc:
           fc=f.read(1024*1000)
           f.flush()
           n=n+1
           client.sendall(fc)
           print(n)

       client.close()


getFile("1.mp4")