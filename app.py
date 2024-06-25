import streamlit as st
from PIL import Image
import pandas as pd
import plost
import numpy as np
import matplotlib.pyplot as plot

# Page Configuration
st.set_page_config(page_title="HRV Analysis & RR Tachogram Detection", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .cta-button {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
    }
    .background {
        background-image: url('Bedah Jantung.jpg');
        background-size: cover;
        padding: 50px 0;
        text-align: center;
        color: white;
    }
    .background h1 {
        margin: 0;
        font-size: 2.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation Function
def switch_page(page):
    if page == "Dashboard":
        st.session_state.page = "Dashboard"
    else:
        st.session_state.page = "Landing"

# Landing Page Sections
def header_section():
    st.markdown("<h1 style='text-align: center;color: #F7F8F7;'>Your heart's rhythm reveals more than just beats</h1> <h4 style='text-align: center;color: #555;'>Unlock the SECRETS of your heart's rhythm </h4>", unsafe_allow_html=True)

def user_concerns_section():
    st.markdown("<h2 style='text-align: center; color: #F7F8F7;'>Unseen Dangers Awaiting You</h2>", unsafe_allow_html=True)
    st.image('Orang Sakit.png', use_column_width=True) 
    st.markdown("<h4 style='text-align: center; color: #EB455F;'>Faktanya: lebih dari 17.9 juta orang meninggal tiap tahunnya akibat penyakit jantung.</h4>", unsafe_allow_html=True)
    st.write("""
        Kita terlalu sibuk, sampai kita lupa dan abai terhadap kesehatan jantung kita. Tanpa kita sadari ada banyak ancaman yang mendekat:
         - Peningkatan risiko penyakit kardiovaskular.
         - Tingkat stres tanpa disadari yang memengaruhi kesejahteraan secara keseluruhan.
         - Hilangnya peringatan dini mengenai potensi kondisi jantung.
    """)

def causes_section():
    st.markdown("<h2 class='header'>Recognize it early</h2>", unsafe_allow_html=True)
    st.write("""
        Sadar akan pentingnya deteksi HRV akan membantu kamu terhindar dari masalah yang lebih besar, seperti:
          1. **Stres Kronis**: Stres yang berkepanjangan dapat mengganggu ritme jantung, sehingga menyebabkan masalah kesehatan jangka panjang.
          2. **Pilihan Gaya Hidup yang Buruk**: Kebiasaan makan yang tidak sehat, kurang olahraga, dan kurang tidur berkontribusi signifikan terhadap masalah jantung.
          3. **Kurangnya Kesadaran**: Banyak orang tidak menyadari pentingnya memantau kesehatan jantung mereka secara teratur.
    """)

def testimonials_section():
    st.markdown("<h2 class='header'>Hear from Our Community</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image('Ardi.png', width=150)  # Replace with your actual image file
        st.markdown("<h4 class='testimonial'>Rahardian Asyam Zuhdi</h4>", unsafe_allow_html=True)
        st.write("""
            Setelah mempelajari analisis HRV,  stress saya menjadi berkurang. Saya bisa berolahraga dengan teratur dan berkeliling dunia kapanpun saya mau.
        """)
        
    with col2:
        st.image('Bahari.png', width=150)  # Replace with your actual image file
        st.markdown("<h4 class='testimonial'>Bahari Noor Hidayat</h4>", unsafe_allow_html=True)
        st.write("""
            Deteksi RR Tachogram membantu saya mengetahui kondisi kesehatan saya sejak dini, saya tidak lagi merasa khawatir menentukan penanganan yang tepat untuk rasa sakit yang saya alami.
        """)
        
    with col3:
        st.image('Qusay.png', width=150)  # Replace with your actual image file
        st.markdown("<h4 class='testimonial'>Muhammad Qusay Yubasyrendra Akib</h4>", unsafe_allow_html=True)
        st.write("""
            Memahami HRV berarti mulai memahami diri sendiri. Saya menjadi lebih mampu untuk mengelola mengelola kecemasan saya, akhirnya kualitas tidur saya menjadi lebih baik.
        """)

def cta_section():
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>It's Never Too Late</h2>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center;color: #F7F8F7;'>Kami percaya setiap orang ingin memberikan yang terbaik untuk dirinya dan orang di sekitranya</h2>", unsafe_allow_html=True)
    st.markdown("<div class='cta-button'><a href='#' onclick='window.location.reload()' style='background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;'>I'm ready to be more healthy</a></div>", unsafe_allow_html=True)
    if st.button("I'm Aware"):
        switch_page("Dashboard")

def landing_page():
    header_section()
    st.markdown("---")
    user_concerns_section()
    st.markdown("---")
    causes_section()
    st.markdown("---")
    testimonials_section()
    st.markdown("---")
    cta_section()

# Dashboard Page
def dashboard_page():
    st.header('ASN Group 2')

    st.subheader("Dataset")
    data_file = st.file_uploader("Upload Dataset", type=["txt"])
    if data_file is not None:
        try:
            column_names=["ECG"]
            data = pd.read_csv(data_file, delimiter="\t",names=column_names)  # Pastikan delimiter sesuai dengan file txt
            data["sample interval"] = np.arange(len(data))
            data["elapsed time"] = (data["sample interval"]) * (1/200)
            x = data["elapsed time"]
            y = data["ECG"] - (sum(data["ECG"] / len(data["ECG"])))
            st.dataframe(data)
            st.write("Grafik dari dataset")
            fig, ax = plot.subplots(figsize=(35, 15))
            ax.plot(x[0:2000], y[0:2000], color='b')
            ax.set_xlabel("Elapsed time")
            ax.set_ylabel("Amplitude (mv)")

            # Display the plot in Streamlit
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error reading file: {e}")
    jumlahdata = int(np.size(x))
    st.write("Jumlah data:\n ",jumlahdata)
    
# Main App
def main():
    if "page" not in st.session_state:
        st.session_state.page = "Landing"
    
    if st.session_state.page == "Dashboard":
        dashboard_page()
    else:
        landing_page()

if __name__ == "__main__":
    main()
