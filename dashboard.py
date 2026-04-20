import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set header dashboard
st.header('Bike Sharing Dashboard 🚲')

# Load data - Pastikan path file benar sesuai struktur folder kamu
df = pd.read_csv("dashboard/main_data.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# Membuat Sidebar untuk filter
min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    # Mengambil input rentang waktu
    date_range = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Memisahkan start_date dan end_date dari date_input
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range[0]

# --- PERBAIKAN 1: Filtering Tanggal ---
# Menggunakan pd.to_datetime agar sesuai dengan tipe data kolom
main_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & 
             (df["dteday"] <= pd.to_datetime(end_date))]

# --- PERBAIKAN 3: Info Rentang Waktu ---
# Menampilkan informasi tanggal yang sedang difilter
st.write(f"Menampilkan data dari **{start_date}** sampai **{end_date}**")

# --- PERBAIKAN 2: Agregasi Bulanan & Plotting ---
st.subheader('Monthly Rentals Trend')
fig, ax = plt.subplots(figsize=(10, 5))

# Menggunakan resample 'M' (Month) untuk agregasi bulanan yang akurat
monthly_df = main_df.resample(rule='M', on='dteday').agg({
    "cnt": "mean"
}).reset_index()

# Menggunakan kolom 'dteday' sebagai sumbu X agar urutan tanggal benar
sns.lineplot(
    data=monthly_df, 
    x="dteday", 
    y="cnt", 
    marker="o", 
    ax=ax
)

ax.set_xlabel("Tanggal") # Label sumbu X diperbarui
ax.set_ylabel("Rata-rata Penyewa")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# Visualisasi 2: Musim
st.subheader('Season-wise Rentals')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=main_df, x="season", y="cnt", ax=ax, palette="viridis")
ax.set_xlabel("Musim (1:Semi, 2:Panas, 3:Gugur, 4:Dingin)")
ax.set_ylabel("Jumlah Penyewa")
st.pyplot(fig)

st.caption('Copyright (c) Dicoding 2024')