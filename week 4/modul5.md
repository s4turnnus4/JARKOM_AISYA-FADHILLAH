# UDP
## Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol UDP menggunakan Wireshark
---
## 5.1 Pengantar
Di modul ini, kita akan melihat sekilas protokol transport UDP. UDP adalah protokol yang
senderhana dan tidak rumit. Pada tahap ini, Mahasiswa seharusnya sudah mahir menggunakan Wireshark. Oleh karena itu, langkah-langkah pengerjaan tidak akan dijelaskan secara eksplisit seperti pada modul sebelumnya. Contoh tangkapan layar juga tidak akan disediakan.
---

## 5.2 Tugas

Mulailah menangkap paket di Wireshark. Kemudian lakukanlah sesuatu yang akan menyebabkan host mengirim dan menerima beberapa paket UDP. Terkadang, tanpa melakukan apapun (kecuali jika melakukan penangkapan melalui Wireshark), beberapa paket UDP yang dikirimkan oleh orang lain akan terekam dalam jejak atau trace. Secara khusus, Simple Network mengirimkan pesan SNMP di dalam UDP sehingga akan menemukan beberapa pesan SNMP (dan juga paket UDP) di dalam trace.

Setelah menghentikan penangkapan paket, atur filter paket sehingga Wireshark hanya menampilkan paket UDP yang dikirimkan dan diterima oleh host. Pilih salah satu paket UDP kemudian perluas fields atau bidangnya pada bagian detail. Jika tidak dapat menemukan paket UDP atau menjalankan Wireshark pada koneksi jaringan langsung, kita dapat mengunduh file berisi trace penangkapan paket UDP yang telah disediakan.

Langkah-Langkah

1. Unduh file `http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip` kemudian file diekstrak dengan nama wireshark-traces.
Hasil ekstrak file yang diunduh:

![wr traces](../week%204/assets/image/wr-traces.png)

2. Didalam file cari yang tulisannya `http-ethernal-trace-5`, lalu buka hasil penangkapan paketnya menggunakan wireshark:

![buka di wr](../week%204/assets/image/buka%20di%20ws.png)

3. Pada filter ketikkan udp untuk hanya menampilkan paket yang menggunakan UDP saja, kita akan menganalisis yang line 1 gambar dibawah ini:

![filter udp](../week%204/assets/image/udp%20wr.png)

---

## Jawaban dari Pertanyaan

### 1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak “field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan!
![no1](../week%204/assets/image/1&2.png)
### 2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?
![no2](../week%204/assets/image/1&2.png)
### 3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui paket UDP pada trace.
![no3](../week%204/assets/image/no3.png)
### 4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2)
![no4](../week%204/assets/image/no3.png)
### 5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk pada pertanyaan 4)
![no5](../week%204/assets/image/no3.png)
### 6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada datagram IP yang mengandung segmen UDP.
![no6](../week%204/assets/image/no6.png)
### 7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!
![no7](../week%204/assets/image/no6.png)