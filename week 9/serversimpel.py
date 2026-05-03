from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 8080))
serverSocket.listen(5)

print('Serversimpel ready on port 8080...')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Client: {addr}")
    
    try:
        message = connectionSocket.recv(1024).decode()
        parts = message.split()
        
        if len(parts) < 2:
            connectionSocket.send("HTTP/1.1 400 Bad Request\r\n\r\n".encode())
        else:
            filename = parts[1][1:]
            try:
                f = open(filename, 'r')
                data = f.read()
                f.close()
                connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
                connectionSocket.sendall(data.encode())
            except:
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>".encode())
                
    except Exception as e:
        print(f"Error: {e}")
    
    connectionSocket.close()