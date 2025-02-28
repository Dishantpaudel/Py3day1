import socket

host = "localhost"  # Using localhost for local testing
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print("Connected to server")

while True:
    message = input("You: ")
    sock.sendall(message.encode())
    
    data = sock.recv(1024)
    if not data:
        break
    print(f"Server: {data.decode()}")

sock.close()
