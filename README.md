# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang memiliki rekam jejak panjang sejak tahun 2000. Meskipun telah menghasilkan lulusan berkualitas, tingkat dropout mahasiswa yang tinggi menjadi tantangan utama. Dropout bukan hanya memengaruhi reputasi institusi, tetapi juga menurunkan efisiensi operasional dan keberhasilan program pendidikan.

### Permasalahan Bisnis

- Tingginya angka mahasiswa yang tidak menyelesaikan studi tepat waktu (dropout).
- Tidak adanya sistem deteksi dini untuk memprediksi potensi dropout.
- Kurangnya visualisasi data untuk mendukung pengambilan keputusan strategis oleh manajemen.

### Cakupan Proyek

- Melakukan eksplorasi data dan visualisasi untuk memahami pola dropout mahasiswa.
- Membangun business dashboard berbasis Metabase.
- Mengembangkan model machine learning untuk memprediksi status mahasiswa.
- Menyediakan prototipe aplikasi berbasis Streamlit yang mudah digunakan pihak non-teknis.

### Persiapan

**Sumber data**: Dataset publik bertema pendidikan tinggi (Student Dropout and Success Prediction Dataset)

**Setup environment:**

```bash
pip install -r requirements.txt
```

## Business Dashboard

Business dashboard dikembangkan menggunakan **Metabase** sebagai alat bantu visualisasi untuk membantu manajemen Jaya Jaya Institut dalam memahami faktor-faktor yang memengaruhi status akademik mahasiswa, khususnya potensi dropout.

Dashboard yang dibangun terdiri dari **enam visualisasi utama**, yaitu:

1. **Status Mahasiswa (Enrolled, Dropout, Graduate)**  
   Menampilkan distribusi keseluruhan status mahasiswa. Visualisasi ini memberikan gambaran umum proporsi mahasiswa yang bertahan, lulus, atau keluar dari sistem pendidikan.

2. **Dropout Berdasarkan Status Pernikahan**  
   Visualisasi ini menunjukkan bahwa mahasiswa yang belum menikah memiliki tingkat dropout yang lebih tinggi dibandingkan yang sudah menikah, kemungkinan karena faktor tanggung jawab dan stabilitas hidup.

3. **Hubungan antara Jumlah Mata Kuliah Disetujui dan Dropout**  
   Menampilkan korelasi antara keberhasilan akademik di semester pertama dengan status dropout. Semakin banyak mata kuliah yang disetujui, semakin kecil kecenderungan dropout.

4. **Distribusi Dropout Berdasarkan Usia saat Mendaftar**  
   Mahasiswa usia muda, terutama di bawah 20 tahun, memiliki kecenderungan dropout yang lebih tinggi dibanding usia lebih senior. Hal ini menjadi perhatian dalam strategi pendampingan awal.

5. **Status Dropout Berdasarkan Status Debtor (Tunggakan Pembayaran)**  
   Mahasiswa yang memiliki tunggakan pembayaran (debtor) terlihat lebih rentan mengalami dropout dibanding yang tidak memiliki tunggakan. Visual ini mendukung pentingnya pemantauan aspek finansial mahasiswa.

6. **Hubungan antara Nilai Akademik dan Dropout**  
   Menampilkan rata-rata nilai akademik semester pertama dan kedua terhadap status dropout. Nilai rendah berkorelasi kuat dengan peningkatan angka dropout.

📊 **Akses Dashboard**:  
Email: `root@mail.com`  
Password: `root123`  
(Screenshot dashboard tersedia pada folder `satyacoding-dashboard`)

## Menjalankan Sistem Machine Learning

Model machine learning dibangun menggunakan Random Forest Classifier untuk memprediksi status mahasiswa: `Dropout`, `Enrolled`, atau `Graduate`. Model terintegrasi ke dalam aplikasi berbasis web menggunakan Streamlit.

**Cara menjalankan sistem:**

Untuk menjalankan prototype sistem prediksi dropout mahasiswa, ikuti langkah berikut:

1. Pastikan seluruh dependensi sudah terinstal:

```bash
pip install -r requirements.txt
```

2. Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

3. Aplikasi akan terbuka otomatis di browser. Isi seluruh input data mahasiswa yang tersedia, lalu klik tombol **"Prediksi Status Mahasiswa"** untuk melihat hasil prediksi apakah mahasiswa tersebut akan **Dropout**, **Enrolled**, atau **Graduate**.

**Link aplikasi di Streamlit Cloud**  
[[Klik untuk membuka aplikasi prediksi dropout mahasiswa](https://dropout-predictor.streamlit.app)]

## Conclusion

Proyek ini berhasil menghasilkan sistem prediksi dan dashboard visual yang dapat digunakan Jaya Jaya Institut untuk menganalisis dan memprediksi dropout mahasiswa secara akurat. Model mampu mengidentifikasi mahasiswa berisiko tinggi berdasarkan data akademik, finansial, dan demografis. Dashboard memperkuat analisis dengan visualisasi yang mudah dipahami oleh manajemen.

### Rekomendasi Action Items

- Memberikan pembimbingan khusus bagi mahasiswa tahun pertama, usia muda, dan lajang.
- Menyusun program pendampingan akademik bagi mahasiswa dengan performa semester pertama rendah.
- Melakukan evaluasi berkala terhadap status pembayaran mahasiswa.
- Mengintegrasikan sistem prediksi ke dalam proses penerimaan dan monitoring internal kampus.
