  #encoding=utf-8
#1������ģ��
import  socket
#2������һ��socket����
udpclient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#3����������˷�������
serverHost=("127.0.0.1",9999)
udpclient.sendto("hello".encode("utf-8"),serverHost)
#4���ر�
udpclient.close()