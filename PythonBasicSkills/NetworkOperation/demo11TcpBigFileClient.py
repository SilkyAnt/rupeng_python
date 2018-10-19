#使用TCP协议传输大文件到服务器
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clienthost = socket.gethostname()
client.connect((clienthost,9999))

f = open("pycharm-professional-2018.2.1.exe",mode="rb")
fcontent = f.read(1024*1024)
n = 1
while fcontent:
    client.sendall(fcontent)
    fcontent = f.read(1024*1024)
    n = n + 1
print(n)

f.close()
client.close()