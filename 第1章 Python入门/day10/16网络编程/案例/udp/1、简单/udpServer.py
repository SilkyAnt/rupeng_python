#encoding=utf-8
#1������ģ��
import socket
#2������һ��socket
udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#print(udpSocket)
#3���󶨷������׽���
udpSocket.bind(("127.0.0.1",9999))
#4������/��������
data, address_info=udpSocket.recvfrom(512)
print(data.decode("utf-8"))
#5���ر�
udpSocket.close()