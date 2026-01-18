# 📷 Panduan Menggunakan Scanner Barcode

## 🎯 Fitur Scanner Barcode untuk Admin Gudang

Aplikasi sekarang mendukung **scan barcode** untuk ID Order dan No. Resi! Ini akan sangat mempercepat proses unboxing paket retur.

---

## 🔧 Jenis Scanner yang Didukung

### 1️⃣ **USB Barcode Scanner** (RECOMMENDED)
Scanner barcode USB yang dijual bebas di marketplace.

**Keuntungan:**
- ✅ Paling cepat dan akurat
- ✅ Plug & play (colok USB langsung jalan)
- ✅ Scan otomatis tanpa klik tombol
- ✅ Bisa scan dari jarak jauh
- ✅ Harga murah: Rp 150.000 - Rp 500.000

**Contoh produk:**
- Scanner barcode 1D/2D USB
- Merek: Iware, Yongli, Eppos, dll
- Beli di: Tokopedia, Shopee, Bukalapak

### 2️⃣ **Scanner HP/Tablet**
Menggunakan kamera HP untuk scan barcode.

**Keuntungan:**
- ✅ Tidak perlu beli scanner
- ✅ Pakai HP yang ada
- ✅ Portable

**Kekurangan:**
- ⚠️ Perlu ketik manual atau paste hasil scan
- ⚠️ Agak lambat dibanding USB scanner

---

## 🚀 Cara Menggunakan

### ✅ Dengan USB Scanner (RECOMMENDED)

#### Setup Pertama Kali:

1. **Colok USB Scanner** ke laptop
2. Scanner otomatis terdeteksi (tidak perlu install driver)
3. Test scanner:
   - Buka Notepad
   - Scan barcode apapun
   - Jika muncul text di Notepad = **scanner siap!**

#### Cara Pakai di Aplikasi:

1. **Buka aplikasi** Shopee Retur Automation
2. **Upload file** CSV/Excel dari Shopee
3. **Klik tab** "🔍 Search & Input"
4. **Pilih mode**: "📷 Scanner Barcode"
5. **Klik di kolom input** (kotak "Scan Barcode di sini:")
6. **Scan barcode** di paket:
   - Barcode ID Order (biasanya di label Shopee)
   - Atau barcode No. Resi (di resi pengiriman)
7. **Otomatis muncul hasil!** ✅
8. **Lanjut scan paket berikutnya** (tanpa klik apapun)
9. **Repeat** sampai semua paket ter-scan

**Tips:**
- Cursor harus tetap di kolom input
- Scanner otomatis ketik + enter
- Aplikasi langsung cari data
- History scan tersimpan di bawah

---

### ✅ Dengan HP/Tablet

#### Cara 1: Gunakan App Scanner Barcode

1. Install app scanner barcode di HP:
   - **Android:** "Barcode Scanner" dari Play Store
   - **iOS:** Built-in di Camera app (iOS 11+)
2. Scan barcode dengan app
3. Copy hasil scan (biasanya muncul di notifikasi)
4. Paste di aplikasi mode "📷 Scanner Barcode"
5. Klik tombol "🔍 Scan"

#### Cara 2: Manual Input

1. Lihat ID Order di label paket
2. Ketik di mode "📷 Scanner Barcode"
3. Tekan Enter atau klik "🔍 Scan"

---

## 📋 Workflow Admin Gudang dengan Scanner

### Scenario: Terima 50 Paket Retur

**Tanpa Scanner (Cara Lama):**
1. Lihat ID Order di paket
2. Ketik manual di laptop
3. Klik cari
4. Tunggu hasil
5. Repeat 50x = **~15 menit**

**Dengan USB Scanner (Cara Baru):**
1. Arahkan scanner ke barcode
2. Klik trigger scanner
3. Otomatis muncul hasil
4. Lanjut paket berikutnya
5. Repeat 50x = **~5 menit** ⚡

**Hemat waktu: 66%!**

---

## 🎬 Step-by-Step dengan Gambar

### 1. Pilih Mode Scanner

```
┌─────────────────────────────────────────┐
│ Mode Pencarian:                         │
│ ○ 📝 Manual Input  ● 📷 Scanner Barcode │
└─────────────────────────────────────────┘
```

### 2. Scan Barcode

```
┌─────────────────────────────────────────┐
│ 📷 Mode Scanner Aktif                   │
│                                         │
│ Scan Barcode di sini:                  │
│ [____260101U95E5RBQ___]  [🔍 Scan]     │
│                                         │
│ ✅ Ditemukan 3 item untuk 260101U95E5RBQ│
└─────────────────────────────────────────┘
```

### 3. History Scan

```
┌─────────────────────────────────────────┐
│ 📜 History Scan                         │
│                                         │
│ ✅ [14:23:15] 260101U95E5RBQ - 3 item  │
│ ✅ [14:22:58] SPXID067190313141 - 1 item│
│ ❌ [14:22:45] 123456789 - Tidak ditemukan│
│ ✅ [14:22:30] 260109JVE371VN - 2 item  │
└─────────────────────────────────────────┘
```

### 4. Hasil Gabungan

Semua paket yang di-scan akan digabung di bawah, siap untuk:
- Input data tambahan (Tanggal, Batch, Ket Product, Stock In)
- Export ke Excel

---

## 💡 Tips & Tricks

### ✅ Best Practices:

1. **Atur jarak scan yang pas**
   - USB scanner: 5-15 cm dari barcode
   - Terlalu dekat/jauh = gagal scan

2. **Pencahayaan cukup**
   - Barcode harus jelas terbaca
   - Hindari refleksi/silau

3. **Barcode harus utuh**
   - Tidak sobek/rusak
   - Jika rusak, ketik manual

4. **Scan continuous**
   - Tidak perlu klik tombol di aplikasi
   - Langsung scan paket berikutnya
   - Hemat waktu!

5. **Cek history scan**
   - Pastikan semua paket ter-scan
   - Jika ada yang gagal, scan ulang

6. **Clear history sebelum batch baru**
   - Klik "🗑️ Clear History"
   - Mulai scan batch baru

---

## 🔍 Jenis Barcode yang Didukung

Scanner barcode **1D** (garis):
- ✅ Code 128 (paling umum di Shopee)
- ✅ Code 39
- ✅ EAN-13
- ✅ UPC

Scanner barcode **2D** (QR Code):
- ✅ QR Code
- ✅ Data Matrix

**Catatan:** Barcode di label Shopee biasanya **Code 128** (1D).

---

## 🛒 Rekomendasi Produk Scanner

### Budget: Rp 150.000 - Rp 300.000
**Scanner Barcode 1D USB**
- Merek: Iware, Eppos
- Scan 1D barcode saja (cukup untuk Shopee)
- Plug & play

### Budget: Rp 400.000 - Rp 700.000
**Scanner Barcode 2D USB**
- Merek: Yongli, Iware Pro
- Scan 1D + 2D (QR Code)
- Lebih cepat dan akurat
- **RECOMMENDED untuk intensitas tinggi**

### Budget: Rp 0 (Gratis!)
**Pakai HP**
- Gunakan kamera HP
- Install app scanner
- Agak lambat tapi bisa dipakai

---

## ⚠️ Troubleshooting

### ❌ Scanner tidak berfungsi

**Solusi:**
1. Cek koneksi USB (cabut-colok ulang)
2. Test di Notepad (scan harusnya muncul text)
3. Restart laptop
4. Ganti port USB

### ❌ Scan tidak otomatis search

**Solusi:**
1. Pastikan cursor di kolom input
2. Klik kolom input sebelum scan
3. Scanner harus setting "Enter after scan"
4. Cek manual scanner untuk setting

### ❌ Barcode tidak terbaca

**Solusi:**
1. Cek pencahayaan
2. Barcode tidak boleh sobek/rusak
3. Atur jarak scanner (5-15 cm)
4. Coba beberapa angle berbeda
5. Jika tetap gagal, ketik manual

### ❌ Hasil scan salah/random character

**Solusi:**
1. Scanner mungkin setting wrong encoding
2. Reset scanner ke factory default
3. Scan barcode "Factory Reset" di manual scanner
4. Atau ganti scanner

---

## 📊 Perbandingan Workflow

| Aspek | Manual Input | USB Scanner | HP Scanner |
|-------|--------------|-------------|------------|
| **Kecepatan** | ⭐⭐ Lambat | ⭐⭐⭐⭐⭐ Super cepat | ⭐⭐⭐ Cukup cepat |
| **Akurasi** | ⭐⭐⭐ Bisa salah ketik | ⭐⭐⭐⭐⭐ 99.9% akurat | ⭐⭐⭐⭐ Akurat |
| **Biaya** | Gratis | Rp 150K - 700K | Gratis |
| **Setup** | - | Plug & play | Install app |
| **Cocok untuk** | 1-10 paket | 10-500+ paket | 1-50 paket |

---

## 🎯 Kesimpulan

**Untuk admin gudang yang handle banyak retur:**
👉 **Beli USB Scanner** (Rp 300K-500K)
- Investasi terbayar dalam 1 minggu
- Hemat waktu 60-70%
- Kurangi error ketik
- Lebih produktif

**Untuk testing/penggunaan sesekali:**
👉 **Pakai HP** atau **Manual Input**
- Tidak perlu invest scanner dulu
- Test dulu workflow
- Upgrade ke scanner kalau cocok

---

## 📞 Rekomendasi Setup

### Setup Ideal untuk Gudang:
1. **1 Laptop** - Aplikasi Shopee Retur
2. **1 USB Scanner 2D** (Rp 500K)
3. **1 Meja** untuk unboxing
4. **Pencahayaan** yang cukup

### Workflow Optimal:
1. Upload CSV Shopee di awal hari
2. Kumpulkan paket retur (batch 20-50 paket)
3. Scan semua barcode (5-10 menit)
4. Unboxing sambil input data tambahan
5. Export Excel di akhir shift
6. **Done!** ✅

---

**Happy Scanning! 📷🚀**
