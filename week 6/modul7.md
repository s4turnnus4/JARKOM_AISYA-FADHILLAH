# SOCKET PROGRAMMING: MEMBUAT APLIKASI JARINGAN 

## Tujuan Praktikum

1. Mahasiswa bisa membuat program berbasis socket UDP
2. Mahasiswa bisa membuat program berbasis socket TCP

### Virtual envirounment
![ngecek py dan membuat folder VE](../week%206/assets/image/jarkom1.png)
![hasil foldernya](../week%206/assets/image/jarkom2.png)
![script](../week%206/assets/image/script.png)
![untuk eror authorize](../week%206/assets/image/untuk%20eror%20authorize.png)

### Mekanisme Pengalamatan Paket
Dalam komunikasi jaringan, pengiriman data memerlukan identitas yang sangat spesifik agar tidak salah sasaran:

1.  **Alamat IP sebagai Penunjuk Host:** Alamat IP tujuan merupakan bagian dari paket yang memungkinkan router di Internet mengarahkan data melintasi berbagai jaringan hingga mencapai komputer (host) target.
2.  **Nomor Port sebagai Penunjuk Soket:** Karena satu komputer dapat menjalankan banyak aplikasi sekaligus, alamat IP saja tidak cukup. Diperlukan **nomor port** untuk mengidentifikasi soket (pintu masuk) spesifik dari aplikasi yang sedang berjalan.
3.  **Struktur Alamat Lengkap:** Paket yang dikirimkan selalu melampirkan alamat tujuan (IP dan Port tujuan) serta alamat sumber (IP dan Port sumber).
4.  **Peran Sistem Operasi:** Pada aplikasi berbasis UDP, penempelan alamat sumber biasanya dilakukan secara otomatis oleh Sistem Operasi, bukan oleh kode aplikasi yang ditulis oleh programmer.

### Alur Kerja Aplikasi Client-Server
Untuk mendemonstrasikan pemrograman soket (baik TCP maupun UDP), aplikasi sederhana mengikuti langkah-langkah berikut:

* Langkah 1: Klien membaca input berupa sebaris karakter (data) melalui keyboard, kemudian mengirimkan data tersebut ke server.
* Langkah 2: Server menerima data tersebut dan melakukan pemrosesan dengan mengubah seluruh karakter menjadi **huruf besar**.
* Langkah 3: Server mengirimkan kembali data yang telah dimodifikasi (kapital) tersebut kepada klien.
* Langkah 4: Klien menerima data hasil modifikasi dari server dan menampilkannya di layar pengguna.

Proses ini menggambarkan konsep dasar *Request-Response*. Perbedaan utamanya terletak pada bagaimana soket tersebut dikelola: **TCP** akan memastikan urutan data benar melalui jabat tangan (*handshake*), sedangkan **UDP** akan langsung mengirimkan data tanpa mempedulikan status koneksi terlebih dahulu.

## Program Socket dengan UDP

Di bagian ini, kita akan menulis program client-server sederhana yang menggunakan UDP dan menulis program serupa yang menggunakan TCP. Proses yang berjalan pada mesin yang berbeda berkomunikasi satu sama lain dengan mengirimkan pesan ke dalam soket. Kita mengatakan bahwa setiap proses dianalogikan dengan sebuah rumah dan soket proses dianalogikan dengan sebuah pintu. Aplikasi berada di satu sisi pintu di rumah; protokol transport-layer berada di sisi lain pintu di dunia luar. Developer aplikasi memiliki kendali atas segala sesuatu di sisi lapisan aplikasi soket; namun, ia memiliki sedikit kontrol dari sisi transport-layer.

### Kode UDP Client dalam file udp-client.py
```
from socket import *
import sys

# Konfigurasi alamat dan port server
serverName = '10.218.0.61'  # Ganti dengan alamat IP server yang sesuai
serverPort = 12000

# Inisialisasi socket UDP di luar loop agar tidak dibuat berulang-ulang
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)  # Batas waktu tunggu 5 detik

print("Ketik 'exit' untuk mematikan server dan keluar, atau 'keluar' untuk tutup client saja.\n")

try:
    while True:
        # Input pesan dari pengguna
        message = input('Masukkan kalimat lowercase : ')
        
        # Validasi jika input kosong
        if not message:
            continue

        # Mengirim pesan ke server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Cek apakah pengguna ingin keluar
        if message.lower() == 'exit':
            print("Perintah exit dikirim. Mematikan server dan menutup klien...")
            break
        elif message.lower() == 'keluar':
            print("Menutup klien...")
            break
        
        try:
            # Menerima balasan dari server
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print(f"Balasan dari Server: {modifiedMessage.decode()}\n")
        except timeout:
            print("Kesalahan : Server tidak merespons (Timeout).\n")

except Exception as e:
    print(f"Terjadi kesalahan : {e}")
finally:
    # Menutup koneksi socket secara permanen saat loop berhenti
    clientSocket.close()
    print("Koneksi ditutup.")
```

### Kode UDP Server dalam file udp-server.py
```
from socket import *
import sys

# Konfigurasi server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print(f"Server UDP siap menerima pesan pada port {serverPort}")
print("Ketik 'exit' dari sisi klien untuk mematikan server secara remote.\n")

try:
    while True:
        # Menerima pesan dari klien
        message, clientAddress = serverSocket.recvfrom(2048)
        
        # Mendekode pesan
        original_message = message.decode().strip()
        
        # Cek apakah pesan adalah perintah untuk keluar
        if original_message.lower() == 'exit':
            print(f"Mematikan server...")
            break
        
        # Mengubah pesan menjadi huruf kapital
        modifiedMessage = original_message.upper()
        
        # Menampilkan informasi klien dan isi pesan
        print(f"Diterima dari {clientAddress[0]}:{clientAddress[1]}: {original_message}")
        print(f"Mengirim balik : {modifiedMessage}")
        
        # Mengirim kembali pesan yang telah diubah ke klien
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        
except Exception as e:
    print(f"\nTerjadi kesalahan : {e}")
finally:
    print("Server telah berhenti.")
    serverSocket.close()
    sys.exit(0)
```

### OUTPUT

![udp output](../week%206/assets/image/udp.png)

## Program Socket dengan TCP

Tidak seperti UDP, TCP adalah protokol berorientasi koneksi. Ini berarti bahwa sebelum klien dan server dapat mulai mengirim data satu sama lain, mereka harus terlebih dahulu handshake dan membuat koneksi TCP. Salah satu ujung koneksi TCP terpasang ke soket klien dan ujung lainnya terpasang ke soket server. Saat membuat koneksi TCP, kita mengaitkannya dengan alamat soket klien (alamat IP dan nomor port) dan alamat soket server (alamat IP dan nomor port).

### Kode TCP Client dalam file tcp-client.py

```
#
from socket import * #import all ketik bintang

serverName = "localhost" #nama server
serverPort = 12000 #port server

clientSocket = socket(AF_INET,SOCK_STREAM) #membuat socket TCP | AF_INET untuk IPv4 | SOCK_STREAM untuk TCP

#HUBUNGKAN | connect ke server
clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukkan pesan yang ingin dikirim ke server: ")

running = True
while running:
    message = input(">") #input pesan dari user
#KIRIM PESAN | send pesan ke server
    clientSocket.send(message.encode()) #encode(mengubah menjadi biner) pesan ke bytes sebelum dikirim

    #kalo exit = socket ditutup
    if message.lower() == "exit":
        print("[SYSTEM] Keluar dari program.")
        running = False
        break

    #menerima balasan dari server
    modifiedMessage = clientSocket.recv(2048) #menerima data dari server, 2048 adalah ukuran buffer(maksimal bytes yang diterima dalam satu kali recv)
    print("[SERVER] pesan: ", modifiedMessage.decode())

#tutup socket
clientSocket.close()
print("[SYSTEM] Socket ditutup. Program selesai.")
```

### Kode TCP Server dalam file tcp-server.py
```
from socket import * #import semua dari modul socket

serverPort = 12000 #port server
serverSocket = socket(AF_INET,SOCK_STREAM) #membuat socket TCP | AF_INET untuk IPv4 | SOCK_STREAM untuk TCP

#BIND | mengikat socket ke alamat dan port tertentu
serverSocket.bind(
    ('', serverPort) #'' berarti bind ke semua interface yang tersedia
)

#LISTEN | siap menerima koneksi masuk
serverSocket.listen(1) #1 adalah jumlah maksimum koneksi yang dapat antre
print("[SYSTEM] Server siap digunakan")

running = True
while running:
    #menyetujui koneksi masuk dari client
    connectionSocket, addr = serverSocket.accept()

    while True:
        #menerima pesan dari client, pesannya = 1010101010
        message = connectionSocket.recv(2048).decode() #menerima data dari client, 2048 adalah ukuran buffer(maksimal bytes yang diterima dalam satu kali recv)

        if not message:
            break #keluar dari loop jika tidak ada pesan (client menutup koneksi)

        #cek apakah pesan adalah "exit"?
        if message.lower() == "exit":
            print("[SYSTEM] Client ingin keluar.")
            running = False
            break

        #memodifed menjadi capslock
        modifiedMessage = message.upper() #ubah pesan menjadi huruf kapital
        print("[CLIENT] diterima: ", modifiedMessage)

        #kirim balasan ke client
        connectionSocket.send(modifiedMessage.encode()) #encode(mengubah menjadi biner) pesan ke bytes sebelum dikirim

    #tutup koneksi dengan client
    connectionSocket.close()

#tutup socket server
serverSocket.close()
```

### OUTPUT

![tcp output](../week%206/assets/image/tcp.png)