import streamlit as st
import pandas as pd
from PIL import Image

# Data sample untuk menu makanan
food_items = [
    {"name": "Nasi Goreng", "price": 15000, "producer": "Warung Bu Tini", "image": "https://via.placeholder.com/150"},
    {"name": "Ayam Geprek", "price": 12000, "producer": "Kantin Mas Bro", "image": "https://via.placeholder.com/150"},
    {"name": "Sate Ayam", "price": 20000, "producer": "Warung Sate Pak Kumis", "image": "https://via.placeholder.com/150"},
    {"name": "Mie Ayam", "price": 10000, "producer": "Kantin Mbak Sri", "image": "https://via.placeholder.com/150"}
]

# Data sample untuk produsen
producers = [
    {"name": "Warung Bu Tini", "address": "Kantin Teknik Mesin", "rating": 4.5},
    {"name": "Kantin Mas Bro", "address": "Kantin Teknik Elektro", "rating": 4.0},
    {"name": "Warung Sate Pak Kumis", "address": "Kantin Teknik Sipil", "rating": 4.8},
    {"name": "Kantin Mbak Sri", "address": "Kantin Teknik Industri", "rating": 4.2}
]

# Data sample untuk akun pengguna
user_account = {
    "username": "Fulan",
    "balance": 50000,
    "order_history": [
        {"food": "Nasi Goreng", "quantity": 2, "total_price": 30000},
        {"food": "Ayam Geprek", "quantity": 1, "total_price": 12000}
    ],
    "profile_image": "https://id.pinterest.com/pin/650699846174439397/"
}

# Fungsi untuk menampilkan rekomendasi kuliner
def show_recommendations():
    st.header("Rekomendasi Kuliner")
    for item in food_items:
        st.subheader(item['name'])
        st.image(item['image'], width=150)
        st.write(f"Harga: Rp {item['price']}")
        st.write(f"Produsen: {item['producer']}")

# Fungsi untuk menampilkan daftar produsen
def show_producers():
    st.header("Daftar Produsen")
    for producer in producers:
        st.subheader(producer['name'])
        st.write(f"Alamat: {producer['address']}")
        st.write(f"Rating: {producer['rating']}")

# Fungsi untuk tracking kurir (dummy data)
def track_courier():
    st.header("Tracking Kurir")
    st.write("Kurir saat ini berada di gerbang utama ITS.")
    st.map()

# Fungsi untuk fitur pemesanan makanan
def food_delivery():
    st.header("Pesan Makanan")
    selected_food = st.selectbox("Pilih makanan yang ingin dipesan", [item['name'] for item in food_items])
    quantity = st.number_input("Jumlah porsi", min_value=1, max_value=10, value=1)
    selected_producer = next(item for item in food_items if item["name"] == selected_food)["producer"]
    price = next(item for item in food_items if item["name"] == selected_food)["price"]
    total_price = quantity * price
    
    st.write(f"Harga total: Rp {total_price}")
    if st.button("Pesan Sekarang"):
        st.success(f"Pesanan {selected_food} sebanyak {quantity} porsi dari {selected_producer} berhasil dipesan!")

# Fungsi untuk menampilkan halaman akun pengguna
def show_account():
    st.header("Akun Pengguna")
    st.image(user_account['profile_image'], width=150)
    st.subheader(user_account['username'])
    
    st.write("**Saldo:** Rp", user_account['balance'])
    
    st.subheader("Riwayat Pemesanan")
    for order in user_account['order_history']:
        st.write(f"Makanan: {order['food']}, Jumlah: {order['quantity']}, Total Harga: Rp {order['total_price']}")

    st.subheader("Pengaturan")
    st.write("Pengaturan akun dapat disesuaikan di sini.")

# Main function
def main():
    st.title("Aplikasi Pemesanan Makanan ITS")
    menu = ["Food Delivery", "Rekomendasi Kuliner", "Tracking Kurir", "Daftar Produsen", "Akun"]
    choice = st.sidebar.selectbox("Pilih Fitur", menu)

    if choice == "Food Delivery":
        food_delivery()
    elif choice == "Rekomendasi Kuliner":
        show_recommendations()
    elif choice == "Tracking Kurir":
        track_courier()
    elif choice == "Daftar Produsen":
        show_producers()
    elif choice == "Akun":
        show_account()

if __name__ == '__main__':
    main()
