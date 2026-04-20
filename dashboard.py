import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set header dashboard
st.header('Bike Sharing Dashboard 🚲')

# Load data
df = df = pd.read_csv("main_data.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# Membuat Sidebar untuk filter (Opsional tapi bagus untuk nilai)
min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data
main_df = df[(df["dteday"] >= str(start_date)) & 
                (df["dteday"] <= str(end_date))]

# Visualisasi 1: Tren Bulanan
st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(10, 5))
monthly_df = main_df.groupby(by="mnth").agg({"cnt": "mean"})
sns.lineplot(data=monthly_df, x=monthly_df.index, y="cnt", marker="o", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata Penyewa")
st.pyplot(fig)

# Visualisasi 2: Musim (Tambahan agar dashboard lebih ramai)
st.subheader('Season-wise Rentals')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=main_df, x="season", y="cnt", ax=ax)
ax.set_xlabel("Musim (1:Semi, 2:Panas, 3:Gugur, 4:Dingin)")
ax.set_ylabel("Jumlah Penyewa")
st.pyplot(fig)

st.caption('Copyright (c) Dicoding 2024')