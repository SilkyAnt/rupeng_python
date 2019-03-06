# 使用TCP协议传输大文件到服务器
import socket

client = None


def getTcpCliet():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clienthost = socket.gethostname()
    client.connect((clienthost, 9999))
    return client


def sendFile(filename, buffSize):
    getTcpCliet()
    f = open(filename, mode="rb")
    fcontent = f.read(1024 * 1024)
    n = 1
    while fcontent:
        client.sendall(fcontent)
        fcontent = f.read(buffSize)
        n = n + 1
    print(n)

    f.close()
    client.close()


sendFile("pycharm-professional-2018.2.1.exe", 1024 * 1024)
