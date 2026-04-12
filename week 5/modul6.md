# TCP
## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol TCP menggunakan Wireshark

## 6.1 Pengantar
Pada modul ini, kita akan mempelajari protokol yang terkenal yaitu TCP secara mendetail. Kita akan menganalisis trace atau jejak segmen TCP yang dikirim dan diterima ketika terjadi transaksi pengiriman file dengan ukuran 150 KB (berisi teks Alice’s Adventures in Wonderland karya Lewis Carrol) dari komputer Anda ke server jarak jauh. Kita akan mempelajari penggunaan nomor urutan dan acknowledgement TCP untuk memfasilitasi proses transfer data yang terpercaya; kita akan melihat algoritma “congestion control” TCP –mulai bekerja secara lambat dan menghindari kemacetan-beraksi; dan kita akan melihat mekanisme “flow control” yang disarankan oleh penerima TCP. Kita juga akan membahas secara singkat pengaturan koneksi TCP serta menyelidiki performa (throughput dan round-trip time) koneksi TCP antara komputer Anda dan server.

---

## Transfer TCP
1. Buka browser dan masukkan link `http://gaia.cs.umass.edu/wireshark-labs/alice.txt`
![alice](../week%205/assets/image/alice.png)

2. Unduh salinan ASCII dari naskah Alice in Wonderland. Simpan file tersebut di komputer.
![unduh alice](../week%205/assets/image/unduhalice.png)

3. Selanjutnya buka link upload `http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html`. 
4. Gunakan tombol Choose File untuk memilih file alice.txt yang telah diunduh tadi, namun jangan dulu menekan tombol upload. Berikut adalah gambar sebelum tombol upload ditekan namun sudah memilih file:
![choose file](../week%205/assets/image/uploadfile.png)

5. Jalankan Wireshark dan mulai untuk mengambil paket.

6. Kembali ke browser dan tekan tombol Upload alice.txt untuk mengunggah file ke `gaia.cs.umass.edu`.
![upload file](../week%205/assets/image/upload%20alice.png)

7. Buka kembali wireshark dan hentikan pengambilan paket
8. Filter `tcp` untuk melihat hanya tcp saja yang tampil
![filter tcp](../week%205/assets/image/filter%20tcp.png)

7. Cari paket dengan flag [SYN] di bagian awal paket.
![SYN](../week%205/assets/image/SYN1.png)

8. Cari paket dengan keterangan HTTP POST yang menunjukkan bahwa proses pengiriman file alice telah berhasil.
![200OK](../week%205/assets/image/200OK.png)

## 6.3 Menganalisis Tampilan Awal pada Captured Trace dan Menjawab Pertanyaannya
1. Unduh file `http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip` kemudian file diekstrak dengan nama wireshark-traces.
Hasil ekstrak file yang diunduh:

![wr traces](../week%204/assets/image/wr-traces.png)

2. Buka file tcp-ethernal-trace-1
![open](../week%205/assets/image/open%20with.png)

#### Jawaban Pertanyaan
1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk mentransfer file ke gaia.cs.umass.edu?

![nomor1](../week%205/assets/image/nmr1.png)
Source Port: 1161
Destination Port: 80 (ini adalah port standar untuk layanan HTTP)
Source: 192.168.1.102
Destination: 128.119.245.12 (ini adalah alamat IP dari server gaia.cs.umass.edu)

2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini?
![nomor2](../week%205/assets/image/nmr2.png)

Alamat IP: `128.119.245.12`
Mengirim segmen: Server menggunakan Source Port: 80.
Menerima segmen: Server menerima data dari klien pada Destination Port: 80.

## 6.4 Dasar TCP
1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN?

Menggunakan Filter :`tcp.flags.syn == 1 && tcp.flags.ack == 0`

![no1](../week%205/assets/image/no1.png)

Nomor urut (sequence number) segmen TCP SYN yang digunakan untuk memulai koneksi antara komputer klien dan gaia.cs.umass.edu adalah 0 (secara relatif) atau 232129012 (secara raw), di mana segmen ini dapat diidentifikasi sebagai segmen SYN karena pada bagian Flags di header TCP, bit Syn bernilai 1 (Set) sementara bit Acknowledgment (ACK) bernilai 0, yang menandakan bahwa ini adalah langkah pertama dari proses three-way handshake untuk menyinkronkan nomor urut awal antara klien dan server.

2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen sehingga teridentifikasi sebagai segmen SYNACK?

Menggunakan Filter : `tcp.flags.syn == 1 && tcp.flags.ack == 1`

![no2](../week%205/assets/image/no2.png)

Segmen SYNACK yang dikirim oleh `gaia.cs.umass.edu` memiliki nomor urut (*Sequence Number*) sebesar **0** secara relatif (atau **883061785** secara *raw*), dengan nilai pada *field* **Acknowledgment Number** sebesar **1** secara relatif (atau **232129013** secara *raw*). Server menentukan nilai *Acknowledgment* tersebut dengan cara mengambil nomor urut (*Sequence Number*) dari segmen SYN yang diterima sebelumnya dari klien (yaitu 232129012) dan menambahkannya dengan **1**. Segmen ini teridentifikasi sebagai **SYNACK** karena pada bagian **Flags** di *header* TCP, kedua bit yaitu **Acknowledgment: Set** dan **Syn: Set** bernilai **1** secara bersamaan (ditunjukkan dengan kode hex `0x012`), yang menandakan bahwa server telah menerima permintaan koneksi dan mengirimkan sinkronisasi balasan kepada klien.

3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATA-nya.
![no3.1](../week%205/assets/image/no3.1.png)
![no3.2](../week%205/assets/image/no3.2.png)

Detail pada TCP gambar diatas menunjukkan relative sequence numbernya adalah 1

4. Analisis 6 segmen pertama
Langkahnya:
![langkah](../week%205/assets/image/langkah4.png)

Hasilnya:
![no4](../week%205/assets/image/no4.png)

Berdasarkan grafik RTT diatas, nilai RTT selama proses transfer file ini didalam rentang 0 ms sampai 280 ms.

5. Panjangnya 6 segmen pertama

![no5](../week%205/assets/image/no5.png)

Segmen 1 berukuran 565 bytes, dan segmen 2 sampai 6 masing masing berukuran 1460 bytes.

6. Buffer Penerima

![no6](../week%205/assets/image/no6.png)

Pada blok merah dan keterangannya dibawah ada tulisan window : 5840 byte, yang berarti jumlah minimum 5840 byte. Artinya tidak menghambat pengirim karena tidak pernah melampaui batas window size yang tersedia selama seluruh proses transfer berlangsung.

7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di dalam file trace) untuk menjawab pertanyaan ini?

Menggunakan Filter : `tcp.analysis.retransmission`

![no7](../week%205/assets/image/no7.png)

Tidak ada segmen yang di transmisikan ulang.

8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang diterima?

![no8](../week%205/assets/image/no8.png)

Berdasarkan data pada gambar, penerima biasanya mengakui data dalam jumlah **1460 bytes**, yang sesuai dengan nilai *Maximum Segment Size* (MSS) untuk satu segmen TCP standar (terlihat pada kolom *Length* di paket-paket seperti Frame 5, 7, dan 8). Namun, dalam log tersebut, kita dapat mengidentifikasi kasus di mana penerima melakukan ACK untuk setiap segmen karena terdapat beberapa paket ACK berturut-turut yang masing-masing mengakui satu segmen data berukuran 1460 bytes (seperti pada Frame 7, 8, dan 10), menunjukkan bahwa penerima tidak selalu menunggu dua segmen untuk mengirimkan satu ACK (metode *Delayed ACK*), melainkan segera merespons segmen yang datang untuk memastikan kelancaran transmisi data selama proses transfer file tersebut.

9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? Jelaskan bagaimana Anda menghitung nilai ini.

Ini tampilan grafik Throughput TCP yang dihasilkan melalui Statistics → TCP Stream Graph → Throughput:

![no9](../week%205/assets/image/no9.png)

Nilai *throughput* dihitung dengan membagi total data yang ditransfer dengan durasi waktu transmisi, yaitu **Throughput = Total Bytes / Total Waktu**. Dari informasi yang muncul di bagian bawah grafik (*hover over the graph for details*), tercatat bahwa total data yang ditransfer adalah **164 KB** (atau sekitar **164.000 bytes**) dengan jumlah paket sebanyak **125 pkts**. Jika kita melihat sumbu horizontal (Time), proses transfer dimulai dari detik **0** hingga sekitar detik **5,4** (berdasarkan Frame 203 pada data sebelumnya). Dengan demikian, perhitungan kasarnya adalah **164.000 bytes / 5,4 detik = 30.370 bytes/detik**. Nilai ini jika dikonversi ke satuan bit (dikali 8) menjadi sekitar **242,9 kbps**, yang sangat sesuai dengan visualisasi garis cokelat pada grafik yang stabil di rentang **200-250 kbps**.

## 6.5 Congestion Control pada TCP
Untuk menganalisis congestion control TCP, gunakan fitur Statistics → TCP Stream Graph → Time-Sequence-Graph (Stevens) yang memplot nomor urut segmen terhadap waktu pengirimannya.
Berikut tampilan grafik Time-Sequence (Stevens):

![akhir](../week%205/assets/image/terakhir.png)

### Jawaban dari pertanyaan
Berdasarkan grafik **Time-Sequence-Graph (Stevens)** yang Anda lampirkan, berikut adalah analisis mengenai perilaku kontrol kemacetan (*congestion control*) pada koneksi tersebut:

1. Analisis Slow Start dan Congestion Avoidance
**Fase Slow Start:** Fase ini dimulai tepat pada **0 detik** segera setelah *three-way handshake* selesai. Anda dapat mengidentifikasi fase ini melalui kurva kenaikan nomor urut yang berbentuk eksponensial (melengkung ke atas dengan cepat) pada rentang waktu **0 hingga sekitar 0,5 detik**. Di sini, TCP mencoba meningkatkan jumlah segmen yang dikirim secara agresif.
**Fase Congestion Avoidance:** Algoritma ini mengambil alih setelah detik ke-0,5, di mana kenaikan nomor urut berubah dari kurva eksponensial menjadi **garis lurus (linear) yang stabil** hingga akhir transmisi pada detik ke-5,4. Hal ini menunjukkan bahwa TCP telah mencapai ambang batas (*threshold*) atau mendeteksi keterbatasan bandwidth, sehingga hanya meningkatkan jendela kemacetan secara bertahap untuk menghindari kepadatan jaringan.

2. Perbedaan dengan Perilaku Ideal TCP
Data yang diukur dalam *trace* ini menunjukkan perbedaan yang cukup mencolok dibandingkan teori ideal:
**Kenaikan yang Sangat Linear:** Dalam perilaku ideal, kita biasanya melihat pola "gigi gergaji" (*sawtooth pattern*) di mana grafik akan naik, lalu turun tajam saat terjadi kehilangan paket (*packet loss*), dan naik kembali. Namun, pada grafik Anda, garisnya terlihat sangat mulus dan stabil.
**Keterbatasan Bandwidth vs Kemacetan:** Perilaku linear yang sangat panjang ini menunjukkan bahwa transmisi tidak dibatasi oleh kemacetan jaringan yang dinamis, melainkan lebih dibatasi oleh **kapasitas bandwidth tetap** atau *pacing* dari sistem operasi/aplikasi. TCP tidak sempat melakukan "tabrakan" yang memaksa jendela kemacetan turun drastis, melainkan langsung beroperasi pada tingkat yang stabil (mencapai *steady state*) dengan sangat cepat.

Secara keseluruhan, *trace* ini menunjukkan koneksi yang sangat stabil dengan *throughput* yang konsisten, berbeda dengan lingkungan jaringan yang sibuk di mana pola fluktuatif lebih sering terjadi.