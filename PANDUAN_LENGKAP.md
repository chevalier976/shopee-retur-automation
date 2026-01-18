# Panduan Lengkap Shopee Retur Automation

## 📖 Cara Install dan Jalankan (Untuk Pengguna Baru)

### Untuk Windows (Paling Mudah)

#### 1️⃣ Install Python (Hanya Sekali)

1. Buka browser, kunjungi: https://www.python.org/downloads/
2. Download Python versi terbaru (3.9 atau lebih baru)
3. **PENTING**: Saat install, centang ✅ **"Add Python to PATH"**
4. Klik "Install Now"
5. Tunggu hingga selesai

#### 2️⃣ Install Aplikasi (Hanya Sekali)

1. Copy folder `shopee-retur-automation-main` ke laptop lain
2. Buka folder tersebut
3. **Double-click file `install.bat`**
4. Tunggu proses download dan instalasi library (sekitar 1-3 menit)
5. Jika muncul "Instalasi berhasil!" berarti siap digunakan

#### 3️⃣ Jalankan Aplikasi (Setiap Kali Mau Pakai)

1. Buka folder aplikasi
2. **Double-click file `run_app.bat`**
3. Tunggu sebentar, browser akan terbuka otomatis
4. Jika tidak otomatis buka, buka browser dan ketik: `http://localhost:8501`
5. ✅ Aplikasi siap digunakan!

#### 4️⃣ Tutup Aplikasi

- Tekan `Ctrl + C` di jendela hitam (command prompt)
- Atau langsung tutup jendela hitam tersebut

---

## 🎯 Cara Menggunakan Aplikasi

### Langkah 1: Upload File dari Shopee

1. Di sidebar kiri, klik **"Browse files"**
2. Pilih file yang sudah di-download dari Shopee:
   - ✅ **CSV** (.csv) - Format standar
   - ✅ **Excel** (.xlsx, .xls) - Bisa juga!
3. Tunggu hingga muncul ✅ "File berhasil diupload!"
4. Akan muncul info jumlah baris dan pesanan

**Format File yang Didukung:**
- ✅ CSV (.csv)
- ✅ Excel (.xlsx, .xls)

**Catatan**: File harus memiliki kolom-kolom berikut:
- No. Pesanan
- Status Pesanan
- Alasan Pembatalan
- Status Pembatalan/ Pengembalian
- No. Resi
- Nomor Referensi SKU
- Nama Produk
- Nama Variasi
- Jumlah
- Returned quantity

### Langkah 2: Lihat Dashboard

1. Klik tab **"📊 Dashboard"**
2. Lihat statistik:
   - Total Retur: Total semua data retur
   - Partial Returns: Retur yang jumlahnya tidak lengkap
   - No Resi Kosong: Data tanpa nomor resi
   - Unique Orders: Jumlah pesanan unik

3. Lihat grafik:
   - Pie chart: Pembagian status pembatalan/pengembalian
   - Bar chart: 5 alasan pembatalan terbanyak

4. Bisa filter data berdasarkan kolom tertentu

### Langkah 3: Cari Data Retur (FITUR UTAMA)

**Mode 1: Manual Input**

1. Klik tab **"🔍 Search & Input"**
2. Pilih mode **"📏 Manual Input"**
3. Di kotak teks besar, ketik/paste nomor pesanan atau nomor resi
4. Bisa input banyak sekaligus (satu nomor per baris)

**Mode 2: Scanner Barcode** 🆕

1. Klik tab **"🔍 Search & Input"**
2. Pilih mode **"📷 Scanner Barcode"**
3. Klik di kolom "Scan Barcode di sini:"
4. **Scan barcode** di paket dengan:
   - USB Barcode Scanner (RECOMMENDED)
   - Atau HP/kamera
5. Hasil **otomatis muncul!**
6. **Lanjut scan paket berikutnya** tanpa klik apapun
7. History scan tersimpan di bawah

📚 **Panduan lengkap scanner:** Lihat file `PANDUAN_SCANNER.md`

**Contoh Manual Input:**
```
260101U95E5RBQ
SPXID067190313141
260109JVE371VN
```

4. Klik tombol **"🔍 Cari"**
5. Hasil akan muncul di bawah dengan informasi lengkap
6. **Alert otomatis** jika ada:
   - ⚠️ Partial return (jumlah retur tidak sesuai)
   - ⚠️ No resi kosong

### Langkah 4: Input Data Tambahan (Unboxing)

Setelah search data, scroll ke bawah ke bagian **"📝 Input Data Tambahan"**

Untuk setiap item yang ditemukan:

1. Klik expander untuk membuka form input
2. Isi data:

   **A. Tanggal**
   - Otomatis terisi tanggal hari ini
   - Bisa diganti jika perlu

   **B. Batch**
   - Ketik nomor batch (contoh: 001, 002, dst)

   **C. Ket Product** (Keterangan Produk)
   Pilih salah satu:
   - OK → Produk dalam kondisi baik
   - Defect → Produk cacat/rusak
   - Kemasan Sudah Dibuka → Kemasan terbuka tapi produk OK
   - Sudah dibuka sealnya → Seal sudah dibuka
   - Packaging terbuka → Packaging tidak utuh
   - IB Rusak → Inner box rusak
   - Produk Kosong → Paket kosong/tidak ada produk
   - Produk Sudah dicoba → Bekas dipakai/dicoba
   - Bukan Produk BLP → Bukan produk dari BLP

   **D. Stock In** (Lokasi Penyimpanan)
   Pilih salah satu:
   - Retur Central → Simpan di gudang retur pusat
   - WH Online → Simpan di warehouse online
   - Prodev → Kirim ke product development

3. Klik **"Simpan Data"** di setiap item

### Langkah 5: Export ke Excel

1. Klik tab **"📥 Export"**
2. Preview data yang akan diexport (pastikan sudah benar)
3. Klik tombol **"📥 Download Excel"**
4. File akan terdownload dengan nama: `Retur_Shopee_YYYYMMDD_HHMMSS.xlsx`
5. File Excel sudah rapi dengan header berwarna

---

## 💡 Tips Workflow Efisien

### Untuk Admin Gudang:

**Di Awal Hari/Minggu:**
1. Download CSV terbaru dari Shopee
2. Upload ke aplikasi

**Saat Terima Paket Retur:**
1. Kumpulkan beberapa paket retur (misal 10-20 paket)
2. Catat semua nomor pesanannya
3. Paste sekaligus ke aplikasi untuk search
4. Buka paket satu per satu sambil lihat info di layar
5. Input data tambahan langsung setelah unboxing
6. Setelah selesai satu batch, export ke Excel

**Keuntungan Cara Ini:**
- ⚡ Lebih cepat dari cek manual satu-satu
- 📊 Langsung dapat statistik
- ⚠️ Otomatis dapat alert jika ada masalah
- 📥 Data langsung tersimpan rapi di Excel

### Multi-Search untuk Efisiensi:

**Scenario 1**: Terima 20 paket retur
```
# Paste sekaligus 20 nomor pesanan
260101U95E5RBQ
260102ABC123XY
260103DEF456ZZ
... (17 lainnya)
```
Klik cari → Langsung dapat info 20 paket sekaligus!

**Scenario 2**: Ada paket tanpa label jelas
- Search pakai nomor resi
- Bisa campur nomor pesanan dan nomor resi

---

## ❓ Troubleshooting (Jika Ada Masalah)

### 1. "Python tidak ditemukan" saat install
**Solusi:**
- Install Python dari https://www.python.org/downloads/
- **PENTING**: Centang "Add Python to PATH" saat install
- Restart komputer setelah install Python
- Coba jalankan `install.bat` lagi

### 2. Browser tidak terbuka otomatis
**Solusi:**
- Buka browser manual
- Ketik di address bar: `http://localhost:8501`

### 3. "Error saat parse CSV"
**Solusi:**
- Pastikan file CSV dari Shopee asli (tidak diedit)
- Pastikan ada 10 kolom wajib
- Coba download ulang CSV dari Shopee

### 4. "Instalasi dependencies gagal"
**Solusi:**
- Pastikan koneksi internet lancar
- Coba jalankan ulang `install.bat`
- Atau install manual:
  ```
  pip install streamlit pandas openpyxl plotly
  ```

### 5. Aplikasi crash/error saat dijalankan
**Solusi:**
- Tutup aplikasi (Ctrl+C)
- Jalankan ulang `run_app.bat`
- Jika masih error, install ulang dengan `install.bat`

### 6. File Excel tidak bisa dibuka
**Solusi:**
- Pastikan ada Microsoft Excel atau LibreOffice
- File Excel ada di folder Downloads browser
- Nama file: `Retur_Shopee_YYYYMMDD_HHMMSS.xlsx`

---

## 📦 Cara Transfer ke Laptop Lain

### Yang Perlu Di-Copy:
1. **Seluruh folder** `shopee-retur-automation-main`
2. Pastikan semua file ada:
   - `app.py`
   - `requirements.txt`
   - `install.bat` ⭐
   - `run_app.bat` ⭐
   - Folder `config/`
   - Folder `utils/`
   - Folder `.streamlit/`
   - Folder `data/`
   - Folder `output/`

### Di Laptop Baru:
1. Install Python (jika belum ada)
2. Copy folder aplikasi
3. Jalankan `install.bat`
4. Jalankan `run_app.bat`
5. ✅ Siap digunakan!

**CATATAN**: File `.bat` hanya untuk Windows. Untuk Mac/Linux, gunakan terminal manual.

---

## 📞 Kontak & Support

Jika ada pertanyaan atau masalah, hubungi developer atau tim IT.

**Happy Processing! 🎉**
