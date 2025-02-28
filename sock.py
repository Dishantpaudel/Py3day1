import socket



host="test.net"
port =80


sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
socket.send(b"GET / HTTP/1.1\r\n\n Host: test.net\r\n\r\n")
data =sock.rev(1024)
print(data)
sock.close()