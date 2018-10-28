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
data,address_info = udp_server.recvfrom(512)
print(data.decode("utf-8"))
udp_server.close()