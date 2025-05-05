from socket import socket, AF_INET, SOCK_DGRAM
send_socket = socket(AF_INET, SOCK_DGRAM)
data = input('请输入要发送的数据：')
ip_port = ('127.0.0.1', 8888)
send_socket.connect(ip_port)
send_socket.sendto(data.encode('utf-8'),ip_port)
#接收来自接收方的数据
recv_data,addr = send_socket.recvfrom(1024)
print("接收到的数据为：",recv_data.decode('utf-8'))
send_socket.close()