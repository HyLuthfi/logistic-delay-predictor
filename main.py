import os
import pandas as pd
from collections import Counter
import math
import random
import time
import streamlit as st

st.set_page_config(
    page_title="Prediksi Keterlambatan Paket",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS: Clean, White, Symmetrical, Centered Navbar + Interactive Hover
css_kustom = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #FAFAFA;
        color: #111827;
    }
    
    .stApp {
        background-color: #FAFAFA;
    }

    /* TABS NAVBAR STYLING - CENTERED */
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        gap: 30px;
        border-bottom: 1px solid #E5E7EB;
        padding-bottom: 10px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 0px;
        padding: 10px 15px;
        color: #6B7280;
        font-weight: 600;
        font-size: 1.1rem;
        border: none !important;
        transition: all 0.3s;
    }
    
    .stTabs [aria-selected="true"] {
        color: #111827 !important;
        border-bottom: 3px solid #111827 !important;
        background-color: transparent !important;
    }

    /* Card styling for modern white look */
    .metric-card {
        background-color: #FFFFFF;
        color: #111827 !important;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 32px 24px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .info-card {
        background-color: #FFFFFF;
        color: #111827 !important;
        border: 1px solid #E5E7EB;
        border-left: 4px solid #111827;
        border-radius: 8px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }

    /* Interactive Hover Effects (Upgrade) */
    .metric-card:hover, .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        border-color: #D1D5DB;
    }

    /* Gradient Typography */
    .gradient-text {
        background: linear-gradient(135deg, #111827 0%, #4B5563 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
        font-weight: 700 !important;
    }

    /* Premium Animated Button */
    .stButton > button {
        background: linear-gradient(135deg, #111827 0%, #374151 100%);
        color: white;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #000000 0%, #111827 100%);
        transform: scale(1.02) translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        color: white;
    }
    
    .status-aman {
        color: #065F46;
        background-color: #D1FAE5;
        padding: 6px 20px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
        border: 1px solid #A7F3D0;
    }
    
    .status-bahaya {
        color: #991B1B;
        background-color: #FEE2E2;
        padding: 6px 20px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
        border: 1px solid #FECACA;
    }
    
    hr {
        border-color: #E5E7EB;
        margin: 2rem 0;
    }
    
    p, li {
        font-size: 1.05rem;
        line-height: 1.7;
        color: #374151;
    }
</style>
"""
st.markdown(css_kustom, unsafe_allow_html=True)

@st.cache_data
def muat_dan_siapkan_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "Train.csv")
    data_asli = pd.read_csv(file_path)
    data = data_asli.drop(columns=["ID", "Customer_rating"])
    
    kolom_label = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
    pemetaan_label = {}
    for kolom in kolom_label:
        nilai_unik = data[kolom].unique()
        pemetaan_label[kolom] = {v: i for i, v in enumerate(nilai_unik)}
        data[kolom] = data[kolom].map(pemetaan_label[kolom])
        
    fitur = list(data.columns[:-1])
    data_fitur = data[fitur].values.tolist()
    data_target = data["Reached.on.Time_Y.N"].tolist()
    data_gabungan = [x + [y] for x, y in zip(data_fitur, data_target)]
    
    return data_asli, data_gabungan, fitur, pemetaan_label

def bagi_data(data, rasio_uji=0.2, acak_seed=42):
    random.seed(acak_seed)
    data_acak = data[:]
    random.shuffle(data_acak)
    titik_bagi = int(len(data_acak) * (1 - rasio_uji))
    return data_acak[:titik_bagi], data_acak[titik_bagi:]

def entropi(baris):
    total = len(baris)
    jumlah_kelas = Counter(r[-1] for r in baris)
    return -sum((jumlah / total) * math.log2(jumlah / total) for jumlah in jumlah_kelas.values() if jumlah)

def bagi(baris, kolom, nilai):
    if isinstance(nilai, (int, float)):
        kiri = [r for r in baris if r[kolom] <= nilai]
        kanan = [r for r in baris if r[kolom] > nilai]
    else:
        kiri = [r for r in baris if r[kolom] == nilai]
        kanan = [r for r in baris if r[kolom] != nilai]
    return kiri, kanan

def keuntungan_info(baris, kolom, nilai):
    kiri, kanan = bagi(baris, kolom, nilai)
    if not kiri or not kanan:
        return 0
    proporsi = len(kiri) / len(baris)
    return entropi(baris) - (proporsi * entropi(kiri) + (1 - proporsi) * entropi(kanan))

def cari_pemisah_terbaik(baris):
    terbaik_gain = 0
    kolom_terbaik = None
    nilai_terbaik = None
    for k in range(len(baris[0]) - 1):
        nilai_unik = set(r[k] for r in baris)
        for v in nilai_unik:
            gain = keuntungan_info(baris, k, v)
            if gain > terbaik_gain:
                terbaik_gain, kolom_terbaik, nilai_terbaik = gain, k, v
    return terbaik_gain, kolom_terbaik, nilai_terbaik

@st.cache_resource
def latih_pohon(data_latih):
    def bangun_pohon(baris, kedalaman=0, maks_kedalaman=10, min_split=5):
        label = [r[-1] for r in baris]
        if label.count(label[0]) == len(label):
            return label[0]
        if len(baris) < min_split or kedalaman >= maks_kedalaman:
            return Counter(label).most_common(1)[0][0]
        gain, kolom, nilai = cari_pemisah_terbaik(baris)
        if gain == 0:
            return Counter(label).most_common(1)[0][0]
        kiri, kanan = bagi(baris, kolom, nilai)
        return {
            'kolom': kolom,
            'nilai': nilai,
            'kiri': bangun_pohon(kiri, kedalaman + 1, maks_kedalaman, min_split),
            'kanan': bangun_pohon(kanan, kedalaman + 1, maks_kedalaman, min_split)
        }
    return bangun_pohon(data_latih)

def prediksi(baris, simpul):
    if not isinstance(simpul, dict):
        return simpul
    nilai = baris[simpul['kolom']]
    arah = simpul['kiri'] if nilai <= simpul['nilai'] else simpul['kanan']
    return prediksi(baris, arah)

def evaluasi(data_uji, pohon):
    aktual = [r[-1] for r in data_uji]
    prediksi_ = [prediksi(r, pohon) for r in data_uji]
    tp = sum((a == 1 and p == 1) for a, p in zip(aktual, prediksi_))
    tn = sum((a == 0 and p == 0) for a, p in zip(aktual, prediksi_))
    fp = sum((a == 0 and p == 1) for a, p in zip(aktual, prediksi_))
    fn = sum((a == 1 and p == 0) for a, p in zip(aktual, prediksi_))
    akurasi = (tp + tn) / len(aktual)
    presisi = tp / (tp + fp + 1e-10)
    recall = tp / (tp + fn + 1e-10)
    f1 = 2 * presisi * recall / (presisi + recall + 1e-10)
    return akurasi, presisi, recall, f1

def utama():
    st.markdown("<h1 class='gradient-text' style='text-align: center; margin-top: 1rem;'>Sistem Prediksi Logistik & Pengiriman</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1rem; color: #6B7280; margin-bottom: 2rem;'>Sistem Pendukung Keputusan Berbasis Algoritma Decision Tree</p>", unsafe_allow_html=True)
    
    try:
        data_asli, data_gabungan, fitur, pemetaan_label = muat_dan_siapkan_data()
    except FileNotFoundError:
        st.error("Dataset 'Train.csv' tidak ditemukan. Pastikan file berada di direktori yang sama.")
        return
        
    data_latih, data_uji = bagi_data(data_gabungan)
    
    with st.spinner("Menginisialisasi model..."):
        pohon = latih_pohon(data_latih)
        akurasi, presisi, recall, f1 = evaluasi(data_uji, pohon)

    tab_prediksi, tab_batch, tab_analisis, tab_metodologi = st.tabs([
        "Prediksi Tunggal", 
        "Prediksi Massal (CSV)",
        "Hasil Analisis Data", 
        "Metodologi"
    ])

    with tab_prediksi:
        st.markdown("<br>", unsafe_allow_html=True)
        kolom_kiri, kolom_tengah, kolom_kanan = st.columns([1, 2, 1])
        with kolom_tengah:
            st.markdown("<div class='info-card'><b>Instruksi Operasional:</b> Masukkan spesifikasi paket pengiriman secara lengkap pada form di bawah ini untuk memprediksi potensi keterlambatan.</div>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                warehouse = st.selectbox("Blok Gudang", list(pemetaan_label['Warehouse_block'].keys()))
                shipment = st.selectbox("Moda Pengiriman", list(pemetaan_label['Mode_of_Shipment'].keys()))
                importance = st.selectbox("Prioritas Produk", list(pemetaan_label['Product_importance'].keys()))
                gender = st.selectbox("Gender Klien", list(pemetaan_label['Gender'].keys()))
                
            with c2:
                calls = st.number_input("Jumlah Panggilan CS", min_value=0, max_value=10, value=3)
                cost = st.number_input("Harga Produk (USD)", min_value=0, max_value=1000, value=150)
                purchases = st.number_input("Riwayat Pembelian", min_value=0, max_value=20, value=3)
                discount = st.number_input("Diskon Diberikan (%)", min_value=0, max_value=100, value=10)
                weight = st.number_input("Berat Paket (Gram)", min_value=0, max_value=10000, value=1500)

            st.markdown("<br>", unsafe_allow_html=True)
            tombol_prediksi = st.button("Jalankan Prediksi Pengiriman")

            if tombol_prediksi:
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Laporan Hasil Prediksi</h2>", unsafe_allow_html=True)
                
                input_data = [
                    pemetaan_label['Warehouse_block'][warehouse],
                    pemetaan_label['Mode_of_Shipment'][shipment],
                    calls,
                    cost,
                    purchases,
                    pemetaan_label['Product_importance'][importance],
                    pemetaan_label['Gender'][gender],
                    discount,
                    weight
                ]
                
                hasil = prediksi(input_data, pohon)
                
                status_kelas = "status-bahaya" if hasil == 1 else "status-aman"
                teks_kelas = "TERLAMBAT" if hasil == 1 else "TEPAT WAKTU"
                deskripsi = "Paket diprediksi akan mengalami keterlambatan dari jadwal yang ditentukan." if hasil == 1 else "Paket diprediksi akan tiba tepat waktu sesuai jadwal pengiriman."
                
                # Interaksi Notifikasi Toast (Upgrade)
                if hasil == 0:
                    st.toast("Prediksi Aman! Paket akan tiba tepat waktu.", icon="✅")
                else:
                    st.toast("Peringatan Keterlambatan! Evaluasi ulang rute.", icon="⚠️")

                st.markdown(f"""
                <div class='metric-card' style='margin-bottom: 2rem;'>
                    <h3 style='color: #374151; font-size: 1.2rem; margin-bottom: 1.5rem;'>Status Pengiriman</h3>
                    <div style='margin-bottom: 1.5rem;'>
                        <span class='{status_kelas}'>{teks_kelas}</span>
                    </div>
                    <p style='margin: 0; font-size: 0.95rem; color: #4B5563;'>{deskripsi}</p>
                </div>
                """, unsafe_allow_html=True)

    with tab_batch:
        st.markdown("<div style='padding: 1rem 3rem;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center;'>Pemrosesan Prediksi Skala Besar (Batch)</h2>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        
        st.markdown("<div class='info-card'><b>Fitur Enterprise:</b> Unggah dataset yang berisi ratusan atau ribuan data resi pengiriman sekaligus dalam format CSV. Sistem akan memproses prediksi secara otomatis dalam hitungan detik.</div>", unsafe_allow_html=True)
        
        berkas_unggah = st.file_uploader("Unggah file CSV pengiriman (Format mengikuti Train.csv)", type=['csv'])
        
        if berkas_unggah is not None:
            df_batch = pd.read_csv(berkas_unggah)
            st.write("Pratinjau Data Unggahan:")
            st.dataframe(df_batch.head(3))
            
            if st.button("Eksekusi Prediksi Massal", type="primary"):
                # Interaksi Progress Bar (Upgrade)
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                with st.spinner("Memproses ribuan data..."):
                    hasil_batch = []
                    total_data = len(df_batch)
                    
                    for index, baris_data in df_batch.iterrows():
                        # Simulasi loading ringan & update progress
                        if index % max(1, total_data // 100) == 0:
                            progress_bar.progress(min(1.0, index / total_data))
                            status_text.text(f"Menganalisis baris {index+1} dari {total_data}...")
                            
                        try:
                            baris_input = [
                                pemetaan_label['Warehouse_block'][baris_data['Warehouse_block']],
                                pemetaan_label['Mode_of_Shipment'][baris_data['Mode_of_Shipment']],
                                baris_data['Customer_care_calls'],
                                baris_data['Cost_of_the_Product'],
                                baris_data['Prior_purchases'],
                                pemetaan_label['Product_importance'][baris_data['Product_importance']],
                                pemetaan_label['Gender'][baris_data['Gender']],
                                baris_data['Discount_offered'],
                                baris_data['Weight_in_gms']
                            ]
                            pred_val = prediksi(baris_input, pohon)
                            hasil_batch.append("Terlambat" if pred_val == 1 else "Tepat Waktu")
                        except Exception as e:
                            hasil_batch.append("Data Tidak Valid")
                            
                    progress_bar.progress(1.0)
                    status_text.empty()
                    
                    df_batch['Status Prediksi'] = hasil_batch
                    
                    # Interaksi Balloons Sukses (Upgrade)
                    st.balloons()
                    st.success("Pemrosesan massal berhasil diselesaikan!")
                    
                    st.write("Hasil Prediksi (Pratinjau 10 Baris Pertama):")
                    st.dataframe(df_batch.head(10))
                    
                    csv_hasil = df_batch.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Unduh Rekapitulasi Prediksi (CSV)",
                        data=csv_hasil,
                        file_name='Laporan_Prediksi_Massal.csv',
                        mime='text/csv',
                    )
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_analisis:
        st.markdown("<div style='padding: 1rem 3rem;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center;'>Evaluasi Kinerja Model & Analisis Data</h2>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #374151; font-size: 1.2rem; margin-bottom: 1.5rem;'>Akurasi Keseluruhan</h3>
                <h2 style='margin: 0 0 1.5rem 0; color: #111827;'>{akurasi*100:.2f}%</h2>
                <div style='background-color: #F3F4F6; padding: 10px; border-radius: 6px; display: inline-block;'>
                    <span style='font-size: 0.85rem; color: #4B5563;'>Proporsi prediksi benar terhadap total data uji</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #374151; font-size: 1.2rem; margin-bottom: 1.5rem;'>F1-Score (Harmonik)</h3>
                <h2 style='margin: 0 0 1.5rem 0; color: #111827;'>{f1:.3f}</h2>
                <div style='background-color: #F3F4F6; padding: 10px; border-radius: 6px; display: inline-block;'>
                    <span style='font-size: 0.85rem; color: #4B5563;'>Keseimbangan antara Presisi ({presisi:.2f}) dan Recall ({recall:.2f})</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Korelasi Diskon dan Berat Paket Terhadap Keterlambatan")
        st.markdown("Eksplorasi visual di bawah ini menunjukkan sebaran 500 sampel acak. Paket yang mendapat **diskon besar** berpotensi tinggi untuk **Terlambat**, sedangkan berat paket membentuk kluster tertentu.")
        
        df_viz = data_asli.copy()
        df_viz['Status Pengiriman'] = df_viz['Reached.on.Time_Y.N'].map({0: 'Tepat Waktu', 1: 'Terlambat'})
        st.scatter_chart(
            df_viz.sample(500, random_state=42), 
            x='Discount_offered', 
            y='Weight_in_gms', 
            color='Status Pengiriman',
            height=400
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_metodologi:
        st.markdown("<div style='padding: 1rem 3rem;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center;'>Metodologi & Parameter Algoritma</h2>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        
        st.markdown("""
        ### Pendekatan Konseptual
        Sistem ini dirancang murni *from scratch* (tanpa campur tangan *library* seperti `scikit-learn`). Logika pembangunan pohon keputusan dikembangkan menggunakan kalkulasi kemurnian cabang secara rekursif, menjadikannya proyek portofolio yang sangat fundamental.
        
        ### Metrik Pembentukan Model (Tree Splitting)
        - **Pengukuran Impuritas**: Menggunakan *Shannon Entropy* untuk mengukur ketidakpastian distribusi probabilitas antar kelas.
        - **Kriteria Pemisahan (Split Criterion)**: Memilih fitur (kolom) dengan bobot *Information Gain* terbesar untuk memaksimalkan kepastian pada sub-simpul (kiri/kanan).
        - **Regulasi Kedalaman (Max Depth)**: Model dibatasi maksimum 10 level ke bawah untuk menghambat fenomena penghafalan data (*overfitting*).
        - **Batas Henti (Min Split)**: Node berhenti bercabang jika sisa sampel kurang dari 5 baris data.
        
        ### Arsitektur Evaluasi Silang
        Dataset mentah dipecah dan diajak menggunakan teknik `random.shuffle()` dengan rasio stabil:
        - **80% untuk Fase Pelatihan (Training)**: Menciptakan jutaan probabilitas aturan klasifikasi.
        - **20% untuk Fase Pengujian (Testing)**: Validasi objektif di luar ruang pelatihan.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    utama()
