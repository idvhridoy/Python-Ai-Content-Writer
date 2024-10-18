import openai

def generate_description(product_name, product_data, category_keywords, competitor_brands):
    # Create a prompt for the OpenAI API
    prompt = f"Write an SEO-ready product description for a skincare product called '{product_name}'. " \
             f"The product details are as follows:\n" \
             f"Category: {product_data['category']}\n" \
             f"Purchase Price: {product_data['purchase_price']}\n" \
             f"Sale Price: {product_data['sale_price']}\n" \
             f"Ingredients: {product_data['ingredients']}\n" \
             f"Use Case: {product_data['use_case']}\n" \
             f"Caution: {product_data['caution']}\n" \
             f"Competitor Brands: {', '.join(competitor_brands)}\n" \
             f"Relevant Keywords: {', '.join(category_keywords)}\n\n" \
             f"Please include a short description, key features, ingredients list, use cases, cautions, " \
             f"detailed information, and FAQs about the product."

    # Generate description using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()
