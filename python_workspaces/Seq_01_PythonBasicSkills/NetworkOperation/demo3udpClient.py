'''
1、导入模块
2、创建一个scoket对象
3、向服务端发送数据
4、关闭
'''
import socket
udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sendData = "hello"
udp_client.sendto(sendData.encode("utf-8"),("127.0.0.1",9999))
udp_client.close()


