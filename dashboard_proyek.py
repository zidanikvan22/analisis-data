import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
top_10_cities = pd.read_csv("top_10_cities.csv")
bottom_5_cities = pd.read_csv("bottom_5_cities.csv")
top_10_states = pd.read_csv("top_10_states.csv")
bottom_5_states = pd.read_csv("bottom_5_states.csv")
top_10_products = pd.read_csv("top_10_products.csv")
bottom_10_products = pd.read_csv("bottom_10_products.csv")
monthly_sales = pd.read_csv("monthly_sales.csv")

# Judul dashboard
st.title("Dashboard proyek akhir")

# **Visualisasi Tren Penjualan Bulanan**
# Set tema seaborn
sns.set_theme(style="whitegrid")

# Buat subheader
st.subheader("Tren Total Order dan Revenue per Bulan")

# Ukuran figure
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot total orders sebagai bar chart
sns.barplot(data=monthly_sales, 
            x="order_purchase_timestamp", 
            y="total_orders", 
            color="skyblue", 
            label="Total Orders", 
            ax=ax1)

# Buat sumbu y kedua untuk revenue
ax2 = ax1.twinx()
sns.lineplot(data=monthly_sales, 
             x="order_purchase_timestamp", 
             y="total_revenue", 
             marker="o", 
             color="red", 
             linewidth=2, 
             label="Total Revenue", 
             ax=ax2)

# Label dan judul
ax1.set_xlabel("Bulan", fontsize=12)
ax1.set_ylabel("Jumlah Order", fontsize=12, color="blue")
ax2.set_ylabel("Total Revenue (Rp)", fontsize=12, color="red")
plt.title("Tren Total Order dan Revenue per Bulan", fontsize=14)

# Rotasi label x agar lebih rapi
plt.xticks(rotation=45)

# Tambahkan legenda
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Menampilkan data dalam tabel
st.subheader("Data Penjualan Bulanan")
st.dataframe(monthly_sales)

# **Visualisasi Top 10 Kota dengan Pelanggan Terbanyak**
st.subheader("Top 10 Kota dengan Pelanggan Terbanyak")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(y=top_10_cities["customer_city"], x=top_10_cities["customer_count"], palette="Blues_r", ax=ax)
ax.set_xlabel("Jumlah Pelanggan")
ax.set_ylabel("Kota")
ax.set_title("Top 10 Kota dengan Pelanggan Terbanyak")
st.pyplot(fig)

# **Visualisasi Bottom 5 Kota dengan Pelanggan Paling Sedikit**
st.subheader("Bottom 5 Kota dengan Pelanggan Paling Sedikit")
fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(y=bottom_5_cities["customer_city"], x=bottom_5_cities["customer_count"], palette="Reds_r", ax=ax)
ax.set_xlabel("Jumlah Pelanggan")
ax.set_ylabel("Kota")
ax.set_title("Bottom 5 Kota dengan Pelanggan Paling Sedikit")
st.pyplot(fig)

# **Visualisasi Top 10 Provinsi dengan Pelanggan Terbanyak**
st.subheader("Top 10 Provinsi dengan Pelanggan Terbanyak")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(y=top_10_states["customer_state"], x=top_10_states["customer_count"], palette="Greens_r", ax=ax)
ax.set_xlabel("Jumlah Pelanggan")
ax.set_ylabel("Provinsi")
ax.set_title("Top 10 Provinsi dengan Pelanggan Terbanyak")
st.pyplot(fig)

# **Visualisasi Bottom 5 Provinsi dengan Pelanggan Paling Sedikit**
st.subheader("Bottom 5 Provinsi dengan Pelanggan Paling Sedikit")
fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(y=bottom_5_states["customer_state"], x=bottom_5_states["customer_count"], palette="Oranges_r", ax=ax)
ax.set_xlabel("Jumlah Pelanggan")
ax.set_ylabel("Provinsi")
ax.set_title("Bottom 5 Provinsi dengan Pelanggan Paling Sedikit")
st.pyplot(fig)

# Menampilkan data dalam tabel
st.subheader("Data Pelanggan per Kota dan Provinsi")
st.write("Top 10 Kota:")
st.dataframe(top_10_cities)

st.write("Bottom 5 Kota:")
st.dataframe(bottom_5_cities)

st.write("Top 10 Provinsi:")
st.dataframe(top_10_states)

st.write("Bottom 5 Provinsi:")
st.dataframe(bottom_5_states)

# **Visualisasi Top 10 Produk Terlaris**
st.subheader("Top 10 Produk Terlaris")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(y=top_10_products["product_category_name"], x=top_10_products["sales"], palette="Blues_r", ax=ax)
ax.set_xlabel("Jumlah Terjual")
ax.set_ylabel("Kategori Produk")
ax.set_title("Top 10 Produk Terlaris")
st.pyplot(fig)

# **Visualisasi Bottom 10 Produk Paling Sedikit Terjual**
st.subheader("Bottom 10 Produk Paling Sedikit Terjual")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(y=bottom_10_products["product_category_name"], x=bottom_10_products["sales"], palette="Reds_r", ax=ax)
ax.set_xlabel("Jumlah Terjual")
ax.set_ylabel("Kategori Produk")
ax.set_title("Bottom 10 Produk Paling Sedikit Terjual")
st.pyplot(fig)

# Menampilkan data dalam tabel
st.subheader("Data Penjualan Produk")
st.write("Top 10 Produk Terlaris:")
st.dataframe(top_10_products)

st.write("Bottom 10 Produk Paling Sedikit Terjual:")
st.dataframe(bottom_10_products)

st.caption('Copyright (c) 2025. Zidan Muhammad Ikvan')
