from socket import *
import threading

def handle_client(connectionSocket):
    try:
        # Menerima pesan dari client (user)
        # Contoh: "GET /index.html HTTP/1.1"
        message = connectionSocket.recv(1024).decode()
        
        # Cek jika message kosong (client menutup koneksi tiba-tiba)
        if not message:
            connectionSocket.close()
            return

        # Pecah string untuk mengambil filename
        parts = message.split()
        
        # Validasi apakah format request benar (minimal ada method dan path)
        if len(parts) >= 2:
            filename = parts[1] # Mengambil "/index.html"
            
            # Membuka file serta menghilangkan tanda "/" di depan
            # filename[1:] mengubah "/index.html" menjadi "index.html"
            f = open(filename[1:])
            
            # Membaca isi file
            outputdata = f.read()

            # Kirim response header ke client
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Kirim isi file html
            connectionSocket.sendall(outputdata.encode())
            
            # Tutup file setelah dibaca
            f.close()
        else:
            print("[WARN] Request tidak valid dari client.")

    except IOError:
        # Jika file tidak ditemukan (404)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        response = "<html><head></head><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.sendall(response.encode())
    
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")

    finally:
        # Pastikan koneksi selalu ditutup di akhir
        connectionSocket.close()

# Inisialisasi Server
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5) 

print(f"[SYSTEM] Server running on port {serverPort}...")

while True:
    # Menunggu koneksi masuk
    connectionSocket, addr = serverSocket.accept()
    print(f"[INFO] Terhubung dengan {addr}")

    # Membuat thread untuk menangani client secara paralel
    thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    thread.start()