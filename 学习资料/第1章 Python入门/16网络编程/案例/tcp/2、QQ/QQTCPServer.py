#encoding=utf-8
#1、导入包
import  socket
#2、创建一个socket对象
socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3、获取本机的机器名
host=socket.gethostname()
#4、服务端绑定
socket_server.bind((host,9999))
#5、侦听
socket_server.listen(5)
print("QQ服务端启动......")
#6、服务端接收客户端的请求
serverSocket, addressinfo=socket_server.accept()
print("服务端接收来自{0}的{1}端口的连接请求".format(addressinfo[0],addressinfo[1]))
while True:
   print("准备接收来自客户端的信息：")
   revicedData= serverSocket.recv(256)
   if revicedData.decode("utf-8")!='quit':
       print(revicedData.decode("utf-8"))
   else:
       print("对方已经退出，QQ退出!")
       break
   sendData=input("请输入发送给客户端的信息:")
   serverSocket.sendall(sendData.encode("utf-8"))
   if sendData=='quit':
       print("QQ退出")
       break

serverSocket.close()
socket_server.close()


