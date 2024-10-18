import openai
import json
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_product_description(product_info):
    prompt = f"Write an SEO-ready product description for {product_info['name']}..."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=5500
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    # Load reference data
    with open('json_data/reference_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Generate description for the first product
    product_desc = generate_product_description(data['products'][0])
    print(product_desc)
