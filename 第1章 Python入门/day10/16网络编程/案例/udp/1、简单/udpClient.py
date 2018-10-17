  #encoding=utf-8
#1、导入模块
import  socket
#2、创建一个socket对象
udpclient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#3、向服务器端发送数据
serverHost=("127.0.0.1",9999)
udpclient.sendto("hello".encode("utf-8"),serverHost)
#4、关闭
udpclient.close()