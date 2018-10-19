'''
1、导入模块
2、创建一个scoket对象
3、获取本机的机器名
4、服务端绑定
5、侦听
6、服务端接/发数据
7、关闭
'''

import socket
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(socket_client)
serverHost = socket.gethostname()
# print(hostname)
socket_server.bind((serverHost,9999))
socket_server.listen()
print("服务端启动侦听。。。")
socket_object,address_info = socket_server.accept()      #阻塞状态，一直等到
print("服务端接收来自客户端的请求。。。")
receivedata = socket_object.recv(512)
print("服务端接受的数据：",receivedata.decode("utf-8"))
print("客户端的地址是：{},端口是：{}" .format(address_info[0],address_info[1]))
socket_object.close()
socket_server.close()