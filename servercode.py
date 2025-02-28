import socket

HOST = '0.0.0.0'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST, PORT))
    sock.listen(1)
except:
    print("Error binding to port")
    exit(1)

print("Server started, waiting for connection...")

conn, addr = sock.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Client: {data.decode()}")

    message = input("You: ")
    conn.sendall(message.encode())

conn.close()
sock.close()
