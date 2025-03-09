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
    st.image("data:image/png;base64,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")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

st.header('Bike Sharing :bike:')

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
st.header("Penyewaan Sepeda per Musim")
st.pyplot(fig)

st.header("Total Penyewaan Sepeda Tiap Bulan")

monthly_rentals_df = all_df.groupby(by=["yr", "mnth"]).agg({"cnt": "sum"}).reset_index()

# Ubah format angka menjadi tahun
monthly_rentals_df["yr"] = monthly_rentals_df["yr"].map({0: "2011", 1: "2012"})

# Ubah format angka menjadi nama bulan
month_map = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}
monthly_rentals_df["mnth"] = monthly_rentals_df["mnth"].map(month_map)

# Buat Grafik
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.lineplot(
    data=monthly_rentals_df,
    x="mnth",
    y="cnt",
    hue="yr",
    marker='o',
    linewidth=2,
    palette=["#f5cc16", "blue"],
    ax=ax2
)

ax2.set_title("Total Penyewaan Sepeda Tiap Bulan", loc="center", fontsize=15)
ax2.set_xlabel(None)
ax2.set_ylabel("Total Sewa")
ax2.set_xticklabels(monthly_rentals_df["mnth"].unique(), rotation=45)
ax2.legend(title="Tahun")
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Tampilkan di Streamlit
st.pyplot(fig2)

st.header("Rata-rata Penyewaan Sepeda per Musim dan Cuaca")
df_cluster = all_df.copy()
df_grouped = df_cluster.groupby(["season", "weathersit"]).agg({"cnt": "mean"}).reset_index()
df_grouped.rename(columns={"cnt": "avg_rentals"}, inplace=True)

# Bikin 2 kolom
col1, col2 = st.columns(2)

# Grafik 1: Rata-rata Penyewaan per Musim
fig3, ax3 = plt.subplots(figsize=(5, 5))
colors_season = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
sns.barplot(x="season", y="avg_rentals", data=df_grouped, palette=colors_season, errorbar=None, ax=ax3)
ax3.set_title("Rata-rata Penyewaan Sepeda per Musim", fontsize=13)
ax3.set_xlabel("Musim")
ax3.set_ylabel("Rata-rata Penyewaan")
ax3.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])

# Grafik 2: Rata-rata Penyewaan Berdasarkan Cuaca
fig4, ax4 = plt.subplots(figsize=(5, 5))
colors_weathersit = ["#446DD4", "#dae1f5", "#dae1f5", "#dae1f5"]
sns.barplot(x="weathersit", y="avg_rentals", data=df_grouped, palette=colors_weathersit, errorbar=None, ax=ax4)
ax4.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca", fontsize=13)
ax4.set_xlabel("Cuaca")
ax4.set_ylabel("Rata-rata Penyewaan")
ax4.set_xticklabels(["Cerah", "Mendung", "Hujan Ringan", "Hujan Deras"])

# Tampilkan di Streamlit (2 Grafik dalam 1 Baris)
col1.pyplot(fig3)
col2.pyplot(fig4)