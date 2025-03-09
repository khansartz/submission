import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

# Grouping data berdasarkan season
byseason_df = all_df.groupby(by="season").agg({"cnt": "sum"}).reset_index()
byseason_df.rename(columns={"cnt": "total_rentals"}, inplace=True)

# Ubah format angka menjadi nama musim
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]

# Buat Grafik di Matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    y="total_rentals",
    x="season",
    data=byseason_df.sort_values(by="total_rentals", ascending=False),
    palette=colors,
    ax=ax
)

ax.set_xticklabels([season_labels[season] for season in byseason_df["season"]])
ax.set_title("Total Penyewaan Sepeda Tiap Musim", loc="center", fontsize=15)
ax.set_ylabel(None)

# Tampilkan di Streamlit
st.title("Analisis Penyewaan Sepeda")
st.pyplot(fig)