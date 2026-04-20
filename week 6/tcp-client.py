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