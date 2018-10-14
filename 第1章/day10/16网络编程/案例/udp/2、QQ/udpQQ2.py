#encoding=utf-8
#1、导入模块
import socket
#2、创建一个socket
udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#print(udpSocket)
#3、绑定服务器套接字
udpSocket.bind(("127.0.0.1",9999))
#4、接收/发送数据
print("QQ聊天程序启动：")
clientHost=("127.0.0.1",19999)
while True:
    data, address_info=udpSocket.recvfrom(512)
    if data.decode("utf-8")!='quit':
       print("服务端接收到的数据：")
       print(data.decode("utf-8"))
       sendData=input("请输入服务端发送给客户端的数据")
       udpSocket.sendto(bytes(sendData.encode("utf-8")),clientHost)
       if sendData=='quit':
           print("关闭QQ聊天程序!")
           break
    else:
        print("关闭QQ聊天程序!")
        break

#5、关闭
udpSocket.close()