import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='white')

# Judul aplikasi
st.title("Dashboard Analisis Data Kualitas Udara di Stasiun China")

# Deskripsi
st.markdown("""
Dashboard ini menampilkan analisis visual dari rata-rata suhu per stasiun 
dan konsentrasi karbon monoksida (CO) per tahun.
""")

# Load data
@st.cache_data
def load_data():
    # Ganti file path dengan file yang sesuai
    file_path = 'combined_df.csv'
    return pd.read_csv(file_path)

data = load_data()

# Membuat dataframe gabungan
combined_df = data.copy()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("logo.jpg")

# Data 1: Rata-rata suhu per stasiun
st.subheader("Data 1: Stasiun dengan Rata-Rata Suhu Tertinggi")

# Kelompokkan data berdasarkan stasiun dan hitung rata-rata suhu
temp_by_station = combined_df.groupby(by="station").agg({"TEMP": "mean"}).reset_index()
temp_by_station_sorted = temp_by_station.sort_values(by="TEMP", ascending=False)

# Plot
plt.figure(figsize=(10, 5))
sns.barplot(y="station", x="TEMP", data=temp_by_station_sorted)
plt.title("Stasiun Dengan Rata-Rata Suhu Tertinggi", loc="center", fontsize=15)
plt.xlabel('Temperature (°C)')
plt.ylabel('Station')
st.pyplot(plt)

# Data 2: Kenaikan gas karbon (CO) per tahun
st.subheader("Data 2: Kenaikan Gas Karbon (CO) per Tahun")

# Kelompokkan data berdasarkan tahun dan hitung rata-rata konsentrasi CO
co_per_year = combined_df.groupby('year').agg({'CO': 'mean'}).reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='CO', data=co_per_year, marker='o', color='b')
plt.title('Kenaikan Gas Karbon (CO) per Tahun', fontsize=16)
plt.xlabel('Tahun')
plt.ylabel('Konsentrasi CO (mg/m³)')
plt.grid(True)
st.pyplot(plt)

st.caption('Copyright © Ifan Hakim 2024')