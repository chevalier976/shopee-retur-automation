# 📦 Shopee Retur Automation

Aplikasi web berbasis Streamlit untuk mengotomasi proses data retur dari marketplace Shopee. Aplikasi ini dirancang khusus untuk membantu admin gudang mengelola 300-500 retur per bulan dengan lebih efisien.

## 🎯 Fitur Utama

### 1. Upload & Parse Data Shopee
- ✅ Support upload file **CSV** dan **Excel (.xlsx)** dari Shopee
- ✅ Parse otomatis semua kolom penting (No. Pesanan, Status, SKU, dll)
- ✅ Validasi format dan handling error

### 2. Dashboard Overview
- 📊 Statistik lengkap: Total retur, Partial returns, No resi kosong
- 📈 Grafik breakdown status pembatalan/pengembalian
- 📊 Top 5 alasan pembatalan
- ⚠️ Alert otomatis untuk partial returns dan no resi kosong

### 3. Multi-Search Feature (FITUR UTAMA)
- 🔍 Search by No. Pesanan atau No. Resi
- ⚡ **SUPER CEPAT** - Pencarian <50ms (instant!)
- 🔍 Support multiple search sekaligus (paste banyak ID)
- 📷 **BARU: Scanner Barcode Mode** - Scan barcode dengan USB scanner atau HP!
- 🔧 **BARU: Mismatch Handler** - Otomatis handle barcode yang berbeda!
- 🎯 Hasil instant dengan highlight alert
- 📦 Tampilan gabungan Produk + Variasi
- 📜 History scan untuk tracking

### 4. Form Input Data Unboxing
- 📅 **Tanggal**: Auto-fill dengan hari ini, bisa diedit
- 🏷️ **Batch**: Input nomor batch
- 📷 **Barcode di Paket**: Auto-capture barcode yang di-scan
- ⚠️ **Mismatch Detection**: Warning otomatis jika barcode tidak match
- ✅ **Ket Product**: 9 opsi status produk (OK, Defect, dll)
- 📍 **Stock In**: 3 lokasi tujuan (Retur Central, WH Online, Prodev)
- 📝 **Catatan Mismatch**: Dokumentasi jika ada perbedaan barcode

### 5. Export to Excel
- 📥 Download hasil ke Excel dengan 1 klik
- 🎨 Format rapi dengan header berwarna
- 📊 Include semua kolom Shopee + data tambahan
- 🕐 Filename otomatis dengan timestamp

---

## 🚀 3 CARA Menjalankan Aplikasi

### ⚡ OPSI 1: Executable (.exe) - TANPA INSTALL PYTHON! 
**✅ Paling mudah untuk laptop lain - cukup copy paste file!**

1. Di laptop ini: Double-click **`build_executable.bat`**
2. Tunggu 3-5 menit (build file .exe)
3. Copy folder **`dist/`** ke USB/drive
4. Paste di laptop lain
5. Double-click **`run_ShopeeReturAutomation.bat`**
6. ✅ Aplikasi jalan tanpa Python!

📖 **Detail:** Lihat [CARA_TANPA_PYTHON.md](CARA_TANPA_PYTHON.md)

---

### 🌐 OPSI 2: Deploy ke Cloud - AKSES VIA URL!
**✅ Akses dari laptop/HP manapun via browser!**

1. Upload ke GitHub
2. Deploy ke Streamlit Cloud (gratis)
3. Dapat URL: `https://shopee-retur.streamlit.app`
4. Share URL ke semua orang
5. ✅ Akses dari mana saja!

📖 **Detail:** Lihat [DEPLOY_CLOUD.md](DEPLOY_CLOUD.md)

---

### 🐍 OPSI 3: Install Python (Cara Tradisional)

**Langkah 1: Install Python**
1. Download Python dari https://www.python.org/downloads/
2. **PENTING**: Saat install, centang "Add Python to PATH"
3. Install seperti biasa

**Langkah 2: Install Dependencies**
1. Buka folder aplikasi
2. **Double-click file `install.bat`**
3. Tunggu proses instalasi selesai
4. ✅ Instalasi selesai!

**Langkah 3: Jalankan Aplikasi**
1. **Double-click file `run_app.bat`**
2. Browser akan terbuka otomatis di http://localhost:8501
3. ✅ Aplikasi siap digunakan!

**Cara Menghentikan Aplikasi:**
- Tekan `Ctrl + C` di window command prompt yang terbuka
- Atau tutup window command prompt

📖 **Detail:** Lihat [PANDUAN_LENGKAP.md](PANDUAN_LENGKAP.md)

---

## 📊 Perbandingan 3 Cara

| Aspek | Executable | Cloud | Install Python |
|-------|------------|-------|----------------|
| **Perlu Python?** | ❌ Tidak | ❌ Tidak | ✅ Ya |
| **Perlu Internet?** | ❌ Tidak | ✅ Ya | Saat install |
| **Setup Laptop Lain** | ⚡⚡⚡ Copy paste | ⚡⚡⚡ Buka URL | ⚡⚡ Install |
| **Akses dari HP** | ❌ | ✅ | ❌ |
| **Multi-User** | ❌ | ✅ | ❌ |

💡 **Rekomendasi:**
- **1-2 laptop:** Gunakan Executable (.exe)
- **Banyak user/device:** Gunakan Cloud Deploy
- **Developer:** Install Python

---

## 📂 Struktur Folder

```
│
├── app.py                         # File utama aplikasi
├── requirements.txt               # Dependencies Python
│
├── install.bat                    # ⚡ Script instalasi (Windows)
├── run_app.bat                    # ⚡ Script jalankan aplikasi (Windows)
├── build_executable.bat           # ⚡ Build file .exe tanpa Python
│
├── README.md                      # Dokumentasi utama
├── PANDUAN_LENGKAP.md            # Panduan lengkap penggunaan
├── PANDUAN_SCANNER.md            # ⭐ Panduan scanner barcode
├── PANDUAN_MISMATCH.md           # ⭐ Handle barcode berbeda
├── OPTIMASI_KECEPATAN.md         # Info optimasi performa
├── CARA_TANPA_PYTHON.md          # 3 cara tanpa install Python
├── DEPLOY_CLOUD.md               # Panduan deploy ke cloud
├── QUICK_DEPLOY.md               # Quick start deploy
│
├── config/                        # Konfigurasi aplikasi
│   ├── __init__.py
│   └── settings.py               # Settings (kolom CSV, opsi dropdown)
│
├── utils/                         # Utility modules
│   ├── __init__.py
│   ├── parser.py                 # Parse CSV Shopee
│   ├── search.py                 # Search & filter data
│   └── export.py                 # Export ke Excel
│
├── data/                          # Sample data
│   └── sample_shopee_retur.csv
│
├── output/                        # Folder hasil export Excel
│
└── .streamlit/                    # Konfigurasi Streamlit
    └── config.toml               # Config server & theme
```

---

## 📖 Panduan Penggunaan

### Step 1: Upload File CSV
1. Klik tombol **"Browse files"** di sidebar kiri
2. Pilih file CSV dari Shopee
3. ✅ Tunggu hingga muncul notifikasi "File berhasil diupload!"

**Format CSV yang didukung:**
- File harus berisi 10 kolom wajib dari Shopee
- Encoding: UTF-8 atau UTF-8-BOM
- Lihat `data/sample_shopee_retur.csv` untuk contoh

### Step 2: Lihat Dashboard
1. Klik tab **"📊 Dashboard"**
2. Lihat statistik overview:
   - Total retur
   - Partial returns (jika ada)
   - No resi kosong (jika ada)
   - Unique orders
3. Analisa grafik:
   - Pie chart: Status pembatalan/pengembalian
   - Bar chart: Top 5 alasan pembatalan
4. Gunakan filter untuk melihat data detail

### Step 3: Search Data Retur
1. Klik tab **"🔍 Search & Input"**
2. Paste No. Pesanan atau No. Resi di textarea (satu per baris)
   
   **Contoh:**
   ```
   260101U95E5RBQ
   SPXID067190313141
   260109JVE371VN
   ```

3. Klik tombol **"🔍 Cari"**
4. ✅ Lihat hasil pencarian dengan alert jika ada partial return atau no resi kosong

### Step 4: Input Data Tambahan
1. Setelah search, scroll ke bawah ke section **"📝 Input Data Tambahan"**
2. Klik expander untuk setiap item yang ingin diinput
3. Isi form:
   - **Tanggal**: Otomatis hari ini, bisa diganti
   - **Batch**: Input nomor batch manual
   - **Ket Product**: Pilih kondisi produk
     - OK
     - Defect
     - Kemasan Sudah Dibuka
     - Sudah dibuka sealnya
     - Packaging terbuka
     - IB Rusak
     - Produk Kosong
     - Produk Sudah dicoba
     - Bukan Produk BLP
   - **Stock In**: Pilih lokasi
     - Retur Central
     - WH Online
     - Prodev

### Step 5: Export ke Excel
1. Klik tab **"📥 Export"**
2. Preview data yang akan diexport
3. Klik tombol **"📥 Download Excel"**
4. ✅ File akan terdownload dengan nama: `Retur_Shopee_YYYYMMDD_HHMMSS.xlsx`

## 💡 Tips & Tricks

### 🚀 Workflow Efisien untuk Admin
1. **Di awal hari/minggu**: Upload file CSV terbaru dari Shopee
2. **Saat terima paket retur**:
   - Lihat nomor pesanan di paket
   - Paste ke aplikasi (bisa sekaligus beberapa paket)
   - Unboxing sambil lihat info di layar
   - Input data tambahan langsung
3. **Sebelum pulang**: Download Excel untuk laporan

### 🎯 Multi-Search
- Bisa paste 10-20 nomor pesanan sekaligus
- Bisa mix No. Pesanan dan No. Resi
- Case-insensitive (HURUF BESAR/kecil sama aja)

### ⚠️ Perhatikan Alert
- **⚠️ Partial Return**: Qty retur < qty order → cek fisik barang
- **⚠️ No Resi Kosong**: Pesanan dibatalkan sebelum dikirim

## 🔧 Troubleshooting

### ❌ Error: "Kolom yang hilang: ..."
**Penyebab**: Format CSV tidak sesuai

**Solusi**:
- Pastikan file CSV dari Shopee memiliki 10 kolom wajib
- Cek nama kolom tidak berubah
- Download ulang dari Shopee

### ❌ Error: "Error parsing CSV: ..."
**Penyebab**: File corrupt atau encoding salah

**Solusi**:
- Buka file di Excel/Google Sheets
- Save as → pilih "CSV UTF-8"
- Upload ulang

### 🐌 Aplikasi Lambat
**Penyebab**: File terlalu besar atau banyak data

**Solusi**:
- Split file CSV jika > 5000 baris
- Restart aplikasi
- Close tab browser yang tidak dipakai

### 📱 Tidak Bisa Dibuka di Handphone/Tablet
**Penyebab**: Streamlit lebih optimal di desktop/laptop

**Solusi**:
- Gunakan tablet dalam mode landscape
- Zoom out browser untuk lihat penuh
- Atau pakai laptop/PC

## 📊 Format Data

### Kolom yang Diperlukan dari CSV Shopee
1. No. Pesanan
2. Status Pesanan
3. Alasan Pembatalan
4. Status Pembatalan/ Pengembalian
5. No. Resi
6. Nomor Referensi SKU
7. Nama Produk
8. Nama Variasi
9. Jumlah
10. Returned quantity

### Kolom Tambahan dari Input User
1. Tanggal (format: YYYY-MM-DD)
2. Batch
3. Ket Product
4. Stock In

### Output Excel
Semua kolom Shopee + Kolom tambahan + Produk + Variasi (gabungan)

## 🏗️ Struktur Project

```
shopee-retur-automation/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Dokumentasi (file ini)
├── .gitignore                      # Git ignore rules
├── utils/
│   ├── __init__.py
│   ├── parser.py                   # Parse CSV Shopee
│   ├── search.py                   # Search logic
│   └── export.py                   # Export to Excel
├── config/
│   ├── __init__.py
│   └── settings.py                 # Configuration
└── data/
    └── sample_shopee_retur.csv     # Sample data
```

## ❓ FAQ (Frequently Asked Questions)

### Q: Apakah bisa dipakai oleh 2 admin bersamaan?
A: Ya! Setiap admin buka di browser masing-masing. Data tidak saling mempengaruhi.

### Q: Apakah data disimpan di aplikasi?
A: Tidak. Data hanya ada selama session browser aktif. Setelah close tab, data hilang. Ini untuk keamanan data.

### Q: Bisa import dari marketplace lain (TokPed, TikTok)?
A: Saat ini hanya support Shopee. Tapi bisa dikembangkan untuk marketplace lain.

### Q: Berapa lama waktu yang dihemat?
A: **Target: 80-90% lebih cepat!**
- Manual: 5-10 menit per paket
- Pakai app: ~1 menit per paket

### Q: Apakah perlu koneksi internet?
A: Tidak setelah install. Aplikasi jalan di local (localhost).

### Q: File Excel hasilnya bisa dibuka di Google Sheets?
A: Ya, bisa! Upload file .xlsx ke Google Drive dan buka dengan Google Sheets.

## 🎯 Target Pengguna

- **Target Users**: 2 admin gudang
- **Expected Volume**: 300-500 retur/bulan
- **Skill Level**: Non-teknis (user-friendly)
- **Device**: Laptop/PC (atau tablet dalam landscape mode)

## 🔮 Future Enhancement

Fitur yang mungkin ditambahkan di masa depan:
- ☁️ Deploy ke cloud (Streamlit Cloud)
- 📊 Export langsung ke Google Sheets
- 🗄️ Database untuk history data
- 👤 User authentication
- 🛒 Support format TikTok & Tokopedia
- 📱 Mobile responsive optimization

## 📞 Support & Kontak

Jika ada pertanyaan atau menemukan bug:
1. Buat issue di GitHub repository
2. Atau hubungi developer

## 📜 License

MIT License - bebas digunakan dan dimodifikasi

---

**Dibuat dengan ❤️ untuk memudahkan kerja admin gudang**

**Tech Stack**: Python 3.9+, Streamlit, Pandas, openpyxl
#   L a s t   u p d a t e :   0 1 / 1 8 / 2 0 2 6   2 0 : 1 5 : 5 2  
 