"""
1、导入模块
2、创建一个scoket对象
3、获取本机的机器名
4、服务端绑定
5、侦听
6、服务端接/发数据
7、关闭
"""

import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket_client)
serverHost = socket.gethostname()
# print(hostname)
socket_server.bind((serverHost, 9999))
socket_server.listen()
print("服务端启动侦听。。。")
socket_object, address_info = socket_server.accept()  # 阻塞状态，一直等到
while True:
    # print("服务端接收来自客户端的请求。。。")
    receivedata = socket_object.recv(512)
    if receivedata.decode("utf-8") != "quit":
        print("服务端接收的数据：", receivedata.decode("utf-8"))
        senddata = input("请输入发送给客户端的数据：")
        socket_object.sendall(senddata.encode("utf-8"))
        if senddata == "quit":
            print("QQ Server Exit!")
            break
        else:
            print("服务端准备接收的数据：")
    else:
        print("QQ Server Exit!")
        break
    # print("客户端的地址是：{},端口是：{}" .format(address_info[0],address_info[1]))
socket_object.close()
socket_server.close()
