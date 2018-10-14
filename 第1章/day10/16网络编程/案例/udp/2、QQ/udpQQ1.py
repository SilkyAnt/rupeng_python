#encoding=utf-8
#1、导入模块
import  socket
#2、创建一个socket对象
udpclient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#3、向服务器端发送数据
serverHost=("127.0.0.1",9999)
#绑定客户端，用来接收服务端的数据
clientHost=("127.0.0.1",19999)
udpclient.bind(clientHost)
print("QQ聊天程序启动：")
while True:
     send_data=input("请输入聊天内容:")
     udpclient.sendto(send_data.encode("utf-8"),serverHost)
     if send_data=='quit':
         print("退出QQ")
         break
     print("客户端接收到的数据：")
     reciveData,address_infro=udpclient.recvfrom(512)
     if reciveData.decode("utf-8")!='quit':
        print(reciveData.decode("utf-8"))
     else:
         print("退出QQ")
         break
#4、关闭
udpclient.close()