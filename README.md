# PROYEK TENGAH SEMESTER - PEMROGRAMAN BERBASIS PLATFORM C - KELOMPOK 5
## Link Proyek
http://lembarpena-c09-tk.pbp.cs.ui.ac.id/
## Nama-nama anggota kelompok
Bryan Jeshua Mario Timung - 2206027021</br>
Clarista - 2206815541</br>
Muhammad Hilal Darul Fauzan - 2206830542</br>
Sabrina Aviana Dewi - 2206030520</br>
Rifqi Rahmatuloh - 2206820365</br>
---


## Cerita aplikasi yang diajukan serta manfaatnya
LembarPena adalah tempat seluruh komunitas literasi berkumpul. Pembaca dapat membeli buku incaran mereka. Perusahaan memiliki banyak administrator yang akan membantu menjual buku. Penulis buku dapat mempromosikan karya mereka pada satu aplikasi ini melalui fitur forum diskusi. Terdapat juga fitur wishlist sehingga pembaca bisa menyimpan buku yang hendak dibeli. Aplikasi ini ditujukan kepada para peminat literasi yang selama ini harus mencari, membeli, menyimpan, dan mengulas buku pada platform yang berbeda-beda sehingga menimbulkan anggapan bahwa untuk menjadi penggiat literasi itu rumit dan ribet. Dengan efisiensi yang ditawarkan, aplikasi ini bermanfaat untuk meningkatkan minat literasi di kalangan masyarakat, meningkatkan daya beli buku, dan menyediakan tempat untuk pembaca serta penulis berinteraksi.

--- 

## Daftar modul yang akan diimplementasikan
### 📚 Modul Buy Book 📚
Modul ini memungkinkan pengguna untuk memilih dan membeli buku dari katalog yang tersedia di situs web. Fitur-fitur utama dari modul ini akan meliputi:
- Menampilkan daftar buku yang tersedia untuk dibeli. Pengguna bisa melakukan add to cart. Jendela cart akan menampilkan keranjang belanja dan bisa meminta input jumlah dan akan mengoperasikan total harga.
- Opsi untuk pengguna mencari buku berdasarkan rating buku.
- Saat pengguna mengklik buku tertentu, halaman detail buku akan menampilkan informasi yang lebih lengkap

### 🛒 Modul Checkout Book 🛒
Modul ini untuk proses finalisasi pembelian buku yang telah dipilih oleh pengguna. Fitur-fitur utama dari modul ini akan meliputi:
- Menyimpan buku yang dipilih oleh pengguna sebelum melakukan pembayaran
- Memberi konfirmasi kepada pengguna untuk mengisi form, seperti alamat dan pilihan pembayaran
- Integrasikan dengan sistem pembayaran

### 🎁 Modul Wishlist 🎁
Modul ini memungkinkan pengguna untuk menyimpan daftar buku yang mereka inginkan tetapi belum siap dibeli. Fitur-fitur utama dari modul ini akan sebagai berikut:
- Melihat daftar buku yang ada dalam wishlist pengguna
- Menambah buku ke dalam wishlist dari jendela rekomendasi. Di jendela rekomendasi, saat pengguna mengklik buku tertentu, halaman detail buku akan menampilkan informasi yang lebih lengkap
- Menghapus buku dari wishlist
  
### 📝 Modul Book Forum 📝
Modul ini memungkinkan pengguna untuk menulis dan berbagi opini, ulasan, serta dapat berdiskusi mengenai buku dengan pengguna lain. Fitur-fitur utama dari modul ini akan meliputi:
- Pengguna bisa memberikan pertanyaan dan tanggapan untuk buku tertentu
- Berdiskusi dengan pengguna lain mengenai buku tersebut
- Filter untuk hanya menampilkan diskusi terhadap buku dengan rating > 4.5

### 📥 Modul Register Book to Sell 📥
Modul ini memungkinkan admin untuk mendaftarkan buku yang ingin dijual di situs web. Fitur-fitur utama dari modul ini akan meliputi:
- Sebuah form yang harus diisi dengan informasi detail buku seperti judul, penulis, harga, dan lainnya
- Proses verifikasi oleh admin sebelum buku ditampilkan di katalog untuk dijual

---

## Sumber dataset katalog buku
Dataset yang akan kami pakai berasal dari Kaggle dengan judul ```Google Books Dataset```. Klik link di [sini](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)

---

## Role atau peran pengguna beserta deskripsinya
1. Admin </br>
Admin merupakan profil untuk mengatur pengelolaan penjualan buku lewat perusahaan lembarpena.

2. Buyer </br>
Buyer atau pembeli ini dapat membeli buku yang dicari dan diinginkan dari para penjual buku. Nantinya buyer ini juga bisa berdiskusi di forum dengan buyer yang lain.

