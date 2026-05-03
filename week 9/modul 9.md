# MODUL 9 WEB SERVER

## Pengantar
Pada modul ini, kita akan mempelajari dasar-dasar pemrograman soket TCP menggunakan Python, mulai dari cara membuat soket, mengikatnya ke alamat dan port tertentu, hingga memahami format header HTTP untuk komunikasi data. Kita akan mengembangkan sebuah server web sederhana yang mampu menerima dan mengurai permintaan klien, mengambil file yang relevan dari sistem penyimpanan, serta mengirimkan respons balik yang menyertakan isi file tersebut. Jika dokumen yang diminta tidak tersedia, kita akan memprogram server agar secara otomatis mengirimkan pesan kesalahan "404 Not Found", dengan fokus operasional pada penanganan satu permintaan dalam satu waktu.

---

## Kode Python untuk Web Server yang Simple

### kode untuk server, ada di file saya "serversimpel.py"

```
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
```

Program server web dalam file **serversimpel.py** ini bekerja dengan memanfaatkan protokol TCP untuk menjalin komunikasi antara perangkat server dan browser. Proses dimulai dengan inisialisasi *socket* yang dikonfigurasi menggunakan **alamat IP host dan nomor port 8080**. Setelah dijalankan, program akan berada dalam fase *listening*, yaitu kondisi siaga untuk menunggu permintaan masuk dari jaringan. Begitu alamat IP server diakses melalui browser, server akan menerima koneksi dan membaca pesan HTTP *request* yang dikirimkan oleh browser tersebut.

Di dalam blok logika utama, dilakukan pembedahan teks pada pesan yang diterima untuk mengekstrak nama file yang diminta, yaitu **test.html**. Setelah nama file teridentifikasi, server akan mencari dan mencoba membuka file tersebut di direktori yang sama dengan lokasi file **serversimpel.py**. Jika file **test.html** tersedia, server akan mengirimkan respons balik berupa *header* status `HTTP/1.1 200 OK` yang diikuti dengan seluruh isi file agar browser dapat menampilkan halaman web secara utuh.

Namun, jika file tidak ditemukan atau terjadi kesalahan saat proses pembacaan, sistem secara otomatis akan menjalankan fungsi penanganan eksepsi dan mengirimkan pesan kesalahan `404 Not Found`. Setelah seluruh proses pengiriman data selesai, koneksi *socket* akan ditutup untuk membebaskan sumber daya sistem, kemudian server kembali ke mode siaga untuk menunggu permintaan berikutnya dari jaringan.

![eror8080](../week%209/assets/image/aksesfilelain.png)

### File HTML (test.html)

```
<html><body><h1>Test Page</h1></body></html>
```

Ketika client mengakses ```http://localhost:8080/test.html``` maka server akan membaca isi file nya dan mengirimkannya sebagai respons

### Outputnya

![berhasil8080](../week%209/assets/image/test.png)

---

## 9.6 LATIHAN TAMBAHAN
## MULTITHREAD WEB SERVER

Kode server.py yang merupakan pengembangan dari file serversimpel.py 

```
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
```

### Output server.py

![berhasil6789](../week%209/assets/image/output%20server.png)

![output6789](../week%209/assets/image/serverpy.png)

### KODE client.py

```
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
```

### Output client.py

![responclient6789](../week%209/assets/image/respon%20client.png)

Pengembangan pada file **server.py** kini telah mengadopsi konsep **Multithreading** untuk mengatasi keterbatasan server yang sebelumnya hanya mampu melayani satu permintaan dalam satu waktu. Dalam arsitektur yang baru, server memiliki satu *thread* utama yang bertugas secara khusus untuk mendengarkan (*listening*) koneksi masuk pada port 6789(port baru agar beda dgn yg simple). Begitu sebuah permintaan koneksi TCP diterima dari klien, server tidak akan memprosesnya di jalur utama, melainkan segera membentuk *thread* terpisah yang menjalankan fungsi `handle_client`. Hal ini memungkinkan terjadinya koneksi TCP yang independen untuk setiap pasangan permintaan dan respons, sehingga server mampu melayani banyak pengguna secara bersamaan tanpa harus membuat pengguna lain menunggu proses sebelumnya selesai.

Di sisi lain, pengujian server kini dilakukan menggunakan file **client.py** yang dirancang untuk mensimulasikan perilaku browser secara terprogram melalui baris perintah. Klien ini bekerja dengan menerima tiga argumen input, yaitu alamat IP atau *hostname* server, nomor port, dan nama file yang ingin diakses, seperti **index.html**. Setelah argumen tersebut diterima, **client.py** akan membangun koneksi TCP langsung ke arah server dan menyusun pesan permintaan HTTP menggunakan metode `GET` secara manual. Pesan tersebut kemudian dikirimkan melalui *socket*, dan klien akan menunggu respons balik dari server untuk ditampilkan seluruhnya sebagai *output* di terminal.

Interaksi antara **server.py** yang bersifat multithreaded dan **client.py** ini mencerminkan mekanisme dasar komunikasi jaringan yang efisien. Ketika klien meminta file **index.html**, *thread* khusus yang dibuat oleh server akan mencari file tersebut di direktori lokal; jika ditemukan, server mengirimkan kode status `200 OK` beserta isi dokumennya, dan jika tidak, server mengirimkan respons `404 Not Found`. Seluruh proses ini diakhiri dengan penutupan koneksi pada setiap *thread* untuk memastikan penggunaan sumber daya sistem tetap optimal, sementara *thread* utama pada **server.py** tetap berdiri siaga untuk menerima permintaan-permintaan baru dari jaringan.

## OUTPUT KETIKA AKSES FILE SALAH

![outputsalah](../week%209/assets/image/eror%20untuk%20latsol.png)