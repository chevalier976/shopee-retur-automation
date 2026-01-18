# 🆕 Panduan Handle Retur Baru (Belum di CSV)

## ❓ Problem: Paket Datang Duluan, Data Belum Update

### Scenario Real di Lapangan:

**Situasi yang Sering Terjadi:**
```
Hari Senin Pagi:
- Admin terima paket retur dari kurir
- Scan barcode: JNT1234567890
- ❌ Tidak ketemu di sistem
- ❌ Cari manual juga tidak ada

Ternyata:
- Paket BARU return kemarin sore
- Data di marketplace belum ter-update/sync
- CSV yang di-upload pagi tadi belum include order ini
- Admin stuck, tidak bisa proses paket
```

### Penyebab:
1. **Delay Update Marketplace** - Shopee/marketplace update data 1-24 jam
2. **CSV Download Timing** - Admin download CSV pagi, paket datang siang
3. **Manual Retur** - Customer langsung kirim tanpa report dulu
4. **System Lag** - Kurir update tracking lebih cepat dari marketplace

---

## ✅ SOLUSI: Fitur "Input Retur Baru"

Aplikasi sekarang bisa **handle retur yang belum ada di CSV!**

### 🎯 Workflow Baru:

```
1. Scan barcode → ❌ Tidak ketemu
   ↓
2. Pilih: "📦 Input Retur Baru (Belum di CSV)"
   ↓
3. Cek marketplace/sistem untuk data order
   ↓
4. Input manual: ID Order, SKU, Produk, dll
   ↓
5. Simpan sebagai "RETUR BARU"
   ↓
6. Lanjut proses seperti biasa
   ↓
7. Export dengan flag "🆕 RETUR BARU"
   ↓
8. Besok: Update CSV & re-check
```

---

## 🎬 Tutorial Step-by-Step

### Scenario: Paket Retur Baru Datang

**Situasi:**
- Paket dari JNT: `JNT9876543210`
- Cek label: ID Order `260105NEWORDER`
- Scan di aplikasi: ❌ Tidak ketemu
- Cari manual: ❌ Tidak ada di CSV

**Action:**

#### Step 1: Scan & Pilih Opsi
```
Mode: 📷 Scanner Barcode
Scan: JNT9876543210
Result: ❌ Tidak ditemukan

Muncul popup:
🔧 Barcode tidak ditemukan? Pilih opsi
⚠️ Kemungkinan:
1. Barcode di paket BERBEDA dengan data sistem
2. Data BELUM TER-UPDATE di CSV Shopee

○ 🔗 Link ke Order Existing
● 📦 Input Retur Baru (Belum di CSV)
```

#### Step 2: Pilih "Input Retur Baru"
```
📦 Input data retur baru (belum ada di CSV):
💡 Data ini akan disimpan sementara dan di-export 
   dengan flag 'RETUR BARU'
```

#### Step 3: Cek Data di Marketplace
**Buka Shopee Seller Center:**
- Search order: `260105NEWORDER`
- Lihat detail:
  - ID Order: `260105NEWORDER`
  - SKU: `BLP-CREAM-001`
  - Produk: `BLP Beauty Cream 30ml`
  - No. Resi: `SPXID888777666`
  - Qty: 1

#### Step 4: Input ke Aplikasi
```
ID Order: [260105NEWORDER]
No. Resi: [SPXID888777666]
SKU Produk: [BLP-CREAM-001]
Qty Retur: [1]
Nama Produk: [BLP Beauty Cream 30ml]
Catatan: [Data belum sync dari Shopee, paket datang duluan]

[💾 Simpan Retur Baru]
```

#### Step 5: Berhasil!
```
✅ Retur baru berhasil disimpan: 260105NEWORDER
💡 Data akan di-export dengan flag 'RETUR BARU'
   Jangan lupa update CSV dan re-check nanti!

History Scan:
🆕 [10:15:30] JNT9876543210 (RETUR BARU) - 1 item
```

#### Step 6: Lanjut Input Data
```
Expander otomatis terbuka:
🆕 RETUR BARU - 📦 260105NEWORDER - BLP-CREAM-001...

🆕 RETUR BARU - Data belum ada di CSV Shopee
⚠️ ACTION REQUIRED: Update CSV dan re-check nanti!
💡 Catatan: Data belum sync dari Shopee...

[Form input Tanggal, Batch, Ket Product, Stock In]
```

#### Step 7: Export
```
Excel akan berisi:
┌──────────────────────────────────────────────┐
│ Flag         │ ID Order      │ SKU          │
├──────────────────────────────────────────────┤
│ 🆕 RETUR BARU│ 260105NEW...  │ BLP-CREAM... │
│ (normal)     │ 260101...     │ BLP-SERUM... │
│ (normal)     │ 260102...     │ BLP-MASK...  │
└──────────────────────────────────────────────┘

Column "Catatan Mismatch":
"⚠️ RETUR BARU - Belum ada di CSV. 
Data belum sync dari Shopee, paket datang duluan"
```

---

## 📋 Checklist Handle Retur Baru

### Saat Terima Paket:
- [ ] Scan barcode
- [ ] Jika tidak ketemu, pilih "Input Retur Baru"
- [ ] Buka marketplace/sistem seller
- [ ] Search ID Order (dari label paket)
- [ ] Copy data: ID Order, SKU, Produk, No. Resi, Qty
- [ ] Input ke aplikasi
- [ ] Simpan dengan catatan jelas
- [ ] Lanjut input data (Batch, Ket Product, Stock In)
- [ ] Export

### Di Akhir Hari/Besok:
- [ ] Download CSV Shopee terbaru
- [ ] Upload ke aplikasi
- [ ] Search ID Order yang "RETUR BARU"
- [ ] ✅ Jika ketemu → Data sudah sync, OK!
- [ ] ❌ Jika belum → Follow up ke marketplace

---

## 💡 Best Practices

### ✅ Do's:

1. **Selalu cek marketplace** sebelum input manual
   - Pastikan order benar-benar ada
   - Copy data akurat
   - Jangan asal input

2. **Isi catatan dengan detail**
   ```
   Contoh bagus:
   - "Paket datang pagi, CSV download jam 8, order ini jam 9 kemarin"
   - "Customer langsung kirim tanpa konfirmasi dulu"
   - "Retur via SPX, Shopee belum sync tracking"
   ```

3. **Flag & tracking**
   - Catat semua "RETUR BARU" di Excel
   - Buat list untuk re-check besok
   - Follow up yang belum muncul di CSV

4. **Koordinasi tim**
   - Inform manager ada retur baru
   - Update group chat
   - Track berapa % yang belum di CSV

5. **Double-check besok**
   - Upload CSV fresh
   - Search lagi ID Order
   - Update status di sistem

### ❌ Don'ts:

1. **Jangan skip** retur yang tidak ketemu
   - Pakai fitur "Input Retur Baru"
   - Jangan ditumpuk/pending

2. **Jangan asal input** data
   - Cek marketplace dulu
   - Pastikan ID Order benar
   - Salah input = data kacau

3. **Jangan lupa re-check**
   - "RETUR BARU" bukan final
   - Harus di-verify besok
   - Update CSV rutin

---

## 📊 Monitoring & Reporting

### Daily Report:

```
RETUR HARI INI: 50 paket
├─ From CSV: 45 paket ✅
├─ RETUR BARU: 5 paket 🆕
│  ├─ 260105NEWORDER
│  ├─ 260106ABCXYZ
│  ├─ 260107QWERTY
│  ├─ 260108UIOP
│  └─ 260109ASDF
└─ Action: Re-check besok!
```

### Weekly Analysis:

| Minggu | Total Retur | Retur Baru | % | Status |
|--------|-------------|------------|---|--------|
| Week 1 | 250 | 15 | 6% | Normal |
| Week 2 | 280 | 40 | 14% | ⚠️ High |
| Week 3 | 300 | 8 | 2.6% | ✅ Good |

**Action jika % tinggi:**
- Koordinasi dengan marketplace
- Check delay update system
- Minta prioritas sync data

---

## 🔧 Troubleshooting

### Q1: Retur baru tidak muncul di CSV besok juga?
**A:**
1. **Cek lagi di marketplace** - Mungkin order ID salah
2. **Search dengan No. Resi** - Coba search pakai resi
3. **Contact marketplace support** - Ada issue?
4. **Verify dengan customer** - Order benar?

### Q2: Salah input data retur baru?
**A:**
- Data masih di session state
- Bisa delete dari hasil search
- Re-input dengan benar
- Atau edit di Excel hasil export

### Q3: Banyak sekali retur baru setiap hari?
**A:**
**Penyebab:**
- Timing download CSV kurang tepat
- Marketplace lag tinggi
- Customer banyak langsung kirim

**Solusi:**
- Download CSV multiple times per hari
- Pagi, siang, sore
- Atau pakai API jika tersedia

### Q4: ID Order di paket tidak jelas?
**A:**
1. Foto paket & label
2. Search di marketplace pakai info lain:
   - No. HP customer
   - Produk + tanggal order
3. WA/email customer minta ID Order
4. Last resort: Simpan dulu pakai barcode sebagai ID temp

---

## 📈 Statistik & Insights

### Pattern yang Sering:

**Waktu Retur Baru Paling Banyak:**
- Senin pagi (retur weekend)
- Setelah jam 12 (CSV pagi belum include)
- Hari libur + 1 (backlog)

**Kurir dengan Retur Baru Tinggi:**
- SPX (tracking update cepat)
- JNT (langsung kirim)
- Grab/Gojek (instant delivery)

**Kategori Produk:**
- Flash sale items (banyak return)
- Pre-order (confuse dengan regular)

**Gunakan data ini:**
- Adjust timing download CSV
- Koordinasi dengan kurir
- Warning customer tentang return process

---

## 🎯 SOP Lengkap

### Standard Operating Procedure:

#### Pagi (Shift Start):
1. Download CSV Shopee terbaru
2. Upload ke aplikasi
3. Siap scan

#### Saat Terima Paket:
1. Scan barcode
2. **Jika ketemu:**
   - Lanjut proses normal
   - Input data
3. **Jika tidak ketemu:**
   - Cek label untuk ID Order
   - Pilih opsi:
     - Link to existing (jika barcode beda)
     - Input Retur Baru (jika belum di CSV)
   - Cek marketplace
   - Input data manual
   - Simpan dengan catatan

#### Akhir Shift:
1. Export Excel
2. Review list "RETUR BARU"
3. Report ke manager
4. Set reminder untuk re-check besok

#### Besok Pagi:
1. Download CSV fresh
2. Upload ke aplikasi
3. Search semua ID "RETUR BARU" kemarin
4. ✅ Update status yang sudah muncul
5. ❌ Follow up yang belum muncul

---

## 🎉 Benefits Fitur Ini:

✅ **No More Stuck** - Admin tidak stuck saat paket tidak ketemu
✅ **Full Coverage** - 100% paket bisa diproses
✅ **Tracking** - Semua retur baru ter-record
✅ **Audit Trail** - Clear documentation
✅ **Flexibility** - Handle delay system
✅ **Productivity** - Tidak perlu tunggu CSV update
✅ **Accuracy** - Data tetap lengkap & akurat

---

## 📝 Summary

**Fitur "Input Retur Baru" menyelesaikan masalah:**

1. ❌ Paket datang duluan, CSV belum update
2. ❌ Admin stuck tidak bisa proses
3. ❌ Data hilang/tidak tercatat

**Dengan solusi:**

1. ✅ Input manual dengan cek marketplace
2. ✅ Flag "RETUR BARU" untuk tracking
3. ✅ Export dengan catatan lengkap
4. ✅ Re-check & verify besok
5. ✅ 100% paket ter-handle

**Aplikasi sekarang production-ready untuk handle SEMUA scenario, termasuk edge cases!** 🎉🆕
