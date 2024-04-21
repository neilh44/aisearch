import streamlit as st
from transformers import pipeline

# Load pre-trained language model for encoding
model_name = "bert-base-uncased"
encode_pipeline = pipeline("feature-extraction", model=model_name)

# Load website content vectors from database
website_content_vectors = load_website_content_vectors()

# Streamlit app
st.title("Semantic Search Engine")

# Search query input
query = st.text_input("Enter your search query:")

if query:
    # Encode query into vector
    query_vector = encode_pipeline(query)

    # Perform semantic search
    search_results = semantic_search(query_vector, website_content_vectors)

    # Display search results
    st.subheader("Search Results:")
    if search_results:
        for result in search_results:
            st.write(result)
    else:
        st.write("No results found.")
