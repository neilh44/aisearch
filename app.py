import streamlit as st
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text content from HTML
            text = " ".join([p.text for p in soup.find_all('p')])
            return text
        else:
            return None
    except Exception as e:
        return None

# Function to perform semantic search
def semantic_search(query, indexed_data):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(indexed_data.values())
    query_vec = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    document_scores = [(score, url) for url, score in zip(indexed_data.keys(), cosine_similarities)]
    document_scores.sort(reverse=True)
    return document_scores

def main():
    st.title("Semantic Web Search")

    # Input query
    query = st.text_input("Enter your query:")

    if st.button("Search"):
        if query:
            # Perform semantic search
            search_results = semantic_search(query, indexed_data)
            st.subheader("Search Results:")
            for score, url in search_results:
                st.write(f"- {url} (Score: {score:.2f})")

if __name__ == "__main__":
    main()
