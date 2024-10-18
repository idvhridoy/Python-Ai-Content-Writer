import openai
import config
from preprocess_data import load_data, preprocess_data
from scripts import productdescriptionwriter, blogwriter, faqwriter, helpwriter

def setup_openai():
    openai.api_key = config.OPENAI_API_KEY

def main():
    # Set up OpenAI API
    setup_openai()
    
    # Load and preprocess data
    products_df, reference_data = load_data()
    products_df, category_keywords, competitor_brands = preprocess_data(products_df, reference_data)

    # Example usage for generating different content types
    for _, row in products_df.iterrows():
        product_name = row['product_name']
        
        # Generate a product description
        description = productdescriptionwriter.generate_description(
            product_name, row, category_keywords, competitor_brands
        )
        
        # Generate a blog article
        blog = blogwriter.generate_blog(
            product_name, row, f"Benefits of Using {product_name}", category_keywords
        )
        
        # Generate FAQs
        faqs = faqwriter.generate_faq(
            product_name, row, ["What are the benefits?", "Is it safe for sensitive skin?", "How often should I use it?"]
        )
        
        # Generate a help article
        help_article = helpwriter.generate_help_article(
            product_name, row, f"How to Use {product_name}"
        )
        
        # Display or save the results as needed
        print(f"Description for {product_name}:\n{description}\n")
        print(f"Blog for {product_name}:\n{blog}\n")
        print(f"FAQs for {product_name}:\n{faqs}\n")
        print(f"Help Article for {product_name}:\n{help_article}\n")

if __name__ == "__main__":
    main()
