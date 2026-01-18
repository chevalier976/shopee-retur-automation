# 🌐 Deploy Shopee Retur Automation ke Cloud

Panduan deploy aplikasi ke cloud sehingga bisa diakses dari laptop/HP manapun via URL tanpa perlu install Python.

---

## 🚀 Metode 1: Streamlit Community Cloud (GRATIS & TERCEPAT)

### Keuntungan:
- ✅ **100% GRATIS**
- ✅ Tidak perlu install apapun di laptop lain
- ✅ Akses dari mana saja via URL (contoh: `https://shopee-retur.streamlit.app`)
- ✅ Bisa akses dari HP juga
- ✅ Update otomatis saat code berubah
- ✅ Paling mudah untuk Streamlit apps

### Langkah Deploy:

#### 1️⃣ Persiapan (Sekali Saja)

**A. Buat Akun GitHub**
1. Buka https://github.com/signup
2. Daftar dengan email
3. Verifikasi email

**B. Upload Project ke GitHub**
1. Buka https://github.com/new
2. Repository name: `shopee-retur-automation`
3. Pilih "Public"
4. Klik "Create repository"
5. Upload semua file aplikasi:
   - Drag & drop folder ke GitHub
   - Atau gunakan GitHub Desktop (https://desktop.github.com/)

#### 2️⃣ Deploy ke Streamlit Cloud

**A. Buat Akun Streamlit Cloud**
1. Buka https://share.streamlit.io/
2. Klik "Sign up" atau "Continue with GitHub"
3. Login dengan akun GitHub
4. Authorize Streamlit

**B. Deploy Aplikasi**
1. Klik "New app"
2. Pilih:
   - Repository: `shopee-retur-automation`
   - Branch: `main`
   - Main file path: `app.py`
3. Klik "Deploy!"
4. Tunggu 2-3 menit
5. ✅ Aplikasi live!

**C. Dapatkan URL**
- URL otomatis: `https://[username]-shopee-retur-automation-app-xxxxx.streamlit.app`
- Bisa custom domain jika mau

#### 3️⃣ Akses dari Laptop Lain

1. Buka browser (Chrome, Firefox, Edge, Safari)
2. Ketik URL aplikasi
3. ✅ Langsung bisa digunakan!
4. **Tidak perlu install Python atau apapun**

### Cara Update Aplikasi

Jika ada perubahan code:
1. Update file di GitHub
2. Streamlit Cloud otomatis re-deploy
3. Refresh browser untuk lihat perubahan

---

## 🔧 Metode 2: Railway (GRATIS dengan Batasan)

### Keuntungan:
- ✅ Gratis untuk penggunaan ringan
- ✅ Lebih fleksibel dari Streamlit Cloud
- ✅ Support database jika diperlukan nanti

### Langkah Deploy:

#### 1️⃣ Buat File Konfigurasi

**A. Buat `Procfile`** (tanpa ekstensi)
```
web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

**B. Buat `runtime.txt`**
```
python-3.11.7
```

#### 2️⃣ Deploy ke Railway

1. Buka https://railway.app/
2. Klik "Start a New Project"
3. Login dengan GitHub
4. Pilih "Deploy from GitHub repo"
5. Pilih repository `shopee-retur-automation`
6. Railway otomatis detect Streamlit
7. Klik "Deploy"
8. Tunggu build selesai
9. Klik "Generate Domain"
10. ✅ Dapatkan URL: `https://shopee-retur-production.up.railway.app`

---

## ☁️ Metode 3: Render (GRATIS)

### Langkah Deploy:

#### 1️⃣ Buat File Konfigurasi

**A. Buat `start.sh`**
```bash
#!/bin/bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

#### 2️⃣ Deploy ke Render

1. Buka https://render.com/
2. Sign up dengan GitHub
3. Klik "New +" → "Web Service"
4. Connect repository `shopee-retur-automation`
5. Konfigurasi:
   - Name: `shopee-retur-automation`
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
6. Pilih "Free" plan
7. Klik "Create Web Service"
8. ✅ URL: `https://shopee-retur-automation.onrender.com`

**Catatan**: Free plan sleep setelah 15 menit tidak dipakai, butuh 30-60 detik untuk wake up.

---

## 📊 Perbandingan Metode Cloud

| Fitur | Streamlit Cloud | Railway | Render |
|-------|----------------|---------|--------|
| **Gratis** | ✅ Unlimited | ✅ 500 jam/bulan | ✅ Unlimited |
| **Kecepatan Deploy** | ⚡⚡⚡ Tercepat | ⚡⚡ Cepat | ⚡ Agak lambat |
| **Mudah Setup** | ⭐⭐⭐ Paling mudah | ⭐⭐ Mudah | ⭐ Perlu config |
| **Auto-deploy** | ✅ | ✅ | ✅ |
| **Custom Domain** | ✅ | ✅ | ✅ |
| **Sleep/Downtime** | ❌ Always on | ❌ Always on | ⚠️ Sleep setelah 15 min |
| **Cocok untuk** | Streamlit apps | Any Python app | Any web app |

### Rekomendasi:
- **Untuk aplikasi ini → STREAMLIT CLOUD** (paling mudah dan cocok)

---

## 🎯 Setelah Deploy

### Cara Menggunakan:

1. **Admin 1** (di kantor):
   - Buka `https://shopee-retur.streamlit.app`
   - Upload CSV, input data
   - Export Excel

2. **Admin 2** (di gudang, laptop berbeda):
   - Buka `https://shopee-retur.streamlit.app`
   - Lihat data yang sama
   - Input data juga

3. **Manager** (dari HP):
   - Buka `https://shopee-retur.streamlit.app` di browser HP
   - Lihat dashboard dan statistik

### Keuntungan Cloud Deployment:

✅ **Tidak perlu install apapun** di laptop/HP lain
✅ **Akses dari mana saja** (kantor, gudang, rumah)
✅ **Multi-device** (laptop, HP, tablet)
✅ **Selalu update** otomatis
✅ **Hemat storage** laptop (tidak perlu download aplikasi besar)
✅ **Akses bersama** (banyak user bisa akses bersamaan)

---

## ⚠️ Catatan Penting

### Keamanan Data:

**Untuk Streamlit Cloud:**
- Aplikasi public = siapa saja bisa akses URL
- **Solusi**: Tambahkan password/autentikasi
- Atau gunakan Streamlit Teams (berbayar) untuk private apps

**Untuk Data Sensitif:**
- Jangan upload file CSV yang sudah ada data ke GitHub (public)
- Gunakan `.gitignore` untuk exclude file data
- Atau buat repository private (gratis di GitHub)

### File `.gitignore` (wajib!):

```
# Data files
data/*.csv
output/*.xlsx
!data/sample_shopee_retur.csv

# Python
__pycache__/
*.pyc
venv/

# Build
build/
dist/
*.spec
```

---

## 🔐 Tambah Password (Opsional)

Untuk proteksi aplikasi, tambahkan code ini di `app.py`:

```python
import streamlit as st

# Password protection
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == "shopee2026":  # Ganti password
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password salah")
        return False
    else:
        # Password correct.
        return True

# Tambahkan di awal main()
if not check_password():
    st.stop()
```

---

**Pilih metode yang paling cocok untuk kebutuhan Anda!** 🚀
