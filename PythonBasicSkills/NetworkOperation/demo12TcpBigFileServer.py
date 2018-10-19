import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverhost = socket.gethostname()
server.bind((serverhost,9999))
server.listen(5)
socketobject,addressinfo=server.accept()
fnew = open("new.exe",mode="wb")
recvdata = socketobject.recv(1024 * 1024)
while recvdata:
    fnew.write(recvdata)
    recvdata = socketobject.recv(1024 * 1024)
fnew.close()
socketobject.close()
server.close()