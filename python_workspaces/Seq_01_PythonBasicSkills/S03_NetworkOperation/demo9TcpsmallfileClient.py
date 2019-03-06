# 使用TCP协议传输小文件到服务器
f = open("龙猫.jpg", mode="rb+")

fcontent = f.read()
print(len(fcontent))

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))
client.sendall(fcontent)
client.close()
