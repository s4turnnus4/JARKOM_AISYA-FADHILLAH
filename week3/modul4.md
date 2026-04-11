# DNS
## Tujuan Praktikum
Mahasiswa dapat menginvestigasi cara kerja DNS menggunakan Wireshark

## NSLOOKUP
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

### Perintah 3 : 