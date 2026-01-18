# 🚀 CARA CEPAT DEPLOY KE STREAMLIT CLOUD (GRATIS!)

## ⚡ 5 Langkah - 10 Menit Selesai!

### 📋 Yang Anda Butuhkan:
- ✅ Akun GitHub (gratis)
- ✅ Akun Streamlit Cloud (gratis)
- ✅ Koneksi internet

---

## 🎯 LANGKAH-LANGKAH:

### 1️⃣ Upload Project ke GitHub (5 menit)

**Opsi A: Via Website GitHub (Paling Mudah)**
1. Buka https://github.com/new
2. Isi:
   - Repository name: `shopee-retur-automation`
   - Description: `Aplikasi web untuk automation retur Shopee`
   - Pilih: **Public** (gratis) atau **Private** (perlu upgrade)
3. **JANGAN** centang "Add README"
4. Klik **"Create repository"**
5. Di halaman selanjutnya, klik **"uploading an existing file"**
6. **Drag & drop** semua file dan folder dari aplikasi ini
7. Klik **"Commit changes"**
8. ✅ Selesai! Project sudah di GitHub

**Opsi B: Via Git Command (Untuk yang familiar)**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/shopee-retur-automation.git
git push -u origin main
```

---

### 2️⃣ Buat Akun Streamlit Cloud (1 menit)

1. Buka https://share.streamlit.io/
2. Klik **"Sign up"** atau **"Continue with GitHub"**
3. Login dengan akun GitHub Anda
4. Klik **"Authorize streamlit"**
5. ✅ Akun siap!

---

### 3️⃣ Deploy Aplikasi (2 menit)

1. Di Streamlit Cloud, klik **"New app"** atau **"Create app"**
2. Isi form:
   - **Repository**: Pilih `shopee-retur-automation`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): Bisa custom nama, contoh: `shopee-retur-bagas`
3. Klik **"Deploy!"**
4. Tunggu 2-3 menit (build & deploy)
5. ✅ Aplikasi LIVE!

---

### 4️⃣ Dapatkan URL Aplikasi

Setelah deploy selesai, Anda akan dapat URL seperti:
```
https://USERNAME-shopee-retur-automation-app-xxxxx.streamlit.app
```

Atau jika custom:
```
https://shopee-retur-bagas.streamlit.app
```

---

### 5️⃣ Share ke Tim! 🎉

**Copy URL** dan share ke:
- ✅ Admin gudang
- ✅ Manager
- ✅ Tim logistics
- ✅ Siapa saja yang perlu akses

Mereka cukup buka URL di browser (laptop/HP) - **TIDAK perlu install apapun!**

---

## 🎯 Cara Menggunakan Setelah Deploy:

### Di Laptop/HP Manapun:
1. Buka browser (Chrome, Firefox, Edge, Safari)
2. Ketik URL: `https://shopee-retur-xxx.streamlit.app`
3. ✅ Langsung bisa pakai!

### Upload File:
- ✅ **CSV** (.csv) - Format standar dari Shopee
- ✅ **Excel** (.xlsx, .xls) - Bisa juga!

---

## 🔄 Update Aplikasi (Jika Ada Perubahan Code)

### Cara 1: Via GitHub Website
1. Buka repository di GitHub
2. Klik file yang mau diedit
3. Klik icon pensil (✏️) untuk edit
4. Save changes (Commit)
5. **Streamlit Cloud otomatis re-deploy!**

### Cara 2: Via Git
```bash
git add .
git commit -m "Update fitur xxx"
git push
```
Streamlit Cloud auto-deploy dalam 1-2 menit.

---

## 💰 BIAYA:

### Streamlit Community Cloud:
- ✅ **GRATIS selamanya**
- ✅ 1 GB RAM per app
- ✅ Unlimited apps (public)
- ✅ Unlimited users
- ✅ Custom domain (bisa)

### Batasan Free Plan:
- ⚠️ App harus **public** (siapa saja bisa akses URL)
- ⚠️ Max 1 GB RAM (cukup untuk 500+ retur)
- ⚠️ Resource shared (bisa lambat saat traffic tinggi)

### Upgrade ke Teams (Opsional):
- 💰 $20/user/month
- ✅ Private apps (hanya tim yang bisa akses)
- ✅ SSO & authentication
- ✅ Lebih cepat & dedicated resources

**Rekomendasi:** Mulai dengan **FREE**, upgrade nanti kalau perlu.

---

## 🔐 KEAMANAN (Penting!)

### ⚠️ Aplikasi Public = Siapa Saja Bisa Akses

**Solusi:**

### 1️⃣ Tambah Password Protection (RECOMMENDED)

Edit file `app.py`, tambahkan di awal fungsi `main()`:

```python
def check_password():
    """Returns True if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == "shopee2026":  # GANTI PASSWORD INI!
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("🔐 Password", type="password", 
                      on_change=password_entered, key="password")
        st.info("Masukkan password untuk akses aplikasi")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("🔐 Password", type="password", 
                      on_change=password_entered, key="password")
        st.error("❌ Password salah!")
        return False
    else:
        return True

def main():
    # Tambahkan ini di awal
    if not check_password():
        st.stop()
    
    # ... sisa code
```

### 2️⃣ Jangan Upload Data Sensitif ke GitHub

File `.gitignore` sudah di-set untuk **TIDAK** upload:
- ❌ File CSV data asli
- ❌ File Excel hasil export
- ✅ Hanya code yang di-upload

### 3️⃣ Data yang Di-Upload User Tidak Disimpan

- File CSV/Excel yang di-upload hanya ada di **memory**
- Begitu refresh/tutup browser = **data hilang**
- Aman untuk data retur

---

## ❓ FAQ

**Q: Berapa lama deploy pertama kali?**
A: 2-3 menit setelah klik "Deploy"

**Q: Bisa akses dari HP?**
A: Bisa! Buka URL di browser HP (Chrome, Safari)

**Q: Berapa banyak user yang bisa akses bersamaan?**
A: Unlimited! Tapi kalau traffic sangat tinggi bisa lambat (free plan)

**Q: Data aman?**
A: Ya. File upload hanya di memory, tidak disimpan permanent.

**Q: Bisa offline?**
A: Tidak. Harus ada koneksi internet.

**Q: Aplikasi bisa down?**
A: Jarang. Tapi bisa maintenance sesekali (beberapa menit).

**Q: Bisa custom domain?**
A: Bisa! Setting di Streamlit Cloud dashboard.

**Q: Perlu kartu kredit?**
A: Tidak! 100% gratis tanpa kartu kredit.

---

## 🆚 Alternatif Jika Streamlit Cloud Bermasalah:

### Railway.app
- ✅ Gratis 500 jam/bulan
- URL: https://railway.app/
- Butuh setup lebih (lihat DEPLOY_CLOUD.md)

### Render.com
- ✅ Gratis unlimited
- ⚠️ Sleep setelah 15 menit idle
- URL: https://render.com/

**Tapi Streamlit Cloud tetap yang terbaik untuk Streamlit apps!**

---

## 🎉 SELESAI!

URL Anda sekarang: `https://shopee-retur-xxx.streamlit.app`

Share ke tim dan mulai pakai! 🚀

**Ada masalah?** Cek DEPLOY_CLOUD.md untuk troubleshooting detail.
