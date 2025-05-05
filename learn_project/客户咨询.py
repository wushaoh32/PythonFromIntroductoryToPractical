from socket import socket, AF_INET, SOCK_DGRAM
send_socket = socket(AF_INET, SOCK_DGRAM)
#多次通信
while True:
    data = input("客户说：")
    ip_port = ('127.0.0.1', 8887)
    #数据已经发送
    send_socket.sendto(data.encode('utf-8'), ip_port)
    if data == 'bye':
        break
    #等待和接收来自客服人员的回复
    #recvfrom是一个方法，通常用于从UDP套接字中接收数据
    recv_data,addr = send_socket.recvfrom(1024)
    print("客服回：",recv_data.decode('utf-8'))

send_socket.close()