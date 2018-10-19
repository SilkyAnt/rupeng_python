#encoding=utf-8
import sys
import socket
#2、创建服务端的socket对象
service=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host=socket.gethostname()
#3、绑定
service.bind((host,9999))
#4、设置侦听，其中5表示最大连接数
service.listen(5)
T=1
#5、接收连接
print("服务端启动：")
serviceSocket,addr=service.accept()
f = open("czf.mp4", mode="ab+")
while True:
    print("客户端地址:%s" %str(addr))
    print("服务端接收文件：")
    fileContent=serviceSocket.recv(1024*1000)
    print(len(fileContent))
    f.write(fileContent)
    f.flush()
    if len(fileContent)==0:
        f.close()
        break



