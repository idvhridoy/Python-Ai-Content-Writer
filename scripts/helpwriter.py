import openai

def generate_help_article(product_name, product_data, topic):
    # Create a prompt for the OpenAI API to generate a help article
    prompt = f"Write a detailed help article or guide on {topic} for the skincare product '{product_name}'. " \
             f"The product belongs to the {product_data['category']} category and contains ingredients such as " \
             f"{product_data['ingredients']}. The guide should include how to use the product, any precautions, " \
             f"troubleshooting tips, and recommended routines for best results."

    # Generate help article content using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=750,
        temperature=0.7
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()
