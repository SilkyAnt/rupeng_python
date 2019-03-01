"""
1、导入模块
2、创建一个scoket对象
3、得到客户端主机名字
4、连接服务端
5、收发数据
6、关闭
"""

import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket_client)
hostname = socket.gethostname()
# print(hostname)
socket_client.connect((hostname, 9999))
senddata = "hello"
socket_client.sendall(senddata.encode("utf-8"))
socket_client.close()
