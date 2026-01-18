"""
Shopee Retur Automation - Streamlit Application
Aplikasi untuk mengotomasi proses data retur dari marketplace Shopee
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Import modules
from utils.parser import parse_shopee_file, get_dataframe_info
from utils.search import search_orders, get_search_summary, highlight_alerts, combine_product_variant
from utils.export import export_to_excel, generate_filename
from config.settings import (
    SHOPEE_COLUMNS, 
    ADDITIONAL_COLUMNS, 
    KET_PRODUCT_OPTIONS, 
    STOCK_IN_OPTIONS
)

# Page configuration
st.set_page_config(
    page_title="Shopee Retur Automation",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #EE4D2D;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .alert-warning {
        background-color: #fff3cd;
        padding: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
    }
    .alert-success {
        background-color: #d4edda;
        padding: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = None
if 'search_results' not in st.session_state:
    st.session_state.search_results = None
if 'input_data' not in st.session_state:
    st.session_state.input_data = {}


def main():
    """Main application function."""
    
    # Header
    st.markdown('<p class="main-header">📦 Shopee Retur Automation</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📁 Upload File")
        uploaded_file = st.file_uploader(
            "Upload CSV atau Excel Shopee",
            type=['csv', 'xlsx', 'xls'],
            help="Upload file CSV atau Excel (.xlsx) dari Shopee dengan data retur"
        )
        
        if uploaded_file is not None:
            try:
                with st.spinner("Memproses file..."):
                    df = parse_shopee_file(uploaded_file, uploaded_file.name)
                    st.session_state.uploaded_data = df
                    
                    # Show file info
                    info = get_dataframe_info(df)
                    st.success("✅ File berhasil diupload!")
                    st.info(f"📊 Total baris: {info['total_rows']}")
                    st.info(f"📦 Total pesanan: {info['total_orders']}")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.uploaded_data = None
        
        st.markdown("---")
        st.markdown("### 📖 Panduan Singkat")
        st.markdown("""
        1. Upload file CSV/Excel Shopee
        2. Lihat Dashboard untuk statistik
        3. Gunakan Search untuk cari data
        4. Input data tambahan
        5. Download hasil ke Excel
        """)
    
    # Main content
    if st.session_state.uploaded_data is not None:
        # Create tabs
        tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🔍 Search & Input", "📥 Export"])
        
        with tab1:
            show_dashboard(st.session_state.uploaded_data)
        
        with tab2:
            show_search_and_input(st.session_state.uploaded_data)
        
        with tab3:
            show_export()
    else:
        st.info("👈 Silakan upload file CSV atau Excel Shopee di sidebar untuk memulai")
        
        # Show sample data info
        st.markdown("### 📋 Format File yang Didukung")
        st.markdown("**✅ CSV (.csv)** - Format standar dari export Shopee")
        st.markdown("**✅ Excel (.xlsx, .xls)** - Bisa juga upload file Excel!")
        st.markdown("")
        st.markdown("File harus mengandung kolom-kolom berikut:")
        cols = st.columns(2)
        with cols[0]:
            st.markdown("**Kolom Wajib:**")
            for col in SHOPEE_COLUMNS[:5]:
                st.markdown(f"- {col}")
        with cols[1]:
            st.markdown("**Kolom Wajib (lanjutan):**")
            for col in SHOPEE_COLUMNS[5:]:
                st.markdown(f"- {col}")


def show_dashboard(df: pd.DataFrame):
    """Display dashboard with statistics."""
    st.header("📊 Dashboard Overview")
    
    # Metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_returns = len(df)
        st.metric("Total Retur", total_returns)
    
    with col2:
        partial_returns = len(df[(df['Returned quantity'] < df['Jumlah']) & 
                                 (df['Returned quantity'] > 0) & 
                                 (df['Jumlah'] > 0)])
        st.metric("Partial Returns", partial_returns, 
                 delta="⚠️" if partial_returns > 0 else None)
    
    with col3:
        no_resi_empty = len(df[df['No. Resi'].astype(str).str.strip() == ''])
        st.metric("No Resi Kosong", no_resi_empty,
                 delta="⚠️" if no_resi_empty > 0 else None)
    
    with col4:
        unique_orders = df['No. Pesanan'].nunique()
        st.metric("Unique Orders", unique_orders)
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Status Pembatalan/Pengembalian")
        status_counts = df['Status Pembatalan/ Pengembalian'].value_counts()
        if len(status_counts) > 0:
            # Remove empty values
            status_counts = status_counts[status_counts.index != '']
            if len(status_counts) > 0:
                fig = px.pie(
                    values=status_counts.values,
                    names=status_counts.index,
                    hole=0.4
                )
                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Tidak ada data status pembatalan/pengembalian")
        else:
            st.info("Tidak ada data status pembatalan/pengembalian")
    
    with col2:
        st.subheader("📊 Top 5 Alasan Pembatalan")
        # Get cancellation reasons (non-empty)
        reasons = df[df['Alasan Pembatalan'].astype(str).str.strip() != '']['Alasan Pembatalan']
        if len(reasons) > 0:
            reason_counts = reasons.value_counts().head(5)
            fig = px.bar(
                x=reason_counts.values,
                y=reason_counts.index,
                orientation='h',
                labels={'x': 'Jumlah', 'y': 'Alasan'},
            )
            fig.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Tidak ada data alasan pembatalan")
    
    # Detailed table
    st.markdown("---")
    st.subheader("📋 Data Detail")
    
    # Add filter options
    col1, col2 = st.columns(2)
    with col1:
        status_filter = st.multiselect(
            "Filter Status Pesanan",
            options=df['Status Pesanan'].unique().tolist(),
            default=df['Status Pesanan'].unique().tolist()
        )
    with col2:
        show_alerts_only = st.checkbox("Tampilkan hanya dengan alert", value=False)
    
    # Filter data
    filtered_df = df[df['Status Pesanan'].isin(status_filter)]
    
    if show_alerts_only:
        # Show only rows with partial returns or empty resi
        mask = ((filtered_df['Returned quantity'] < filtered_df['Jumlah']) & 
                (filtered_df['Returned quantity'] > 0) & 
                (filtered_df['Jumlah'] > 0)) | \
               (filtered_df['No. Resi'].astype(str).str.strip() == '')
        filtered_df = filtered_df[mask]
    
    # Display dataframe
    st.dataframe(filtered_df, use_container_width=True, height=400)


def show_search_and_input(df: pd.DataFrame):
    """Display search interface and input form."""
    st.header("🔍 Cari Data Retur")
    
    # Initialize session state for scanner mode
    if 'scanner_mode' not in st.session_state:
        st.session_state.scanner_mode = False
    if 'scan_history' not in st.session_state:
        st.session_state.scan_history = []
    if 'scanner_input' not in st.session_state:
        st.session_state.scanner_input = ""
    if 'new_returns' not in st.session_state:
        st.session_state.new_returns = []  # Store retur baru yang belum di CSV
    
    # Mode selection
    col1, col2 = st.columns([3, 1])
    with col1:
        mode = st.radio(
            "Mode Pencarian:",
            ["📝 Manual Input", "📷 Scanner Barcode"],
            horizontal=True,
            key="search_mode"
        )
    with col2:
        if mode == "📷 Scanner Barcode" and len(st.session_state.scan_history) > 0:
            if st.button("🗑️ Clear History"):
                st.session_state.scan_history = []
                st.session_state.search_results = None
                st.rerun()
    
    st.markdown("---")
    
    # Scanner Mode
    if mode == "📷 Scanner Barcode":
        st.info("📷 **Mode Scanner Aktif** - Scan barcode ID Order atau No. Resi dengan scanner USB atau kamera HP")
        
        # Scanner input with auto-submit
        col1, col2 = st.columns([3, 1])
        with col1:
            # Use text input for scanner (barcode scanner works like keyboard)
            scanner_input = st.text_input(
                "Scan Barcode di sini:",
                key="scanner_input_field",
                placeholder="Arahkan cursor di sini, lalu scan barcode...",
                help="Scanner akan otomatis input data. Tekan Enter atau klik Scan untuk memproses."
            )
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Spacing
            scan_btn = st.button("🔍 Scan", type="primary", use_container_width=True)
        
        # Auto-search when scanner input is received
        if scanner_input and scanner_input.strip() and (scan_btn or scanner_input != st.session_state.scanner_input):
            barcode = scanner_input.strip()
            st.session_state.scanner_input = scanner_input
            
            with st.spinner(f"Mencari {barcode}..."):
                # Search for this barcode
                results = search_orders(df, barcode)
                
                if len(results) > 0:
                    # Add to scan history
                    st.session_state.scan_history.insert(0, {
                        'barcode': barcode,
                        'time': datetime.now().strftime("%H:%M:%S"),
                        'results': results,
                        'status': 'success'
                    })
                    
                    # Update search results with all scanned items
                    all_results = []
                    for scan in st.session_state.scan_history:
                        if scan['status'] == 'success':
                            all_results.append(scan['results'])
                    
                    if all_results:
                        st.session_state.search_results = pd.concat(all_results, ignore_index=True).drop_duplicates()
                    
                    st.success(f"✅ Ditemukan {len(results)} item untuk {barcode}")
                    st.balloons()
                else:
                    st.session_state.scan_history.insert(0, {
                        'barcode': barcode,
                        'time': datetime.now().strftime("%H:%M:%S"),
                        'results': None,
                        'status': 'not_found'
                    })
                    st.error(f"❌ Tidak ditemukan: {barcode}")
                    
                    # Show manual search option for mismatch case
                    with st.expander("🔧 Barcode tidak ditemukan? Pilih opsi", expanded=True):
                        st.warning("⚠️ Kemungkinan:")
                        st.markdown("1. **Barcode di paket BERBEDA** dengan data di sistem")
                        st.markdown("2. **Data BELUM TER-UPDATE** di CSV Shopee (retur baru)")
                        
                        option = st.radio(
                            "Pilih cara handle:",
                            ["🔗 Link ke Order Existing (Barcode Beda)", "📦 Input Retur Baru (Belum di CSV)"],
                            key=f"option_{barcode}"
                        )
                        
                        if option == "🔗 Link ke Order Existing (Barcode Beda)":
                            st.markdown("**Cari order yang sudah ada di sistem:**")
                            manual_search = st.text_input(
                                "Ketik ID Order atau No. Resi yang benar:",
                                key=f"manual_search_{barcode}",
                                placeholder="Contoh: 260101U95E5RBQ atau SPXID067190313141"
                            )
                            
                            if st.button("🔍 Cari Manual", key=f"btn_manual_{barcode}"):
                                if manual_search.strip():
                                    manual_results = search_orders(df, manual_search.strip())
                                    if len(manual_results) > 0:
                                        # Add to history with note
                                        st.session_state.scan_history.insert(0, {
                                            'barcode': f"{barcode} → {manual_search.strip()}",
                                            'time': datetime.now().strftime("%H:%M:%S"),
                                            'results': manual_results,
                                            'status': 'manual_link'
                                        })
                                        
                                        # Update search results
                                        all_results = []
                                        for scan in st.session_state.scan_history:
                                            if scan['status'] in ['success', 'manual_link'] and scan['results'] is not None:
                                                all_results.append(scan['results'])
                                        
                                        if all_results:
                                            st.session_state.search_results = pd.concat(all_results, ignore_index=True).drop_duplicates()
                                        
                                        # Set the original scanned barcode to this order
                                        for idx in manual_results.index:
                                            if idx not in st.session_state.input_data:
                                                st.session_state.input_data[idx] = {
                                                    'Tanggal': datetime.now().strftime("%Y-%m-%d"),
                                                    'Batch': '',
                                                    'Barcode di Paket': barcode,  # Original scanned barcode
                                                    'Ket Product': 'OK',
                                                    'Stock In': 'Retur Central',
                                                    'Catatan Mismatch': f"Barcode di paket ({barcode}) tidak match, manual link ke {manual_search.strip()}"
                                                }
                                        
                                        st.success(f"✅ Berhasil link barcode {barcode} ke order {manual_search.strip()}")
                                        st.rerun()
                                    else:
                                        st.error(f"❌ Tidak ditemukan: {manual_search.strip()}")
                                else:
                                    st.warning("Masukkan ID Order atau No. Resi")
                        
                        else:  # Input Retur Baru
                            st.markdown("**📦 Input data retur baru (belum ada di CSV):**")
                            st.info("💡 Data ini akan disimpan sementara dan di-export bersama data lainnya dengan flag 'RETUR BARU'")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                new_order_id = st.text_input(
                                    "ID Order (cek di marketplace)",
                                    key=f"new_order_{barcode}",
                                    placeholder="260105NEWORDER"
                                )
                                new_sku = st.text_input(
                                    "SKU Produk",
                                    key=f"new_sku_{barcode}",
                                    placeholder="SKU123"
                                )
                            with col2:
                                new_resi = st.text_input(
                                    "No. Resi (jika ada)",
                                    key=f"new_resi_{barcode}",
                                    placeholder="SPXID..."
                                )
                                new_qty = st.number_input(
                                    "Qty Retur",
                                    min_value=1,
                                    value=1,
                                    key=f"new_qty_{barcode}"
                                )
                            
                            new_product = st.text_input(
                                "Nama Produk",
                                key=f"new_product_{barcode}",
                                placeholder="Nama produk yang diretur"
                            )
                            
                            new_note = st.text_area(
                                "Catatan",
                                key=f"new_note_{barcode}",
                                placeholder="Contoh: Data belum update di Shopee, paket sudah datang duluan",
                                height=80
                            )
                            
                            if st.button("💾 Simpan Retur Baru", key=f"btn_new_{barcode}", type="primary"):
                                if new_order_id.strip() and new_product.strip():
                                    # Create new return entry
                                    new_return = {
                                        'No. Pesanan': new_order_id.strip(),
                                        'Status Pesanan': 'Retur (Data Baru)',
                                        'Alasan Pembatalan': '',
                                        'Status Pembatalan/ Pengembalian': 'Retur - Belum di CSV',
                                        'No. Resi': new_resi.strip() if new_resi.strip() else barcode,
                                        'Nomor Referensi SKU': new_sku.strip(),
                                        'Nama Produk': new_product.strip(),
                                        'Nama Variasi': '',
                                        'Jumlah': new_qty,
                                        'Returned quantity': new_qty,
                                        'Barcode di Paket': barcode,
                                        'Tanggal': datetime.now().strftime("%Y-%m-%d"),
                                        'Batch': '',
                                        'Ket Product': 'OK',
                                        'Stock In': 'Retur Central',
                                        'Catatan Mismatch': f"⚠️ RETUR BARU - Belum ada di CSV. {new_note.strip()}",
                                        'Flag': '🆕 RETUR BARU',
                                        'is_new_return': True
                                    }
                                    
                                    # Add to new returns list
                                    st.session_state.new_returns.append(new_return)
                                    
                                    # Add to scan history
                                    st.session_state.scan_history.insert(0, {
                                        'barcode': f"{barcode} (RETUR BARU)",
                                        'time': datetime.now().strftime("%H:%M:%S"),
                                        'results': pd.DataFrame([new_return]),
                                        'status': 'new_return'
                                    })
                                    
                                    # Update search results
                                    all_results = []
                                    for scan in st.session_state.scan_history:
                                        if scan['status'] in ['success', 'manual_link', 'new_return'] and scan['results'] is not None:
                                            all_results.append(scan['results'])
                                    
                                    if all_results:
                                        st.session_state.search_results = pd.concat(all_results, ignore_index=True).drop_duplicates()
                                    
                                    st.success(f"✅ Retur baru berhasil disimpan: {new_order_id.strip()}")
                                    st.info("💡 Data akan di-export dengan flag 'RETUR BARU'. Jangan lupa update CSV dan re-check nanti!")
                                    st.rerun()
                                else:
                                    st.error("❌ ID Order dan Nama Produk wajib diisi!")
            
            # Clear input for next scan
            st.session_state.scanner_input_field = ""
            st.rerun()
        
        # Show scan history
        if len(st.session_state.scan_history) > 0:
            st.markdown("### 📜 History Scan")
            for idx, scan in enumerate(st.session_state.scan_history[:10]):  # Show last 10 scans
                if scan['status'] == 'success':
                    count = len(scan['results']) if scan['results'] is not None else 0
                    st.success(f"✅ [{scan['time']}] {scan['barcode']} - {count} item")
                elif scan['status'] == 'manual_link':
                    count = len(scan['results']) if scan['results'] is not None else 0
                    st.info(f"🔗 [{scan['time']}] {scan['barcode']} (Manual Link) - {count} item")
                elif scan['status'] == 'new_return':
                    count = len(scan['results']) if scan['results'] is not None else 0
                    st.warning(f"🆕 [{scan['time']}] {scan['barcode']} (RETUR BARU) - {count} item")
                else:
                    st.error(f"❌ [{scan['time']}] {scan['barcode']} - Tidak ditemukan")
    
    # Manual Input Mode
    else:
        st.markdown("""
        Paste **No. Pesanan** atau **No. Resi** di bawah ini (satu per baris):
        """)
        
        search_text = st.text_area(
            "Input pencarian",
            height=150,
            placeholder="Contoh:\n260101U95E5RBQ\nSPXID067190313141\n260109JVE371VN",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            search_button = st.button("🔍 Cari", use_container_width=True, type="primary")
        
        # Perform search
        if search_button and search_text.strip():
            with st.spinner("Mencari data..."):
                results = search_orders(df, search_text)
                st.session_state.search_results = results
                
                if len(results) > 0:
                    summary = get_search_summary(results)
                    st.success(f"✅ Ditemukan {summary['total_items']} item dari {summary['unique_orders']} pesanan")
                    
                    # Show alerts if any
                    if summary['partial_returns'] > 0:
                        st.warning(f"⚠️ {summary['partial_returns']} item dengan partial return")
                    if summary['no_resi_empty'] > 0:
                        st.warning(f"⚠️ {summary['no_resi_empty']} item tanpa no resi")
                else:
                    st.error("❌ Tidak ada data yang ditemukan")
                    st.session_state.search_results = None
    
    # Display search results with input form
    if st.session_state.search_results is not None and len(st.session_state.search_results) > 0:
        st.markdown("---")
        
        # Show summary with new returns count
        total_items = len(st.session_state.search_results)
        new_returns_count = len([r for r in st.session_state.search_results.to_dict('records') if r.get('is_new_return', False)])
        
        if new_returns_count > 0:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f"📋 Hasil Pencarian ({total_items} items)")
            with col2:
                st.warning(f"🆕 {new_returns_count} RETUR BARU (belum di CSV)")
        else:
            st.subheader(f"📋 Hasil Pencarian ({total_items} items)")
        
        results_df = st.session_state.search_results.copy()
        
        # OPTIMIZATION: Vectorized operations instead of apply (much faster)
        # Add combined product column
        results_df['Produk + Variasi'] = results_df['Nama Produk'].astype(str) + ' - ' + results_df['Nama Variasi'].astype(str)
        results_df['Produk + Variasi'] = results_df['Produk + Variasi'].str.replace(' - $', '', regex=True)  # Remove trailing ' - ' if variant empty
        
        # Add alerts column (vectorized)
        alerts = []
        for _, row in results_df.iterrows():
            row_alerts = []
            if row['Jumlah'] > 0 and row['Returned quantity'] > 0:
                if row['Returned quantity'] < row['Jumlah']:
                    row_alerts.append('⚠️ Partial Return')
            if not row['No. Resi'] or str(row['No. Resi']).strip() == '':
                row_alerts.append('⚠️ No Resi Kosong')
            alerts.append(' '.join(row_alerts))
        results_df['Alert'] = alerts
        
        # Initialize input data for new searches
        today = datetime.now().strftime("%Y-%m-%d")
        for idx in results_df.index:
            if idx not in st.session_state.input_data:
                # Get scanned barcode if available (from scanner mode)
                scanned_barcode = ""
                if hasattr(st.session_state, 'scan_history') and len(st.session_state.scan_history) > 0:
                    # Get most recent scan that found this order
                    for scan in st.session_state.scan_history:
                        if scan['status'] == 'success' and scan['results'] is not None:
                            if idx in scan['results'].index:
                                scanned_barcode = scan['barcode']
                                break
                
                st.session_state.input_data[idx] = {
                    'Tanggal': today,
                    'Batch': '',
                    'Barcode di Paket': scanned_barcode,
                    'Ket Product': 'OK',
                    'Stock In': 'Retur Central',
                    'Catatan Mismatch': ''
                }
        
        # Display results with input forms
        display_columns = [
            'No. Pesanan', 'Status Pesanan', 'No. Resi',
            'Nomor Referensi SKU', 'Produk + Variasi',
            'Jumlah', 'Returned quantity', 'Alert'
        ]
        
        # Show summary table first
        st.dataframe(
            results_df[display_columns],
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("---")
        st.subheader("📝 Input Data Tambahan")
        st.markdown("Isi form di bawah untuk setiap item:")
        
        # Create expandable forms for each item
        for idx, row in results_df.iterrows():
            # Check if this is a new return
            is_new_return = row.get('is_new_return', False)
            
            # Check for mismatch
            barcode_in_data = st.session_state.input_data[idx].get('Barcode di Paket', '')
            has_mismatch = False
            mismatch_msg = ""
            
            if barcode_in_data and not is_new_return:
                # Check if scanned barcode matches order number or resi
                if (barcode_in_data != str(row['No. Pesanan']) and 
                    barcode_in_data != str(row['No. Resi'])):
                    has_mismatch = True
                    mismatch_msg = f"⚠️ Barcode scan ({barcode_in_data}) TIDAK MATCH dengan ID Order ({row['No. Pesanan']}) atau No. Resi ({row['No. Resi']})"
            
            # Build expander title
            expander_title = f"📦 {row['No. Pesanan']} - {row['Nomor Referensi SKU']} - {row['Produk + Variasi'][:50]}"
            if is_new_return:
                expander_title = f"🆕 RETUR BARU - " + expander_title
            elif has_mismatch:
                expander_title = f"⚠️ MISMATCH! - " + expander_title
            
            with st.expander(expander_title, expanded=(has_mismatch or is_new_return)):
                # Show new return warning
                if is_new_return:
                    st.error("🆕 **RETUR BARU** - Data ini belum ada di CSV Shopee")
                    st.warning("⚠️ **ACTION REQUIRED:** Update CSV Shopee dan re-check data ini nanti!")
                    st.info(f"💡 Catatan: {row.get('Catatan Mismatch', 'Data belum ter-update di marketplace')}")
                    st.markdown("---")
                
                # Show mismatch warning prominently
                elif has_mismatch:
                    st.error(mismatch_msg)
                    st.warning("⚠️ **PERHATIAN:** Barcode yang di-scan berbeda dengan data di sistem. Periksa kembali paket!")
                
                # Barcode info section
                st.markdown("**📷 Info Barcode:**")
                barcode_col1, barcode_col2, barcode_col3 = st.columns(3)
                with barcode_col1:
                    st.info(f"**Di Sistem:**\n- ID Order: `{row['No. Pesanan']}`\n- No. Resi: `{row['No. Resi']}`")
                with barcode_col2:
                    barcode_paket = st.text_input(
                        "Barcode Aktual di Paket",
                        value=st.session_state.input_data[idx].get('Barcode di Paket', ''),
                        key=f"barcode_{idx}",
                        help="Isi jika barcode di paket berbeda dengan ID Order/Resi di sistem"
                    )
                    st.session_state.input_data[idx]['Barcode di Paket'] = barcode_paket
                with barcode_col3:
                    if has_mismatch:
                        st.warning("❌ **TIDAK MATCH!**")
                        # Auto-suggest to add note
                        if not st.session_state.input_data[idx].get('Catatan Mismatch', ''):
                            st.session_state.input_data[idx]['Catatan Mismatch'] = f"Barcode paket: {barcode_in_data}, Data sistem: {row['No. Pesanan']}"
                    elif barcode_paket:
                        st.success("✅ Match!")
                
                st.markdown("---")
                st.markdown("**📝 Input Data:**")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    tanggal = st.date_input(
                        "Tanggal",
                        value=datetime.strptime(st.session_state.input_data[idx]['Tanggal'], "%Y-%m-%d"),
                        key=f"tanggal_{idx}"
                    )
                    st.session_state.input_data[idx]['Tanggal'] = tanggal.strftime("%Y-%m-%d")
                
                with col2:
                    batch = st.text_input(
                        "Batch",
                        value=st.session_state.input_data[idx]['Batch'],
                        key=f"batch_{idx}"
                    )
                    st.session_state.input_data[idx]['Batch'] = batch
                
                with col3:
                    ket_product = st.selectbox(
                        "Ket Product",
                        options=KET_PRODUCT_OPTIONS,
                        index=KET_PRODUCT_OPTIONS.index(st.session_state.input_data[idx]['Ket Product']),
                        key=f"ket_{idx}"
                    )
                    st.session_state.input_data[idx]['Ket Product'] = ket_product
                
                with col4:
                    stock_in = st.selectbox(
                        "Stock In",
                        options=STOCK_IN_OPTIONS,
                        index=STOCK_IN_OPTIONS.index(st.session_state.input_data[idx]['Stock In']),
                        key=f"stock_{idx}"
                    )
                    st.session_state.input_data[idx]['Stock In'] = stock_in
                
                # Catatan Mismatch (if any)
                if has_mismatch or st.session_state.input_data[idx].get('Catatan Mismatch', ''):
                    st.markdown("---")
                    st.markdown("**📝 Catatan Mismatch:**")
                    catatan_mismatch = st.text_area(
                        "Catatan tentang perbedaan barcode",
                        value=st.session_state.input_data[idx].get('Catatan Mismatch', ''),
                        key=f"catatan_{idx}",
                        help="Jelaskan kenapa barcode berbeda, atau catat informasi penting lainnya",
                        height=80
                    )
                    st.session_state.input_data[idx]['Catatan Mismatch'] = catatan_mismatch
                
                # Show row details
                st.markdown("---")
                st.markdown("**📋 Detail Item:**")
                st.markdown("**Detail Item:**")
                detail_col1, detail_col2 = st.columns(2)
                with detail_col1:
                    st.text(f"Status: {row['Status Pesanan']}")
                    st.text(f"Status Pembatalan: {row['Status Pembatalan/ Pengembalian']}")
                with detail_col2:
                    st.text(f"Qty Order: {row['Jumlah']}")
                    st.text(f"Qty Retur: {row['Returned quantity']}")
                    if row['Alert']:
                        st.warning(row['Alert'])


def show_export():
    """Display export interface."""
    st.header("📥 Export ke Excel")
    
    if st.session_state.search_results is not None and len(st.session_state.search_results) > 0:
        results_df = st.session_state.search_results.copy()
        
        # Add input data to results
        for idx in results_df.index:
            if idx in st.session_state.input_data:
                for col in ADDITIONAL_COLUMNS:
                    results_df.loc[idx, col] = st.session_state.input_data[idx].get(col, '')
        
        # Add combined product column
        results_df['Produk + Variasi'] = results_df.apply(combine_product_variant, axis=1)
        
        # Prepare export columns
        export_columns = [
            'No. Pesanan', 'Status Pesanan', 'Alasan Pembatalan',
            'Status Pembatalan/ Pengembalian', 'No. Resi',
            'Nomor Referensi SKU', 'Produk + Variasi',
            'Jumlah', 'Returned quantity'
        ] + ADDITIONAL_COLUMNS
        
        export_df = results_df[export_columns]
        
        # Preview
        st.subheader("👀 Preview Data Export")
        st.dataframe(export_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Export button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            filename = generate_filename()
            excel_data = export_to_excel(export_df)
            
            st.download_button(
                label="📥 Download Excel",
                data=excel_data,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
                type="primary"
            )
        
        st.success(f"✅ File akan didownload dengan nama: **{filename}**")
        st.info(f"📊 Total baris: {len(export_df)}")
        
    else:
        st.info("👈 Lakukan pencarian terlebih dahulu di tab 'Search & Input' untuk export data")


if __name__ == "__main__":
    main()
