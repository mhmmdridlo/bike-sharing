# 🚲 Bike Sharing Analysis

## 🌍 Background 
Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, hingga pengembalian menjadi otomatis melalui sistem. Beroperasinya layanan ini juga menghasilkan karakteristik data yang menarik untuk dibuat analisis dan penelitian. Dengan itu, proyek ini bertujuan untuk menganalisis data yang dihasilkan dan mencari insight atau wawasan yang bermanfaat.

## 📝 Dataset Information
Dataset ini berisi dua file yaitu `hour.csv` dan `day.csv` dengan detail sebagai berikut
```
hour.csv : bike sharing counts aggregated on hourly basis (records 17379 hours)
day.csv  : bike sharing counts aggregated on daily basis (records 731 days)
```

## 📊 Dashboard Streamlit

<p align='center'>
  <img src='/images/dashboard-visualization.png'/>
  🖼️ Tampilan Dashboard

### Streamlit Cloud
Dashboard pada proyek ini sudah di deploy ke dalam Streamlit Cloud, untuk melihat dashboard secara langsung bisa melalui link berikut ini 🔗 https://bike-sharing-mhmmdridloo.streamlit.app/

### Streamlit Local
Setup environment terlebih dahulu dengan perintah seperti di bawah, environment ini menggunakan Anaconda
```
conda create --name python-data python=3.9
conda activate python-data
pip install -r requirements.txt
```
Setelah itu jalankan dashboard streamlit dengan menggunakan perintah seperti di bawah
```
streamlit run dashboard.py
```
