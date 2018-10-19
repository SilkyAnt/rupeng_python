'''
1、导入模块
2、创建一个scoket对象
3、向服务端发送数据
4、关闭
'''
import socket
udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_client.bind(("127.0.0.1",19999))

while True:
    sendData = input("请输入你要向Two发送的信息：")
    udp_client.sendto(sendData.encode("utf-8"),("127.0.0.1",9999))
    if sendData == "quit":
        print("One方退出聊天")
        break
    print("准备接收来自Two方的数据：")
    data,address_info = udp_client.recvfrom(512)
    print("接收来自Two放的数据{}" .format(data.decode("utf-8")))
udp_client.close()


