# PENGENALAN TOOLS
## Tools pada wireshark
1. Pastikan sudah menginstall wireshark dan python
2. Buka aplikasi wireshark
3. Perhatikan bahwa di bawah bagian Capture, ada daftar yang disebut interfaces.
Perhatikan tulisan “Wi-Fi” (yang ditandai dengan warna merah pada gambar dibawah ini), ini merupakan interfaces untuk akses Wi-Fi. Semua paket ke/dari komputer ini akan melewati interfaces Wi-Fi, jadi di sinilah kita akan menangkap paket. Lalu klik dua kali pada interfaces ini untuk membukanya.

gambar:
![http](../assets/image/wifi%20interfaces.png)

4. Setelah mengklik interfaces ini untuk memulai pengambilan paket (yaitu, agar Wireshark
mulai menangkap semua paket yang dikirim ke/dari interfaces itu), gambar dibawah ini akan ditampilkan, dan menampilkan informasi tentang paket yang diambil. Setelah memulai pengambilan paket, kita bisa menghentikannya dengan menggunakan menu pull down Capture dan memilih Stop (atau dengan mengklik tombol kotak merah di sebelah sirip Wireshark pada gambar dibawah ini). Kalau sirip hiu warna biru digunakan untuk memulai pengambilan paket keembali.

gambar :
![klik wifi](../assets/image/tampilan%20klik%20wifi.png)

5. Penjelasan komponen pada gambar diatas :
Antarmuka Wireshark memiliki lima komponen utama yang membantu pengguna dalam menganalisis paket jaringan.

Pertama, **command menu**, yaitu menu utama di bagian atas yang berisi berbagai pilihan seperti membuka atau menyimpan hasil tangkapan paket serta memulai proses capture paket jaringan.

Kedua, **packet-listing window**, yang menampilkan daftar paket yang berhasil ditangkap. Setiap paket ditampilkan dalam satu baris yang berisi informasi seperti nomor paket, alamat sumber dan tujuan, jenis protokol, serta keterangan singkat lainnya. Daftar ini juga bisa diurutkan berdasarkan kolom tertentu dengan mengklik nama kolom tersebut.

Ketiga, **packet-header details window**, yang menampilkan informasi lebih rinci dari paket yang dipilih pada daftar paket. Di bagian ini pengguna dapat melihat detail dari berbagai lapisan protokol seperti Ethernet, IP, TCP, atau UDP. Informasi tersebut bisa diperluas atau disembunyikan sesuai kebutuhan.

Keempat, **packet-contents window**, yang menunjukkan isi lengkap dari paket yang ditangkap. Data ditampilkan dalam dua format, yaitu ASCII dan heksadesimal, sehingga memudahkan analisis data yang lebih mendalam.

Kelima, **packet display filter field**, yaitu kolom untuk menyaring paket yang ditampilkan. Dengan fitur ini, pengguna bisa menampilkan hanya paket tertentu, misalnya hanya paket HTTP, sehingga analisis menjadi lebih fokus dan mudah dilakukan.

## Test Run Wireshark

1. Kita akan lakukan pengambilanz beberapa paket menarik terlebih dahulu. Untuk melakukannya, kita perlu menghasilkan beberapa lalu lintas jaringan. Kita akan melakukannya dengan menggunakan browser web, yang akan menggunakan
protokol HTTP.
2. Saat Wireshark sedang berjalan, masukkan LINK: http://gaia.cs.umass.edu/wiresharklabs/INTRO-wireshark-file1.html dan tampilkan halaman tersebut di aplikasi browser apapun pada laptop. Untuk menampilkan halaman ini, browser kita akan menghubungi server HTTP di gaia.cs.umass.edu dan bertukar pesan HTTP dengan server untuk mendownload halaman ini. Frame Ethernet atau WiFi yang berisi pesan HTTP ini (serta semua frame lain yang melewati adaptor Ethernet atau WiFi) akan ditangkap oleh Wireshark.
3. Setelah browser menampilkan halaman sebuah tulisan berisi selamat, maka kembali ke halaman wireshark untuk mengecek apakah situs tersebut sudah terdeteksi oleh jaringan wifi atau belum.
4. Filter paket yang sedang jalan dengan cara, klik kolom pencarian pada wireshark lalu ketik HTTP yang ditandai dengan warna hijau pada gambar dibawah ini. Setelah itu cari yang menampilkan pesan HTML nya pada halaman detail paket (ditandai dengan klik yang warna merah itu kemudian di lihat bagian detailnya ada dibawah). Pada gambar dibawah ini sudah tertulis pesan selamat yang manandakan situs HTTP berjalan melalui jaringan kita.

gambar: 
![HTTP](../assets/image/modul2.png)

5. Pencet Stop dengan klik tombol persegi warna merah di sebelah sirip hiu
6. Lalu keluar dari wireshark