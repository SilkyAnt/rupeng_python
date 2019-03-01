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
# senddata = "hello"
while True:
    senddata = input("请输入发送给服务端的信息：")
    socket_client.sendall(senddata.encode("utf-8"))
    if senddata == "quit":
        print("QQ Client Exit!")
        break
    print("客户端准备接收来自服务端的数据：")
    recvData = socket_client.recv(512)
    if recvData.decode("utf-8") == "quit":
        print("QQ Server Exit!QQ Client Exit!")
        break
    else:
        print("客户端接收来自服务端的数据：{}".format(recvData.decode("utf-8")))

socket_client.close()
