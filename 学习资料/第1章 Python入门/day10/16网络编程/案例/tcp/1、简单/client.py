#encoding=utf-8
import socket
socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientHost=socket.gethostname()
print("客户端准备连接服务端")
socket_client.connect((clientHost,9999))
print("客户端连上服务端")
sendData="Hello"
socket_client.send(sendData.encode("utf-8"))
print("客户端发送数据：{0}".format(sendData))
socket_client.close()
print("客户端关闭")