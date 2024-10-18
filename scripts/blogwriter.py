import openai

def generate_blog(product_name, product_data, topic, category_keywords):
    # Create a prompt for the OpenAI API to generate a blog article
    prompt = f"Write a comprehensive and SEO-ready blog article about {topic}. The blog should " \
             f"highlight the benefits of using the skincare product called '{product_name}', which is in " \
             f"the {product_data['category']} category. The ingredients include {product_data['ingredients']}. " \
             f"Discuss the use case, potential benefits, and why it stands out among other products. " \
             f"Make sure to include relevant keywords such as {', '.join(category_keywords)} " \
             f"and address common skincare concerns."

    # Generate blog content using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()
