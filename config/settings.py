"""Configuration settings for Shopee Retur Automation."""

# Kolom yang diharapkan dari file CSV Shopee
SHOPEE_COLUMNS = [
    'No. Pesanan',
    'Status Pesanan',
    'Alasan Pembatalan',
    'Status Pembatalan/ Pengembalian',
    'No. Resi',
    'Nomor Referensi SKU',
    'Nama Produk',
    'Nama Variasi',
    'Jumlah',
    'Returned quantity'
]

# Kolom tambahan yang akan ditambahkan user
ADDITIONAL_COLUMNS = ['Tanggal', 'Batch', 'Barcode di Paket', 'Ket Product', 'Stock In', 'Catatan Mismatch']

# Opsi untuk dropdown Keterangan Product
KET_PRODUCT_OPTIONS = [
    'OK',
    'Defect',
    'Kemasan Sudah Dibuka',
    'Sudah dibuka sealnya',
    'Packaging terbuka',
    'IB Rusak',
    'Produk Kosong',
    'Produk Sudah dicoba',
    'Bukan Produk BLP'
]

# Opsi untuk dropdown Stock In
STOCK_IN_OPTIONS = [
    'Retur Central',
    'WH Online',
    'Prodev'
]

# Kolom yang digunakan untuk pencarian
SEARCH_COLUMNS = ['No. Pesanan', 'No. Resi']
