import pandas as pd
import json

def load_data():
    # Load product data from Excel
    products_df = pd.read_excel('data/products.xlsx')
    
    # Load reference data from JSON
    with open('json_data/reference_data.json', 'r') as f:
        reference_data = json.load(f)
    
    return products_df, reference_data

def preprocess_data(products_df, reference_data):
    # Example preprocessing: converting prices to float
    products_df['purchase_price'] = products_df['purchase_price'].astype(float)
    products_df['sale_price'] = products_df['sale_price'].astype(float)
    
    # Extract necessary reference information
    category_keywords = reference_data.get('categories', {})
    competitor_brands = reference_data.get('competitor_brands', [])
    
    # Return preprocessed data
    return products_df, category_keywords, competitor_brands
