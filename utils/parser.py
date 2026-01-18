"""CSV/Excel parser module for Shopee return data."""
import pandas as pd
from typing import BinaryIO
import io


def parse_shopee_file(file: BinaryIO, filename: str) -> pd.DataFrame:
    """
    Parse Shopee CSV or Excel file and return a cleaned DataFrame.
    
    Args:
        file: Uploaded file object from Streamlit
        filename: Name of the uploaded file
        
    Returns:
        pd.DataFrame: Cleaned dataframe with Shopee return data
        
    Raises:
        ValueError: If file format is invalid or required columns are missing
    """
    try:
        # Check file extension
        file_ext = filename.lower().split('.')[-1]
        
        if file_ext in ['xlsx', 'xls']:
            # Read Excel file
            df = pd.read_excel(file, engine='openpyxl' if file_ext == 'xlsx' else None)
        elif file_ext == 'csv':
            # Try reading with UTF-8 encoding first
            try:
                df = pd.read_csv(file, encoding='utf-8')
            except UnicodeDecodeError:
                # Try UTF-8-BOM if UTF-8 fails
                file.seek(0)
                df = pd.read_csv(file, encoding='utf-8-sig')
        else:
            raise ValueError(f"Format file tidak didukung: {file_ext}. Gunakan CSV atau Excel (.xlsx)")
        
        # Clean column names (strip whitespace)
        df.columns = df.columns.str.strip()
        
        # Validate required columns exist
        from config.settings import SHOPEE_COLUMNS
        missing_columns = [col for col in SHOPEE_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Kolom yang hilang: {', '.join(missing_columns)}")
        
        # OPTIMIZATION: Convert and fill in one operation (faster)
        df['Jumlah'] = pd.to_numeric(df['Jumlah'], errors='coerce').fillna(0).astype(int)
        df['Returned quantity'] = pd.to_numeric(df['Returned quantity'], errors='coerce').fillna(0).astype(int)
        
        # OPTIMIZATION: Vectorized fillna for all string columns at once
        string_columns = ['No. Pesanan', 'Status Pesanan', 'Alasan Pembatalan', 
                         'Status Pembatalan/ Pengembalian', 'No. Resi', 
                         'Nomor Referensi SKU', 'Nama Produk', 'Nama Variasi']
        df[string_columns] = df[string_columns].fillna('')
        
        # OPTIMIZATION: Pre-process for faster searching
        # Strip whitespace from search columns once during load
        df['No. Pesanan'] = df['No. Pesanan'].astype(str).str.strip()
        df['No. Resi'] = df['No. Resi'].astype(str).str.strip()
        
        return df
        
    except Exception as e:
        raise ValueError(f"Error parsing file: {str(e)}")


def parse_shopee_csv(file: BinaryIO) -> pd.DataFrame:
    """
    Parse Shopee CSV file (backward compatibility).
    
    Args:
        file: Uploaded file object from Streamlit
        
    Returns:
        pd.DataFrame: Cleaned dataframe with Shopee return data
    """
    # For backward compatibility, assume CSV
    return parse_shopee_file(file, "file.csv")


def get_dataframe_info(df: pd.DataFrame) -> dict:
    """
    Get summary information about the dataframe.
    
    Args:
        df: DataFrame to analyze
        
    Returns:
        dict: Dictionary with summary statistics
    """
    info = {
        'total_rows': len(df),
        'total_orders': df['No. Pesanan'].nunique(),
        'date_range': None
    }
    
    return info
