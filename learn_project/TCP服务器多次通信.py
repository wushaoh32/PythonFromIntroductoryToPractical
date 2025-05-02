from socket import socket, AF_INET, SOCK_STREAM
#创建TCP套接字对象
socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.bind(('127.0.0.1',8888))
socket_obj.listen(5)
print("服务器启动成功，等待接收数据")
"""
等待客户端的TCP连接,系列解包赋值，第一个是客户端的对象，第二个是客户端的地址
当服务器监听到客户端的连接请求并建立连接后，方法accept返回两个值
第一个值代表与客户端通信的套接字对象，即client_socket
变量名和客户端不一定一样
"""
clientSocket,clientAddr = socket_obj.accept()
#接收数据
info = clientSocket.recv(1024).decode('utf-8')
#检查是否结束
while info.strip() !='bye':
        if info!='':
            print('接收到的数据是：',info)
        #准备发送的数据（服务器）
        data = input('请输入要发送的数据：')
        #这句代码：数据编好，已经发出去了
        clientSocket.send(data.encode('utf-8'))
        #然后再判断是否需要关闭服务器
        if data == 'bye':
            break

#关闭socket对象
clientSocket.close()
socket_obj.close()