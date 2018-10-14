#encoding=utf-8
import socket
socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientHost=socket.gethostname()
socket_client.connect((clientHost,9999))
print("QQ客户端上线:")
while True:
  sendData=input("请输入发送到服务端的数据:")
  socket_client.send(sendData.encode("utf-8"))
  if sendData=='quit':
      print("QQ退出!")
      break
  print("准备接收来自服务端的信息：")
  revicedData=socket_client.recv(512)
  if revicedData.decode("utf-8")!='quit':
     print(revicedData.decode("utf-8"))
  else:
      print("对方已经退出，QQ退出!")
      break

socket_client.close()
