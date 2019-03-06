#encoding=utf-8
#1、导入模块
import socket
#2、创建一个socket
udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#print(udpSocket)
#3、绑定服务器套接字
udpSocket.bind(("127.0.0.1",9999))
#4、接收/发送数据
data, address_info=udpSocket.recvfrom(512)
print(data.decode("utf-8"))
#5、关闭
udpSocket.close()