# DNS
## Tujuan Praktikum
Mahasiswa dapat menginvestigasi cara kerja DNS menggunakan Wireshark
---
## 4.2 NSLOOKUP
Perintah `nslookup` merupakan alat bantu yang berfungsi untuk menerjemahkan nama domain yang mudah diingat manusia menjadi alamat IP yang dapat dipahami oleh mesin dalam jaringan komputer. Saat perintah ini dijalankan, perangkat akan mengirimkan permintaan informasi ke server DNS untuk mencari tahu lokasi server dari suatu situs web, baik itu melalui server perantara maupun server sah (asli). Hasil yang ditampilkan pada terminal memungkinkan kita untuk memverifikasi konfigurasi jaringan serta memastikan bahwa koneksi menuju alamat tujuan sudah terarah dengan benar berdasarkan database DNS yang tersedia.
Adapun sintaks umum perintah nslookup, yaitu:

```nslookup –option1 –option2 host-to-find dns-server```

Secara umum, nslookup dapat dijalankan dengan nol, satu, dua, atau lebih opsi.

### Perintah 1 : nslookup untuk domain www.mit.edu
Menggunakan perintah: 
```nslookup www.mit.edu```

![nslookup mit edu](../week3/assets/week3/domain1.png)

Berdasarkan hasil pengujian menggunakan perintah `nslookup`, sistem melakukan pengecekan alamat IP dari domain `www.mit.edu` melalui DNS server lokal dengan alamat `10.217.7.77`. Laporan ini menunjukkan jawaban bersifat non-authoritative, yang berarti informasi alamat IP diambil dari data cache server antara, bukan langsung dari server utama pemilik domain. Hasil resolusi menunjukkan bahwa domain tersebut terhubung ke jaringan Akamai (CDN) dengan alamat IPv4 `23.217.163.122` serta beberapa alamat IPv6, yang mengindikasikan penggunaan distribusi konten global untuk mengoptimalkan kecepatan akses situs.

### Perintah 2 : identifikasi name server otoritatif pada domain mit.edu
Menggunakan perintah: 
```nslookup –type=NS mit.edu```

![nslookup –type=NS mit edu](../week3/assets/week3/domain2.png)

Perintah `nslookup -type=NS mit.edu` digunakan untuk mengidentifikasi daftar server nama (name servers) yang bertanggung jawab secara otoritatif atas pengelolaan domain `mit.edu`. Berdasarkan hasil eksekusi tersebut, domain MIT terlihat menggunakan infrastruktur dari Akamai, yang ditunjukkan oleh deretan nama server seperti `ns1-37.akam.net` hingga `usw2.akam.net` beserta alamat IP (IPv4 dan IPv6) masing-masing. Informasi ini sangat berguna dalam administrasi jaringan untuk mengetahui server mana yang menyimpan catatan DNS asli dari domain tersebut, sehingga proses resolusi nama ke alamat IP dapat dikelola dengan lebih stabil dan terdistribusi secara global.

### Perintah 3 : Percobaan Kueri DNS ke Server Luar
Menggunakan perintah: 
```nslookup www.aiit.or.kr bitsy.mit.edu```

![nslookup www.aiit.or.kr bitsy.mit.edu](../week3/assets/week3/domain3.png)

Perintah ini bertujuan untuk melakukan kueri DNS secara langsung ke server bitsy.mit.edu guna mendapatkan alamat IP dari www.aiit.or.kr tanpa melalui server DNS lokal. Dengan mengarahkan permintaan ke server spesifik, diharapkan terjadi pertukaran informasi langsung antara host pengirim dan server tujuan untuk mendapatkan jawaban yang lebih akurat. Namun, hasil pada terminal menunjukkan status DNS request timed out, yang mengindikasikan bahwa server bitsy.mit.edu tidak merespons permintaan tersebut. Hal ini bisa disebabkan oleh server yang sedang tidak aktif, adanya blokir pada kebijakan keamanan jaringan, atau kendala konektivitas yang menghalangi komunikasi antar perangkat secara langsung.

---

## Jawaban dari 3 Pertanyaan
### 1. Pencarian alamat IP untuk domain National University of Singapore (Server Web Asia)

![web asia nus](../week3/assets/week3/server%20asia.png)

Hasil perintah `nslookup www.nus.edu.sg` menunjukkan proses pencarian alamat IP untuk domain National University of Singapore melalui DNS server dengan alamat 10.92.111.136. Output ini memberikan jawaban bersifat non-authoritative, yang mengindikasikan bahwa informasi alamat IP diperoleh dari rekaman cache pada server lokal dan bukan berasal langsung dari server pusat milik NUS. Berdasarkan hasil tersebut, domain utama diarahkan ke nama alias mgnzsqc.x.incapdns.net dengan alamat IPv4 45.60.35.225, yang menandakan penggunaan layanan keamanan atau akselerasi konten dari Incapsula untuk melindungi dan mengoptimalkan akses menuju situs web tersebut.

### 2. Pencarian server DNS otoritatif Universitas Oxford UK (server DNS otoritatif untuk universitas di Eropa)

![univ eropa](../week3/assets/week3/univ%20eropa.png)

Hasil perintah `nslookup -type=NS ox.ac.uk` menunjukkan daftar server nama (name servers) resmi yang bertanggung jawab atas domain Universitas Oxford. Melalui kueri ini, sistem mengidentifikasi beberapa server otoritatif seperti `dns0.ox.ac.uk` hingga `auth6.dns.ox.ac.uk` beserta alamat IP publiknya masing-masing, baik dalam format IPv4 maupun IPv6. Keberadaan banyak server nama ini menunjukkan redundansi infrastruktur jaringan universitas untuk memastikan bahwa layanan resolusi domain tetap stabil dan dapat diakses dari berbagai lokasi. Data ini berfungsi sebagai referensi utama bagi perangkat lain di internet untuk menemukan alamat IP yang tepat dari semua layanan atau situs web yang berada di bawah naungan domain Oxford.

### 3. Mencari mail server Yahoo melalui DNS yang ada di nomor 2, dan mencari IP nya

![yahoo](../week3/assets/week3/yahoo.png)

Berdasarkan hasil praktik pada domain `yahoo.com` menggunakan server DNS perantara `ns0.ox.ac.uk`, sistem berhasil mendapatkan rekaman *Mail Exchanger* (MX) yang terdiri dari `mta5.am0.yahoodns.net`, `mta6.am0.yahoodns.net`, dan `mta7.am0.yahoodns.net`. Masing-masing server memiliki nilai *preference* sebesar 1, yang menunjukkan bahwa Yahoo! menggunakan beberapa server dengan prioritas setara untuk menangani lalu lintas email masuk. Meskipun terminal hanya menampilkan nama *host* server email tersebut, setiap *host* merujuk pada alamat IP tertentu yang berfungsi sebagai tujuan pengiriman data. Dalam infrastruktur skala besar seperti Yahoo!, alamat IP ini bersifat dinamis dan terdistribusi, di mana alamat IP dari *mail exchanger* tersebut dapat diketahui melalui proses resolusi DNS lanjutan guna memastikan pesan terkirim ke server yang paling optimal secara geografis.
Alamat IP tidak muncul secara otomatis pada perintah tersebut karena `nslookup` hanya memberikan daftar nama server email. Untuk mendapatkan alamat IP pastinya, diperlukan perintah tambahan seperti `nslookup mta5.am0.yahoodns.net`. Berikut praktiknya:

![ip yahoo](../week3/assets/week3/IP%20yahoo.png)

Hasil dari perintah `nslookup mta5.am0.yahoodns.net` menunjukkan proses resolusi nama host dari salah satu server email Yahoo! menjadi daftar alamat IP yang konkret. Terlihat bahwa satu nama host tersebut memiliki banyak alamat IP, seperti `98.136.96.77`, `67.195.228.109`, hingga `67.195.204.72`. Hal ini mengindikasikan bahwa Yahoo! menerapkan teknik *round-robin* DNS atau penggunaan *load balancer* untuk mendistribusikan beban kerja ke berbagai server fisik yang berbeda guna mencegah kelebihan beban (*overload*) pada satu titik. Dengan banyaknya alamat IP yang tersedia, sistem memastikan layanan email tetap stabil dan memiliki ketersediaan tinggi, sehingga jika salah satu server mengalami gangguan, lalu lintas data dapat dialihkan secara otomatis ke alamat IP lain yang masih aktif.

---

## 4.3 IPCONFIG