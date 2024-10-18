import pandas as pd
import json

def preprocess_data():
    # Read the product Excel file
    products_df = pd.read_excel('data/products.xlsx')
    competitors_df = pd.read_excel('data/competitors.xlsx')

    # Convert DataFrames to dictionary format
    reference_data = {
        "products": products_df.to_dict(orient='records'),
        "competitors": competitors_df.to_dict(orient='records')
    }

    # Save to JSON file
    with open('json_data/reference_data.json', 'w') as json_file:
        json.dump(reference_data, json_file, indent=4)

if __name__ == '__main__':
    preprocess_data()
