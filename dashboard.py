# mengimport library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='whitegrid')

# load data
day_df = pd.read_csv('dashboard/day_clean.csv')
hour_df = pd.read_csv('dashboard/hour_clean.csv')

# mengubah tipe data dteday pada dataset bike_day
datetime_columns = ['dteday']

for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])

# membuat sidebar
with st.sidebar:
    st.image('https://play-lh.googleusercontent.com/ioeOxqBziipSynHdCTYn0Ayo03jaw0zgPy_tOGChGiyqndXNLetsDw8VGeCswjoTtw')
    st.subheader('🚴Bike-Sharing Dashboard')
    st.divider()
    st.text('Developed for  \n© Dicoding Academy Projects')
    st.caption('By Muhammad Ridlo')


#####################################
# menambahkan main dashboard
st.header('🚴‍♂️Capital Bike Share: Bike-Sharing Dashboard')

tab1, tab2, tab3 = st.tabs(['🚩 About Dataset', '🎯 Project Goals', '🔍 Analysis & Visualization'])

################ About ####################
with tab1:
    st.subheader('🌍 Latar Belakang')
    st.text('Sistem berbagi sepeda adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, ' \
    'penyewaan, hingga pengembalian telah menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari lokasi tertentu' \
    ' dan mengembalikan kembali di lokasi lain. Saat ini, terdapat sekitar lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari ' \
    'lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena perannya yang penting dalam masalah lalu lintas, lingkungan, dan kesehatan.')
    st.text('Selain aplikasi sistem berbagi sepeda yang menarik di dunia nyata, karakteristik data yang dihasilkan oleh sistem ini membuatnya menarik untuk penelitian. ' \
    'Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, durasi perjalanan, posisi keberangkatan, dan kedatangan dicatat secara eksplisit dalam sistem ini. ' \
    'Fitur ini mengubah sistem berbagi sepeda menjadi jaringan sensor virtual yang dapat digunakan untuk mendeteksi mobilitas di kota. Oleh karena itu, diharapkan sebagian besar peristiwa penting di kota dapat dideteksi melalui pemantauan data ini.')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('https://miro.medium.com/v2/resize:fit:825/1*qHz9gP-PCGKrYmRlJgIz_g.jpeg')
    with col2:
        st.image('https://images.ctfassets.net/p6ae3zqfb1e3/3yDdxN8fttP9JUhyLZcQv4/408c9ac285ef77c50d6d9bceee515314/CaBi_Ride_experience_Classic_ride_2x.png?w=1500&q=60&fm=')
    with col3:
        st.image('https://media4.manhattan-institute.org/sites/e21/files/iStock-171300440.jpg')

    st.subheader('📝 Dataset Information')
    st.text('Proses penyewaan sepeda bersama sangat berkorelasi dengan kondisi lingkungan dan musim. Misalnya, kondisi `weather`cuaca, `precipitation` curah hujan, `day of week`, hari dalam seminggu, `season` musim, `hour of the day` jam, dll. dapat memengaruhi perilaku penyewaan.')
    st.code('''Files
    * `hour.csv` : bike sharing counts aggregated on hourly basis (records 17379 hours)
    * `day.csv`  : bike sharing counts aggregated on daily basis (records 731 days)''')

    st.subheader('🧮 Dataset Characteristics')
    st.code('''
    - `instant`    : record index
    - `dteday`     : date
    - `season`     : season (1:springer, 2:summer, 3:fall, 4:winter)
    - `yr`         : year (0: 2011, 1:2012)
    - `mnth`       : month ( 1 to 12)
    - `hr`         : hour (0 to 23)
    - `holiday`    : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
    - `weekday`    : day of the week
    - `workingday` : if day is neither weekend nor holiday is 1, otherwise is 0.
    + `weathersit` : 
	    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
	    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
	    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
	    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
    - `temp`       : Normalized temperature in Celsius. The values are divided to 41 (max)
    - `atemp`      : Normalized feeling temperature in Celsius. The values are divided to 50 (max)
    - `hum`        : Normalized humidity. The values are divided to 100 (max)
    - `windspeed`  : Normalized wind speed. The values are divided to 67 (max)
    - `casual`     : count of casual users
    - `registered` : count of registered users
    - `cnt`        : count of total rental bikes including both casual and registered
    ''')

################ Goals ####################
with tab2:
    st.subheader('Pertanyaan 1')
    st.text('Bagaimana proporsi antara pengguna casual dan registered? Siapa yang lebih banyak menyewa sepeda secara keseluruhan?')
    st.badge('🎯 Goals : Mengetahui distribusi pengguna', color='green')

    st.subheader('Pertanyaan 2')
    st.text('Pada jam berapa puncak tertinggi dan terendah penyewaan sepeda terjadi?')
    st.badge('🎯 Goals : Mengetahui perilaku harian pengguna', color='green')

    st.subheader('Pertanyaan 3')
    st.text('Bagaimana performa penyewaan sepeda pada tahun 2011 dan 2012?')
    st.badge('🎯 Goals : Mengetahui tren pertumbuhan', color='green')

    st.subheader('Pertanyaan 4')
    st.text('Musim manakah yang memiliki jumlah penyewaan sepeda tertinggi dan terendah?')
    st.badge('🎯 Goals : Korelasi musim dengan penyewaan', color='green')

    st.subheader('Pertanyaan 5')
    st.text('Manakah kombinasi faktor cuaca yang menghasilkan jumlah sewa tertinggi dan terendah?')
    st.badge('🎯 Goals : Korelasi cuaca dengan penyewaan', color='green')
############## Visualization ###############
with tab3:
    ######## menampilkan kpi
    st.subheader('🌟 Ringkasan')

    # mendefinisikan data
    total_casual = day_df['casual'].sum()
    total_registered = day_df['registered'].sum()
    total = total_casual+total_registered

    col1, col2, col3 = st.columns(3)
    with col1:
        # kpi total penyewa semua
        st.metric('Total Semua Penyewa', value=total)
    with col2:
        # kpi total penyewa casual
        total_casual = day_df['casual'].sum()
        st.metric('Total Penyewa Casual', value=total_casual)
    with col3:
        # kpi total penyewa registered
        total_registered = day_df['registered'].sum()
        st.metric('Total Penyewa Registered', value=total_registered)


    ######## menampilkan visualisasi proporsi penyewa sepeda
    st.subheader('🚴‍♂️ Proporsi Penyewa Sepeda')
    labels = ['Casual', 'Registered']
    sizes = [total_casual, total_registered]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=["#ffaba4ff",'#ee3123'], autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

    # insight dari visualisasi
    st.badge('💡 Insight',color='green')
    st.text('Pengguna casual dan registered memiliki proporsi 81.2% untuk pengguna Registered dan 18.8% untuk pengguna Casual yang di mana ini dapat diartikan bahwa secara garis besar lebih banyak penyewa sepeda yang terdaftar secara keseluruhan. Jika dilihat secara data, jumlah pengguna casual sebanyak 620.017 pengguna dan pengguna registered sebanyak 2.672.662. Dengan total keseluruhan penyewa sepeda sebanyak 3.292.679.')
    st.badge('🤵‍♂️ Banyak Pengguna Registered')
    st.divider()

    ######## menampilkan visualisasi waktu penyewaan
    st.subheader('⏰ Waktu Penyewaan Sepeda')

    # menghitung pengguna berdasarkan jam
    sum_hour = hour_df.groupby(by = 'hr').cnt.sum().sort_values(ascending=False).reset_index()

    # membuat visualisasi
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(25,10))
    colors0 = ["#ffaba4ff","#ffaba4ff", '#ee3123',"#ffaba4ff","#ffaba4ff",]
    colors1 = ["#ffaba4ff","#ffaba4ff","#ffaba4ff",'#ee3123', "#ffaba4ff",]

    # membuat visualisasi jam penyewaan tertinggi
    sns.barplot(x='hr', y='cnt', data=sum_hour.sort_values(by='cnt', ascending=False).head(5), palette=colors0, hue='hr', legend=False, ax=ax[0])
    ax[0].set_ylabel('Pengguna', fontsize=20)
    ax[0].set_xlabel('Jam (24h)', fontsize=20)
    ax[0].set_title('Jam-Jam Penyewaan Tertinggi', fontsize=25)
    ax[0].tick_params(axis='y', labelsize=18)
    ax[0].tick_params(axis='x', labelsize=18)

    # membuat visualisasi jam penyewaan terendah
    sns.barplot(x='hr', y='cnt', data=sum_hour.sort_values(by='cnt', ascending=True).head(5), palette=colors1, hue='hr', legend=False, ax=ax[1])
    ax[1].set_ylabel('Pengguna', fontsize=20)
    ax[1].set_xlabel('Jam (24h)', fontsize=20)
    ax[1].invert_xaxis()
    ax[1].set_title('Jam-Jam Penyewaan Terendah', fontsize=25)
    ax[1].tick_params(axis='y', labelsize=18)
    ax[1].tick_params(axis='x', labelsize=18)

    st.pyplot(fig)

    # insight dari visualisasi
    st.badge('💡 Insight',color='green')
    st.text('Pengguna yang menyewa sepeda lebih sering menyewa di sore hari antara pukul 16:00 - 19:00 dan puncak tertingginya di pukul 17:00 dengan jumlah pengguna sebanyak 336.860. Sedangkan untuk jam pengguna paling sedikit/terendah menyewa sepeda pada pagi hari di pukul 4:00 dengan jumlah pengguna sebanyak 4.428 dalam rentang waktu tahun 2011-2012.')
    st.badge('🌅Pengguna lebih sering menyewa di sore hari')
    st.divider()

    ######## menampilkan visualisasi performa penyewaan sepeda
    st.subheader('📈 Trend Penyewaaan Sepeda')

    # menghitung performa penyewaan sepeda tahun 2011
    data_2011 = day_df[day_df['dteday'].dt.year == 2011]
    data_2011.set_index('dteday', inplace=True)
    monthly_2011 = data_2011['cnt'].resample('M').sum().reset_index()

    # menghitung performa penyewaan tahun 2012
    data_2012 = day_df[day_df['dteday'].dt.year == 2012]
    data_2012.set_index('dteday', inplace = True)
    monthly_2012 = data_2012['cnt'].resample('M').sum().reset_index()

    # membuat visualisasi
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24,10))

    # membuat visualisasi tahun 2011
    sns.lineplot(x='dteday', y='cnt', data=monthly_2011, marker='o', color='#ee3123', ax=ax[0])
    ax[0].set_ylabel('Pengguna', fontsize=20)
    ax[0].set_xlabel('Bulan', fontsize=20)
    ax[0].set_title('Performa Penyewaan Sepeda Tahun 2011', fontsize=25)
    ax[0].tick_params(axis = 'y', labelsize=18)
    ax[0].tick_params(axis = 'x', labelsize=15)

    # membuat visualisasi tahun 2012
    sns.lineplot(x='dteday', y='cnt', data=monthly_2012, marker='o', color='#ee3123', ax=ax[1])
    ax[1].set_ylabel('Pengguna', fontsize=20)
    ax[1].set_xlabel('Bulan', fontsize=20)
    ax[1].set_title('Performa Penyewaan Sepeda Tahun 2012', fontsize=25)
    ax[1].tick_params(axis = 'y', labelsize=18)
    ax[1].tick_params(axis = 'x', labelsize=15)

    st.pyplot(fig)

    # insight dari visualisasi
    st.badge('💡 Insight', color='green')
    st.markdown("""
    - Pada tahun 2011, bulan Januari sampai Maret merupakan bulan dengan performa penyewaan terendah dengan range penyewaan antara 35.000 - 65.000 pengguna. Kemudian di bulan selanjutnya angka pengguna yang meminjam sepeda perlahan naik hingga berada di titik penyewaan tertinggi pada bulan Juni dengan jumlah penyewaan sebanyak 143.512 pengguna.
    - Pada tahun 2012, masih sama dengan tahun sebelumnya, bulan Januari sampai Maret merupakan bulan dengan performa penyewaan terendah dengan range penyewaan antara 95.000 - 165.000 pengguna. Kemudian di bulan selanjutnya angka pengguna yang meminjam sepeda meningkat secara tajam hingga berada di titik penyewaan tertinggi pada bulan September dengan jumlah penyewaan sebanyak 218.573 pengguna.
    """)
    st.badge('🗓️ Januari-Maret memiliki performa penyewaan terendah di kedua tahun')
    st.badge('📅 Juni 2011 & September 2012 memiliki performa penyewaan tertinggi')
    st.divider()

    ######## menampilkan visualisasi faktor musim
    st.subheader('☁️ Faktor Musim Terhadap Penyewaan Sepeda')

    # menghitung jumlah penyewaan berdasarkan musim
    season = day_df.groupby(by = 'season').cnt.sum().reset_index()

    # membuat visualisasi
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ['#ee3123', "#ffaba4ff","#ffaba4ff", "#ffaba4ff", "#ffaba4ff",]

    sns.barplot(x='season', y='cnt', data=season, palette=colors, legend=False)
    ax.set_ylabel('Pengguna', fontsize=20)
    ax.set_xlabel('Musim', fontsize=20)
    ax.tick_params(axis='y', labelsize=18)
    ax.tick_params(axis='x', labelsize=18)
    
    st.pyplot(fig)

    # insight dari visualisasi
    st.badge('💡 Insight', color='green')
    st.text('Musim gugur atau Fall Season merupakan musim di mana pengguna paling tinggi menyewa sepeda dengan jumlah sebnyak 1.061.129. Sedangkan untuk musim dengan penyewaan sepeda paling rendah yaitu pada musim semi Spring Season dengan jumlah sebanyak 471.348')
    st.badge('🍁 Pengguna lebih sering menyewa sepeda di Fall Season')
    st.badge('🌹 Pengguna jarang menyewa sepeda di Spring Season')
    st.divider()

    ######## menampilkan visualisasi faktor cuaca
    st.subheader('🌥️ Faktor Cuaca Terhadap Penyewaan Sepeda')
    
    # menghitung jumlah penyewaan berdasarkan cuaca
    weathersit = day_df.groupby(by = 'weathersit').cnt.sum().reset_index()

    # membuat visualisasi
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ['#ee3123', "#ffaba4ff","#ffaba4ff", "#ffaba4ff", "#ffaba4ff",]

    sns.barplot(x='weathersit', y='cnt', data=weathersit, palette=colors, legend=False)
    ax.set_ylabel('Pengguna', fontsize=20)
    ax.set_xlabel('Cuaca', fontsize=20)
    ax.tick_params(axis='y', labelsize=18)
    ax.tick_params(axis='x', labelsize=18)
    
    st.pyplot(fig)

    # insight dari visualisasi
    st.badge('💡 Insight', color='green')
    st.text('Faktor cuaca cerah atau clear menghasilkan jumlah penyewa sepeda tertinggi diantara empat musim lainnya, yaitu sebanyak 2.338.173 pengguna pada periode tahun 2011-2012. Sedangkan untuk faktor cuaca hujan deras atau heavy rain menghasilkan jumlah penyewa sepeda terendah, yaitu sebanyak 223 pengguna')
    st.badge('⛅ Cuaca cerah (clear) membuat orang banyak menyewa sepeda')
    st.badge('🌧️ Cuaca hujan deras (heavy rain) membuat orang jarang untuk menyewa sepeda')