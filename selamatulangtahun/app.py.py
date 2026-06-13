import streamlit as st
import time

# 1. Konfigurasi Dasar Halaman Website
st.set_page_config(page_title="Happy Birthday! 🎈", page_icon="🎂", layout="centered")

# 2. Custom CSS untuk mempercantik tampilan awal & animasi
st.markdown("""
<style>
    /* Mengubah background web menjadi warna light steel blue */
    .stApp {
        background-color: #B0C4DE;
    }
    /* Animasi bergoyang (floating) untuk karakter utama */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    /* Kontainer karakter di halaman awal */
    .char-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
        font-size: 80px; /* Ukuran besar untuk karakter emoji */
        padding: 40px 0;
        animation: float 3s ease-in-out infinite;
    }
    /* Teks judul Happy Birthday! */
    .title-text {
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #FF4B4B;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    /* Styling untuk Surat Ucapan */
    .birthday-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        border: 2px dashed #FF8C00;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. TAMPILAN AWAL: Rubah, Bebek, dan Kue Ulang Tahun
st.markdown("<div class='title-text'>happy sweet seventeen</div>", unsafe_allow_html=True)

# Memunculkan emoji Rubah (🦊), Kue (🎂), dan Bebek (🦆) berjejer secara aesthetic
st.markdown("<div class='char-container'>🦊 🎂 🦆</div>", unsafe_allow_html=True)

st.write("")

# Menggunakan mekanisme session state agar layout tetap rapi saat diklik
if 'surat_terbuka' not in st.session_state:
    st.session_state.surat_terbuka = False

# 4. TOMBOL UTAMA (PENCET UNTUK MUNCULKAN TEXT)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Click here!", use_container_width=True):
        st.session_state.surat_terbuka = True

# 5. AKSI SETELAH TOMBOL DIPENCET (MEMUNCULKAN TEKS & ANIMASI BALON)
if st.session_state.surat_terbuka:
    # Memunculkan efek balon terbang bawaan Streamlit
    st.balloons()
    
    # Menampilkan teks surat ucapan spesial
    st.markdown("""
    <div class='birthday-card'>
        <h2 style='text-align: center; color: #FF8C00;'>🎉 Happy Birthday! 🎉</h2>
        <p style='font-size: 16px; line-height: 1.6; color: #333333;'>
          Happy sweet seventeen!
           alo, uwaw pertama kali nih gue ngasih ginian buat orang, bangga dong jadi orang pertama uyey,
           I won't say much here, but i just wanted you to have the happiest birthday todaayyy okayy, please be happy, show the world your sweet smile, your pure soul, and all the good things you have, show to the world todayy woii!
           maaf ya, belum bisa ngasih kado lu di hari ini, i had the plan but the fate didn't allign with all of it, tapi semoga, letter ini bisa tetep ngebuat lu senyum ya, meskipun bukan si irpan-irpan itu yg ngasih, semoga lu tetep seneng dapat ini dari gue uyey
           jangan pernah nyerah ya put, di hidup yang cuma satu kali ini, masih banyak hal yang akan dan pasti lu capai ke depannya, tujuh belas tahun angka yang bagus untuk sekarang, gua harap gua bisa nemenin lu, dan ngucapin lu di umur belasan atau puluhan yang akan datang lagi nantinya.
           inget ya gue selalu di sini, if the world seems very mean to you, remember that i'm here for some reason that God want to tell you something, everything came for many reasons, jadi menurut gue, pertemanan kita pun ada karna hal yang masih diinginkan Tuhan untuk terjadi, jangan sungkan-sungkan ke gue ya.
           gue mungkin bukan yang terbaik sebagai teman, tapi gue berusaha jadi orang yang bisa ngebantu lu di saat lu butuh, gue harap itu bermakna buat lu. itu aja dehh, intinya, selamat ulang tahun yaa, segala doa terbaik dan baik sudah gue kirimkan ke yang di atas, tinggal lu aamiinin aja bilang aja gini, Tuhan aamiinin doa aqil ya. pasti nyampe tuh.
                  </p>
        <p style='font-size: 16px; line-height: 1.6; color: #333333;'>
            I'll always root for you from here or whenever I am
        </p>
        <hr style='border-top: 1px solid #ddd;'>
        <p style='text-align: right; font-weight: bold; color: #FF4B4B; font-style: italic;'>
            — aqil 🦊
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Efek tambahan salju/bintang jatuh setelah teks terbuka
    st.snow()

# Beri ruang jarak ke bawah agar pemutar lagu berada di posisi paling bawah
st.write("<br><br><br>", unsafe_allow_html=True)
st.write("---")

# 6. PALING BAWAH: PEMUTAR LAGU (MUSIC PLAYER)
st.markdown("<p style='text-align: center; color: #666; font-size: 14px;'>here a song</p>", unsafe_allow_html=True)

# URL Lagu Selamat Ulang Tahun (Anda bisa menggantinya dengan link .mp3 lainnya)
audio_url = st.audio("https://soundhelix.com", format="audio/mp3")
st.audio("notalot.mp3", format="audio/mp3")
