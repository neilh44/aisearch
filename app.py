import streamlit as st
from transformers import pipeline

# Load pre-trained language model
model_name = "bert-base-uncased"
search_pipeline = pipeline("search", model=model_name)

# Sample documents
documents = [
    "The cat sat on the mat.",
    "The dog jumped over the fence.",
    "The quick brown fox.",
    "The lazy dog slept on the couch."
]

# Streamlit app
st.title("AI Search Engine")

# Search query input
query = st.text_input("Enter your search query:")

if query:
    # Perform search
    results = search_pipeline(query, documents)

    # Display search results
    st.subheader("Search Results:")
    if results:
        for i, result in enumerate(results, start=1):
            st.write(f"{i}. {result['text']}")
    else:
        st.write("No results found.")
