from socket import *
import sys

# Cek argumen command line
if len(sys.argv) != 4:
    print("Usage: python client.py <server> <port> <file>")
    print("Example: python client.py localhost 6789 index.html")
    sys.exit(1)

server_host = sys.argv[1]
server_port = int(sys.argv[2])
file_path = sys.argv[3]

# Buat socket dan connect
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))

# Buat HTTP GET request
request = f"GET /{file_path} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"

# Kirim request
clientSocket.send(request.encode())

# Terima response
response = clientSocket.recv(4096).decode()

# Tampilkan response
print("RESPONSE:")
print("-" * 50)
print(response)

clientSocket.close()