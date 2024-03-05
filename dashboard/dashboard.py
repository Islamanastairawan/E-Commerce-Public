import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

sns.set_theme(style='dark')

st.sidebar.title('Proyek Analisis Data: E-Commerce Public')

# Mengimpor data
path = os.getcwd()
all_df = pd.read_csv(path+"\data_all.csv")

# Mengurutkan kategori produk berdasarkan total pendapatan
top_categories = all_df.groupby('product_category_name').sum(numeric_only=True)['price'].nlargest(5).index

# Memfilter data hanya untuk kategori produk teratas    
revenue_top_categories = all_df[all_df['product_category_name'].isin(top_categories)]

# Visualisasi untuk pertanyaan 1
st.title('Hubungan antara Jumlah Pembayaran dan Skor Ulasan Produk')
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='payment_value', y='review_score', data=all_df, ax=ax)
ax.set_title('Hubungan antara Jumlah Pembayaran dan Skor Ulasan')
ax.set_xlabel('Jumlah Pembayaran')
ax.set_ylabel('Skor Ulasan')
st.pyplot(fig)

# Visualisasi untuk pertanyaan 2
st.title('Pengaruh Berat Produk terhadap Biaya Pengiriman')
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='product_weight_g', y='freight_value', data=all_df, ax=ax)
ax.set_title('Hubungan antara Berat Produk dan Biaya Pengiriman')
ax.set_xlabel('Berat Produk (g)')
ax.set_ylabel('Biaya Pengiriman')
st.pyplot(fig)

# Visualisasi untuk pertanyaan 3
st.title('Kontribusi Kategori Produk terhadap Total Pendapatan Penjualan per Penjual')
fig, ax = plt.subplots(figsize=(10, 6))
revenue_top_categories.pivot_table(index='seller_id', columns='product_category_name', values='price').iloc[:10].plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Total Pendapatan Penjualan per Penjual untuk Kategori Produk Teratas')
ax.set_xlabel('Penjual')
ax.set_ylabel('Total Pendapatan')
ax.legend(title='Kategori Produk')
ax.set_xticklabels([])
st.pyplot(fig)
