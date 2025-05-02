"""
1、使用socket类创建一个套接字对象
2、使用bind((ip,port))方法绑定ip地址和端口号
3、listen()方法开始TCP监听
4、使用accept方法等待客户端的连接
5、使用recv()/send()方法接受/发送数据
6、使用close()关闭套接字
"""
#1、使用socket类创建一个套接字对象，inet表示进程通信，stream表示tcp协议
from socket import socket, AF_INET, SOCK_STREAM
server_socket  = socket(AF_INET, SOCK_STREAM)
#2、使用bind((ip,port))方法绑定ip地址和端口号
ip = '127.0.0.1'
port = 8888
server_socket.bind((ip, port))
#3、listen()方法开始TCP监听
server_socket.listen(5)
print('服务器已启动')
#4、使用accept方法等待客户端的连接
client_socket,client_addr = server_socket.accept()
#5、使用recv()/send()方法接受/发送数据
data = client_socket.recv(1024)
print('客户端发送过来的数据为：',data.decode('utf-8'))
#6、使用close()关闭套接字
server_socket.close()