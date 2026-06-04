# 📦 Sistem Prediksi Logistik & Pengiriman

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://logistic-delay-predictor.streamlit.app)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Machine Learning](https://img.shields.io/badge/Machine_Learning-Decision_Tree-FF6F00?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

Sistem Pendukung Keputusan (DSS) berkinerja tinggi untuk memprediksi potensi keterlambatan pengiriman logistik menggunakan algoritma **Decision Tree (Pohon Keputusan)**. Proyek ini mendemonstrasikan keahlian mendalam dalam fundamental Machine Learning dengan membangun algoritma klasifikasi secara murni (*from scratch*) tanpa bergantung pada *library* instan seperti Scikit-Learn.

Dilengkapi dengan antarmuka web *Dashboard* level enterprise yang dibangun menggunakan **Streamlit**, proyek ini menawarkan analitik visual *real-time*, tata letak *Clean & White* eksklusif, dan kemampuan pemrosesan prediktif skala besar.

## ✨ Fitur Unggulan

- **Algoritma Murni (From Scratch)**: Implementasi mandiri matematika dasar AI, mencakup kalkulasi *Shannon Entropy*, *Information Gain*, dan sistem percabangan rekursif.
- **Pemrosesan Massal (Batch Prediction)**: Fitur enterprise untuk mengunggah dataset berformat CSV. Mampu memprediksi status ribuan resi pengiriman hanya dalam hitungan detik.
- **Exploratory Data Analysis (EDA) Terintegrasi**: Visualisasi analitik *Scatter Chart* terintegrasi yang menyorot korelasi antara besaran diskon dan berat paket terhadap kemungkinan terlambat.
- **Antarmuka Visual Premium**: Mengadopsi pedoman UI modern dengan *Custom CSS Variables*, *micro-animations* pada efek *hover*, navigasi berbasis Tab, *Progress Bar* dinamis, dan efek perayaan peramban.
- **Otomatisasi Ekspor Data**: Pengguna dapat mengunduh (*download*) hasil prediksi massal langsung menjadi file rekapitulasi data `.csv`.

## 🛠️ Arsitektur & Teknologi

- **Bahasa Utama**: Python 3.12+
- **Logika Algoritma (Core)**: *Native Python Operations*
- **Pemrosesan Struktur Data**: `pandas`, `collections`, `math`
- **Dashboard Web**: Streamlit (diperkaya dengan *Custom HTML/CSS Injection*)

## 🚀 Panduan Eksekusi Lokal

1. **Kloning Repositori**
   ```bash
   git clone https://github.com/HyLuthfi/logistic-delay-predictor.git
   cd logistic-delay-predictor
   ```

2. **Instalasi Dependensi**
   Direkomendasikan untuk melakukan instalasi di dalam wadah *Virtual Environment*.
   ```bash
   pip install -r requirements.txt
   ```

3. **Menyalakan Server Aplikasi**
   Pastikan dataset utama (`Train.csv`) berada pada ruang direktori yang sama dengan skrip `main.py`.
   ```bash
   streamlit run main.py
   ```

## 📊 Metodologi Model Pembelajaran

Demi memastikan akurasi dan mencegah *Data Leakage*, sistem menggunakan teknik pemisahan silang dengan rasio **80/20 (Data Latih / Data Uji)**. Pohon keputusan dilatih melalui batasan ketat berikut:
- **Metrik Kemurnian**: *Information Gain* tertinggi.
- **Batas Kedalaman Toleransi (Max Depth)**: 10 tingkat bercabang (mengeliminasi risiko *overfitting*).
- **Pembatasan Pemisahan Ekstrem (Min Split)**: Node tidak diizinkan terbelah jika sisa sampel populasi kurang dari 5 residu.

Arsitektur sistem dibangun bukan semata sebagai penyelesaian tugas akhir, namun didesain khusus agar berfungsi mutlak selayaknya platform logistik modern.
