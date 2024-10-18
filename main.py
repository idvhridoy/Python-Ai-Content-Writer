import openai
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Configuration
openai.api_key = OPENAI_API_KEY

# Paths to your datasets
product_data_path = 'G:\My Drive\Google AI Studio\Python-Ai-Content-Writer\products.xlsx'
competitor_data_path = 'path/to/your/competitor_data.xlsx'

# Load datasets
def load_data(file_path):
    return pd.read_excel(file_path)

# Load your product and competitor data
product_data = load_data(product_data_path)
competitor_data = load_data(competitor_data_path)

# Function to search web for additional info on a product
def search_product_info(product_name):
    search_url = f"https://www.google.com/search?q={product_name}+skincare+details"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting basic information from search results
    info_snippets = [p.text for p in soup.find_all('p')][:3]
    return ' '.join(info_snippets)

# Generate content using OpenAI
def generate_content(prompt, max_tokens=300):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=1,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Create structured content for product descriptions
def create_product_description(product):
    product_name = product['Product Name']
    product_info = product['Description']
    
    # Optional: Search for additional information online
    additional_info = search_product_info(product_name)
    
    # Create a prompt for OpenAI to generate a structured description
    prompt = f"""
    Write an SEO-optimized, structured product description for the following skincare product:
    Product Name: {product_name}
    Product Details: {product_info}
    Additional Information: {additional_info}
    Please include key ingredients, usage, benefits, caution, and target audience.
    """
    return generate_content(prompt)

# Generate content for blogs, FAQs, help articles, etc.
def generate_other_content(content_type, topic):
    prompt = f"Write an {content_type} about {topic} for a skincare e-commerce website. Make it informative, SEO-friendly, and well-structured."
    return generate_content(prompt)

# Main function to process all products and generate content
def generate_all_content():
    for _, product in product_data.iterrows():
        description = create_product_description(product)
        print(f"Product: {product['Product Name']}\nDescription:\n{description}\n")
        
        # Save or process the generated description as needed (e.g., save to a file or database)

# Sample generation for other content types
def generate_sample_blog():
    topic = "Benefits of Using Centella Asiatica in Skincare"
    blog_content = generate_other_content("blog article", topic)
    print(f"Blog on {topic}:\n{blog_content}")

# Run the content generation
generate_all_content()
generate_sample_blog()
