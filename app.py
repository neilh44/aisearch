import requests
from bs4 import BeautifulSoup
import faiss
import streamlit as st

# Function to crawl a website and extract its content
def crawl_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text content from the website
        text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
        return text_content
    except Exception as e:
        print("Error crawling website:", e)
        return None

# Function to index content and save it in a Faiss database
def index_content(url, text_content, index):
    if text_content:
        # Transform text content into vector representation
        # (This is just a placeholder, you might need to use a proper vectorization method)
        vector = text_content.encode('utf-8')
        index.add(np.array([vector]))

# Function to generate response for user query
def generate_response(query, index, vectors):
    # Transform query into vector representation
    query_vector = query.encode('utf-8')
    # Search for the most similar vector in the Faiss index
    distances, indices = index.search(np.array([query_vector]), k=1)
    # Get the most similar document's URL
    most_similar_index = indices[0][0]
    most_similar_url = vectors[most_similar_index]
    return most_similar_url

# Streamlit app
def main():
    st.title("Website Search Engine")
    
    # Input URL
    website_url = st.text_input("Enter website URL:", "https://example.com")
    
    # Crawl website
    website_content = crawl_website(website_url)
    
    # Index content
    index = faiss.IndexFlatL2(100)  # You might need to adjust the dimensionality
    vectors = []
    index_content(website_url, website_content, index)
    vectors.append(website_url)
    
    # Example query
    query = st.text_input("Enter your query:")
    
    # Generate response
    if st.button("Search"):
        response_url = generate_response(query, index, vectors)
        st.write("The website that best matches the query is:", response_url)

if __name__ == "__main__":
    main()
