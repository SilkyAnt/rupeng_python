'''
1、导入模块
2、创建一个scoket对象
3、绑定服务器嵌套字
4、接收/发送数据
5、关闭
'''

import socket
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostname = socket.gethostname()
udp_server.bind(("127.0.0.1",9999))
while True:
    print("Two方准备接收数据：")
    data,address_info = udp_server.recvfrom(512)
    if data.decode("utf-8")=="quit":
        print("Two 方也退出聊天")
        break
    print(data.decode("utf-8"))

    senddata = input("请输入发送给One的信息：")
    udp_server.sendto(senddata.encode("utf-8"), ("127.0.0.1", 19999))
udp_server.close()