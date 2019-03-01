import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9999))
server.listen(5)
socketobject, addressinfo = server.accept()
data = socketobject.recv(3 * 1024 * 1024)

f2 = open("new.jpg", mode="wb+")
f2.write(data)
f2.close()
socketobject.close()
server.close()
