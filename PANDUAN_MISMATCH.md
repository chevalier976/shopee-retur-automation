# 🔧 Panduan Mengatasi Barcode Mismatch

## ❓ Problem: Barcode di Paket Berbeda dengan Data Sistem

### Scenario yang Sering Terjadi:

**Case 1: Barcode di paket adalah ID Order, tapi sistem punya No. Resi berbeda**
```
Barcode di paket: 260101U95E5RBQ
Data di sistem:
  - ID Order: 260101U95E5RBQ ✅ (match)
  - No. Resi: SPXID067190313141
```
✅ **Solusi:** Scan akan otomatis ketemu!

---

**Case 2: Barcode di paket adalah No. Resi yang berbeda**
```
Barcode di paket: SPXID999888777
Data di sistem:
  - ID Order: 260101U95E5RBQ
  - No. Resi: SPXID067190313141 ❌ (tidak match!)
```
❌ **Problem:** Scan tidak ketemu karena No. Resi berbeda!

---

**Case 3: Barcode di paket totally berbeda (barcode kurir/internal)**
```
Barcode di paket: JNT1234567890
Data di sistem:
  - ID Order: 260101U95E5RBQ
  - No. Resi: SPXID067190313141
```
❌ **Problem:** Barcode kurir tidak ada di data Shopee!

---

## ✅ SOLUSI: Fitur Manual Link

Aplikasi sekarang punya **3 cara** untuk handle mismatch:

### 1️⃣ **Auto-Detection & Warning**

Saat scan barcode yang tidak match:
```
❌ Tidak ditemukan: JNT1234567890

🔧 Barcode tidak ditemukan? Cari manual di sini
⚠️ Kemungkinan barcode di paket BERBEDA dengan data di sistem
```

### 2️⃣ **Manual Link** (RECOMMENDED)

**Langkah-langkah:**

1. **Scan barcode** di paket (misal: `JNT1234567890`)
2. **Tidak ketemu** ❌
3. **Cek label paket** - Cari ID Order atau No. Resi Shopee
4. **Ketik manual** ID yang benar (misal: `260101U95E5RBQ`)
5. **Klik "🔍 Cari Manual"**
6. **Berhasil!** ✅ System akan link barcode tersebut ke order yang benar

**Hasil:**
- Order ditemukan ✅
- Barcode aktual di paket tersimpan: `JNT1234567890`
- ID Order di sistem: `260101U95E5RBQ`
- Otomatis ada catatan mismatch
- Data lengkap untuk export

---

### 3️⃣ **Field "Barcode Aktual di Paket"**

Di form input data, sekarang ada field:

```
┌─────────────────────────────────────────────┐
│ 📷 Info Barcode:                            │
│                                             │
│ Di Sistem:              Barcode Aktual      │
│ - ID Order: 260101...   [JNT1234567890]    │
│ - No. Resi: SPXID...                        │
│                         ❌ TIDAK MATCH!     │
└─────────────────────────────────────────────┘
```

**Fungsi:**
- Catat barcode yang sebenarnya di paket
- Deteksi otomatis jika tidak match
- Warning jika beda
- Field "Catatan Mismatch" otomatis muncul

---

## 🎬 Tutorial Step-by-Step

### Scenario: Paket dengan Barcode Kurir (Bukan Shopee)

**Situasi:**
- Admin terima paket dari JNT
- Barcode di paket: `JNT1234567890` (barcode kurir)
- ID Order Shopee: `260101U95E5RBQ` (di label kecil)

**Workflow:**

#### Step 1: Scan Barcode Kurir
```
📷 Scanner Mode
Scan: JNT1234567890
❌ Tidak ditemukan
```

#### Step 2: Manual Link
```
🔧 Barcode tidak ditemukan? Cari manual
Ketik ID Order: 260101U95E5RBQ
Klik: 🔍 Cari Manual
✅ Berhasil link!
```

#### Step 3: Data Tercatat
```
Order: 260101U95E5RBQ ✅
Barcode di Paket: JNT1234567890
Catatan: "Barcode di paket (JNT1234567890) tidak match, 
          manual link ke 260101U95E5RBQ"
```

#### Step 4: Export
Excel akan contain:
- ID Order: 260101U95E5RBQ
- No. Resi: SPXID...
- **Barcode di Paket**: JNT1234567890
- **Catatan Mismatch**: Auto-filled
- Semua data lainnya

---

## 💡 Best Practices

### ✅ Do's:

1. **Selalu cek label paket** jika scan tidak ketemu
   - Cari stiker Shopee
   - Biasanya ada ID Order atau No. Resi

2. **Gunakan Manual Link** jika barcode berbeda
   - Lebih akurat
   - Data lengkap tercatat

3. **Isi Catatan Mismatch** dengan jelas
   ```
   Contoh:
   - "Paket pakai barcode JNT, bukan Shopee"
   - "Resi di paket beda dengan sistem"
   - "Label rusak, ketik manual dari WA customer"
   ```

4. **Double-check** sebelum save
   - Pastikan ID Order benar
   - Pastikan produk match

5. **Foto paket** jika perlu bukti
   - Terutama untuk case mismatch
   - Lampirkan di sistem lain

### ❌ Don'ts:

1. **Jangan skip** jika tidak ketemu
   - Pakai manual link
   - Jangan abaikan paket

2. **Jangan asal ketik** ID Order
   - Salah ketik = salah data
   - Cek 2-3x sebelum submit

3. **Jangan lupa isi catatan** mismatch
   - Penting untuk tracking
   - Audit trail

---

## 📊 Contoh Real Cases

### Case 1: Paket JNT Express
```
Barcode scan: JNT1234567890 ❌ (tidak ketemu)
↓
Cek label: ID Order = 260101U95E5RBQ
↓
Manual link: 260101U95E5RBQ ✅
↓
Result:
- Order: 260101U95E5RBQ
- Barcode Paket: JNT1234567890
- Catatan: "Paket pakai resi JNT"
```

### Case 2: Label Rusak/Hilang
```
Barcode scan: [Tidak bisa scan, label rusak]
↓
Cek WA/Email customer: ID Order = 260102ABC123
↓
Ketik manual: 260102ABC123 ✅
↓
Result:
- Order: 260102ABC123
- Barcode Paket: [kosong atau "MANUAL"]
- Catatan: "Label rusak, data dari WA customer"
```

### Case 3: Resi Berbeda (Re-ship)
```
Barcode scan: SPXID999888777 ❌ (tidak ketemu)
↓
Cek sistem: Order 260103XYZ pakai resi lama SPXID111222
↓
Manual link: 260103XYZ ✅
↓
Result:
- Order: 260103XYZ
- Barcode Paket: SPXID999888777
- Catatan: "Paket re-ship, resi baru SPXID999888777"
```

---

## 🚨 Troubleshooting

### Q1: Scan tidak ketemu, tapi yakin ada di sistem?
**A:** 
1. Cek ID Order di CSV yang di-upload
2. Pastikan CSV ter-update
3. Coba search manual di tab Manual Input
4. Re-upload CSV jika perlu

### Q2: Manual link juga tidak ketemu?
**A:**
1. **ID Order salah ketik** - Cek lagi
2. **Order belum di CSV** - Update CSV
3. **Typo di CSV** - Fix CSV, re-upload

### Q3: Satu paket, banyak barcode?
**A:**
- Scan/input yang paling jelas
- Atau yang match dengan sistem
- Catat barcode lainnya di "Catatan Mismatch"

### Q4: Tidak ada barcode sama sekali?
**A:**
- Cek label: Harus ada ID Order minimal
- Cari di WA/email customer
- Ketik manual (mode Manual Input)
- Isi field "Barcode di Paket" dengan "MANUAL"

---

## 📋 Checklist Handle Mismatch

Saat ketemu paket dengan barcode berbeda:

- [ ] Scan barcode di paket
- [ ] Jika tidak ketemu, check label untuk ID Order Shopee
- [ ] Gunakan Manual Link dengan ID Order yang benar
- [ ] Verify data yang muncul (produk, qty, dll)
- [ ] Isi field "Barcode di Paket" (otomatis terisi)
- [ ] Review "Catatan Mismatch" (otomatis terisi)
- [ ] Edit catatan jika perlu penjelasan tambahan
- [ ] Lanjut input data lainnya (Tanggal, Batch, Ket Product, Stock In)
- [ ] Save & export

---

## 📈 Statistik Mismatch

Di tab Export, Anda bisa filter:
- ✅ Berapa paket yang match
- ⚠️ Berapa paket dengan mismatch
- 🔗 Berapa yang manual link
- 📊 Pattern: Barcode kurir mana yang sering berbeda

**Gunakan data ini untuk:**
- Koordinasi dengan kurir
- Update SOP
- Training admin baru

---

## 🎯 Summary

**3 Fitur Baru untuk Handle Mismatch:**

1. **Auto-Detection** - Warning otomatis jika barcode tidak match
2. **Manual Link** - Link barcode yang di-scan ke order yang benar
3. **Tracking Fields** - "Barcode di Paket" & "Catatan Mismatch" untuk dokumentasi

**Benefits:**
- ✅ Tidak ada paket yang "hilang" karena barcode beda
- ✅ Data lengkap dan akurat
- ✅ Audit trail clear
- ✅ Mudah track issue
- ✅ Training admin lebih mudah

**Aplikasi sekarang handle 100% case, termasuk mismatch!** 🎉
