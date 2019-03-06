#encoding=utf-8
#1、导入包
import  socket
#2、创建一个socket对象
socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print(socket1)
'''
<socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
当protocol为0时，会自动选择type类型对应的默认协议
fd 是(file descriptor)，这种一般是BSD Socket的用法，用在Unix/Linux系统上。
在Unix/Linux系统下，一个socket句柄，可以看做是一个文件，在socket上收发数据，
相当于对一个文件进行读写，
所以一个socket句柄，通常也用表示文件句柄的fd来表示。
'''
#3、获取本机的机器名
host=socket.gethostname()
#4、服务端绑定
socket_server.bind((host,9999))
#5、侦听
socket_server.listen(5)
print("服务器处于侦听状态......")
#6、服务端接收客户端的请求
serverSocket, addressinfo=socket_server.accept()
print("服务端接收来自{0}的{1}端口的连接请求".format(addressinfo[0],addressinfo[1]))
print("服务端准备接收数据:")
revicedData= serverSocket.recv(256)
print("服务端接收到的数据:")
print(revicedData.decode("utf-8"))
serverSocket.close()
socket_server.close()
print("服务端关闭")

