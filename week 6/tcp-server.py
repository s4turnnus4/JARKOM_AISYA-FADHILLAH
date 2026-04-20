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