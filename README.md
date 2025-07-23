# 🚲 Bike Sharing Analysis

## 🌍 Background 
Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, hingga pengembalian menjadi otomatis melalui sistem. Beroperasinya layanan ini juga menghasilkan karakteristik data yang menarik untuk dibuat analisis dan penelitian. Dengan itu, proyek ini bertujuan untuk menganalisis data yang dihasilkan dan mencari insight atau wawasan yang bermanfaat.

## 📝 Dataset Information
Dataset ini berisi dua file yaitu `hour.csv` dan `day.csv` dengan detail sebagai berikut
```
hour.csv : bike sharing counts aggregated on hourly basis (records 17379 hours)
day.csv  : bike sharing counts aggregated on daily basis (records 731 days)
```
## 🔍 Analysis & Insight
### Mendefinisikan Pertanyaan
1. Bagaimana proporsi antara pengguna casual dan registered? Siapa yang lebih banyak menyewa sepeda secara keseluruhan?
2. Pada jam berapa puncak tertinggi dan terendah penyewaan sepeda terjadi?
3. Bagaimana performa penyewaan sepeda pada tahun 2011 dan 2012?
4. Musim manakah yang memiliki jumlah penyewaan sepeda tertinggi dan terendah?
5. Manakah kombinasi faktor cuaca yang menghasilkan jumlah sewa tertinggi dan terendah

### Insight yang Didapat
1. Pengguna casual dan registered memiliki proporsi 81.2% untuk pengguna Registered dan 18.8% untuk pengguna Casual yang di mana ini dapat diartikan bahwa secara garis besar lebih banyak penyewa sepeda yang terdaftar secara keseluruhan.
2. Pengguna yang menyewa sepeda lebih sering menyewa di sore hari antara pukul 16:00 - 19:00 dan puncak tertingginya di pukul 17:00. Sedangkan untuk jam pengguna paling sedikit/terendah menyewa sepeda pada pagi hari di pukul 4:00.
3. Pada tahun 2011, bulan Januari sampai Maret merupakan bulan dengan performa penyewaan terendah dan penyewaan tertinggi pada bulan Juni. Sedangkan pada tahun 2012, masih sama dengan tahun sebelumnya, performa penyewaan terendah terjadi pada bulan Januari sampai Maret dan penyewaan tertinggi pada bulan September.
4. Musim gugur atau Fall Season merupakan musim di mana pengguna paling tinggi menyewa sepeda. Sedangkan untuk musim dengan penyewaan sepeda paling rendah yaitu pada musim semi atau Spring Season.
5. Faktor cuaca cerah atau clear menghasilkan jumlah penyewa sepeda tertinggi diantara empat musim lainnya pada periode tahun 2011-2012. Sedangkan untuk faktor cuaca hujan deras atau heavy rain menghasilkan jumlah penyewa sepeda terendah.

📌 Detail proses analisis data terdokumentasi dalam notebook python berikut
[notebook.ipynb](https://github.com/mhmmdridlo/bike-sharing/blob/30262b52fa5cbdf0a45ca0d56526da7f30d26f24/notebook.ipynb)

## 📊 Dashboard Streamlit

<p align='center'>
  <img src='/images/dashboard-visualization.png'/>
  🖼️ Tampilan Dashboard

### Streamlit Cloud
Dashboard pada proyek ini sudah di deploy ke dalam Streamlit Cloud, untuk melihat dashboard secara langsung bisa melalui link berikut ini 

🔗 https://bike-sharing-mhmmdridloo.streamlit.app/

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
