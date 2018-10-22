# 1、导入socket模块
import socket
# 2、创建一个socket对象
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 3、绑定
serversocket.bind(("localhost",9999))
# 4、监听
serversocket.listen(2)
print("web server start,IP:localhost,port:9999")
print(serversocket)

# 5、接受来自客户端的请求
while True:
    # 服务端接受来自客户端的请求
    socket_object,address_info = serversocket.accept()
    request = socket_object.recv(1024)
    print(request)

    http_response = """\
HTTP/1.1 200 OK

Hello, World! 
"""

    # 6、服务端给客户端的响应
    socket_object.sendall(http_response.encode(encoding="utf-8"))
    socket_object.close()