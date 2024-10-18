import openai

def generate_faq(product_name, product_data, common_questions):
    # Create a prompt for the OpenAI API to generate FAQs
    prompt = f"Write a set of frequently asked questions (FAQs) with detailed answers about the skincare product " \
             f"'{product_name}'. The product belongs to the {product_data['category']} category and contains " \
             f"the following ingredients: {product_data['ingredients']}. Make sure to address the most common " \
             f"questions like:\n" \
             f"{', '.join(common_questions)}\n" \
             f"Provide clear and informative answers."

    # Generate FAQs using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=750,
        temperature=0.7
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()
