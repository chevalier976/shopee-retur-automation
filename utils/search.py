"""Search module for finding orders and tracking numbers."""
import pandas as pd
from typing import List


def search_orders(df: pd.DataFrame, search_terms: str) -> pd.DataFrame:
    """
    Search for orders by order number or tracking number.
    Optimized for speed with exact match first, then partial match.
    
    Args:
        df: DataFrame containing Shopee data
        search_terms: String with search terms (one per line)
        
    Returns:
        pd.DataFrame: Filtered dataframe with matching results
    """
    if not search_terms or search_terms.strip() == '':
        return pd.DataFrame()
    
    # Split search terms by newline and clean them
    terms = [term.strip() for term in search_terms.strip().split('\n') if term.strip()]
    
    if not terms:
        return pd.DataFrame()
    
    # OPTIMIZATION: Data is already stripped during parse, use directly
    df_pesanan = df['No. Pesanan']
    df_resi = df['No. Resi']
    
    # Collect all matching indices
    all_indices = set()
    
    for term in terms:
        term_clean = term.strip()
        
        # OPTIMIZATION 1: Try exact match first (fastest - uses index)
        exact_match_pesanan = df_pesanan == term_clean
        exact_match_resi = df_resi == term_clean
        
        if exact_match_pesanan.any() or exact_match_resi.any():
            # Found exact match, use it
            indices = df[exact_match_pesanan | exact_match_resi].index
            all_indices.update(indices)
        else:
            # OPTIMIZATION 2: Only do partial match if exact match fails
            # Use case-insensitive contains only when needed
            term_lower = term_clean.lower()
            
            # Use str accessor only once
            partial_match = (df_pesanan.str.lower().str.contains(term_lower, na=False) | 
                           df_resi.str.lower().str.contains(term_lower, na=False))
            
            if partial_match.any():
                indices = df[partial_match].index
                all_indices.update(indices)
    
    # Return results using indices (faster than boolean mask)
    if all_indices:
        return df.loc[list(all_indices)].copy()
    else:
        return pd.DataFrame()


def get_search_summary(df: pd.DataFrame) -> dict:
    """
    Get summary statistics for search results.
    
    Args:
        df: Filtered dataframe from search
        
    Returns:
        dict: Summary statistics
    """
    summary = {
        'total_items': len(df),
        'unique_orders': df['No. Pesanan'].nunique() if len(df) > 0 else 0,
        'partial_returns': 0,
        'no_resi_empty': 0
    }
    
    if len(df) > 0:
        # Count partial returns (Returned quantity < Jumlah and both > 0)
        summary['partial_returns'] = len(df[(df['Returned quantity'] < df['Jumlah']) & 
                                             (df['Returned quantity'] > 0) & 
                                             (df['Jumlah'] > 0)])
        
        # Count empty tracking numbers
        summary['no_resi_empty'] = len(df[df['No. Resi'].astype(str).str.strip() == ''])
    
    return summary


def highlight_alerts(row: pd.Series) -> List[str]:
    """
    Generate alert flags for a row.
    
    Args:
        row: DataFrame row
        
    Returns:
        List[str]: List of alert messages
    """
    alerts = []
    
    # Check for partial return
    if row['Jumlah'] > 0 and row['Returned quantity'] > 0:
        if row['Returned quantity'] < row['Jumlah']:
            alerts.append('⚠️ Partial Return')
    
    # Check for empty tracking number
    if not row['No. Resi'] or str(row['No. Resi']).strip() == '':
        alerts.append('⚠️ No Resi Kosong')
    
    return alerts


def combine_product_variant(row: pd.Series) -> str:
    """
    Combine product name and variant into single string.
    
    Args:
        row: DataFrame row
        
    Returns:
        str: Combined product + variant name
    """
    product = str(row.get('Nama Produk', ''))
    variant = str(row.get('Nama Variasi', ''))
    
    if variant and variant != 'nan' and variant.strip():
        return f"{product} - {variant}"
    return product
