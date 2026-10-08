# Studi_Kasus_6_Tisha-Ayu

`Nama : Tisha Ayu Nabilah Lubis`

`NIM : 2609116006`

`GENAP`

Sebelum saya membahas kode dari program saya, saya akan menjelaskan sedikit. Program ini adalah sistem manajemen inventaris barang sederhana berbasis Python yang terhubung dengan file format JSON. Fungsinya untuk menampilkan daftar barang beserta stoknya, menambahkan data barang baru ke dalam penyimpanan, serta menyediakan menu interaktif di terminal agar pengoperasian data barang jadi lebih praktis.

## KODE ##

<img width="575" height="257" alt="image" src="https://github.com/user-attachments/assets/5c337a5b-fb25-4a83-94fd-5f6d1a6d526b" />

Disini, saya mengimpor modul `json` dan `os` untuk mengelola data file. Pertama, saya membuat fungsi `lihat_barang` untuk menampilkan data. Fungsi ini membuka dan membaca file `barang.json` dengan mode `"r"`, lalu memuat datanya menggunakan `json.load`. Setelah data berhasil dimuat, dilakukan perulangan `for` untuk menampilkan nama dan stok dari setiap barang satu per satu.

Selanjutnya, saya membuat fungsi `tambah_barang` untuk menambahkan barang baru. Fungsi ini diawali dengan membuka dan membaca file `barang.json` terlebih dahulu agar data lama tersimpan. Kemudian, saya memasukkan kode untuk user menginput nama barang dan stok barang, dimana stok diubah menjadi tipe data integer. Data inputan tersebut dibentuk menjadi sebuah dictionary bernama `data_baru`, lalu ditambahkan ke dalam daftar barang menggunakan fungsi `.append()`. Setelahnya, file `barang.json` dibuka kembali dengan mode `"w"` untuk menyimpan dan memperbarui seluruh data menggunakan `json.dump` agar tersusun rapi.

<img width="566" height="184" alt="image" src="https://github.com/user-attachments/assets/6573fe4a-5146-41a2-9910-1958db9a4fff" />

Disini, saya membuat fungsi `main` sebagai program utama yang menjalankan perulangan `while True` agar menu terus ditampilkan. Pertama, sistem akan menampilkan pilihan menu seperti Lihat Barang, Tambah Barang, dan Keluar, lalu memasukkan kode untuk user menginput nomor pilihan. Setelah user memilih, perintah `os.system` dijalankan untuk membersihkan layar terminal sesuai dengan sistem operasi yang digunakan.

Untuk memproses pilihan user, digunakan pengkondisian `if-elif-else`. Jika user memilih `"1"`, maka fungsi `lihat_barang()` dipanggil. Jika user memilih `"2"`, maka fungsi `tambah_barang()` yang dipanggil. Jika user memilih `"3"`, program akan menampilkan pesan terima kasih dan dihentikan dengan perintah `break`. Selain dari itu, jika input tidak sesuai, program akan menampilkan pesan bahwa pilihan tidak valid. Terakhir, fungsi `main()` dipanggil di paling bawah agar program dapat berjalan.

## OUTPUT ##

<img width="524" height="111" alt="Screenshot 2026-10-08 200339" src="https://github.com/user-attachments/assets/65a12bdb-526c-445d-bda4-811fdcbb7a06" />

<img width="533" height="179" alt="Screenshot 2026-10-08 200354" src="https://github.com/user-attachments/assets/819aa806-077e-4851-9c4b-724d42f496f6" />

<img width="454" height="143" alt="Screenshot 2026-10-08 200421" src="https://github.com/user-attachments/assets/ab5a5d70-b2d1-4131-b25f-74df92c6bcc2" />

<img width="528" height="179" alt="Screenshot 2026-10-08 200434" src="https://github.com/user-attachments/assets/aa005c28-d23a-4b3b-97b2-c3125a2d114f" />

<img width="527" height="56" alt="Screenshot 2026-10-08 200445" src="https://github.com/user-attachments/assets/d1792de0-c0bf-4008-9ff5-1d6135bad5f4" />

## JSON SEBELUM DAN SESUDAH ##

### SEBELUM ###

<img width="598" height="250" alt="Screenshot 2026-10-08 200207" src="https://github.com/user-attachments/assets/92824a77-8f84-48d8-b352-d18bfe81e22a" />

### SESUDAH ###

<img width="602" height="274" alt="Screenshot 2026-10-08 200459" src="https://github.com/user-attachments/assets/c8a3ecab-8bcc-4964-9d57-3d1995a791c5" />
