import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

# Function to index content and save it in a vector database
def index_content(url, text_content, vector_db):
    if text_content:
        vector_db[url] = text_content

# Function to generate response for user query
def generate_response(query, vector_db):
    # Transform query into vector representation
    query_vector = vectorizer.transform([query])
    # Calculate cosine similarity between query vector and document vectors
    similarities = cosine_similarity(query_vector, vector_db.values())
    # Get the most similar document's URL
    most_similar_index = similarities.argmax()
    most_similar_url = list(vector_db.keys())[most_similar_index]
    return most_similar_url

# Main function
def main():
    # Initialize vector database
    vector_db = defaultdict(str)
    
    # Crawl website
    website_url = 'https://example.com'  # Change this to the website you want to crawl
    website_content = crawl_website(website_url)
    
    # Index content
    index_content(website_url, website_content, vector_db)
    
    # Vectorize content
    global vectorizer
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(vector_db.values())
    
    # Example query
    query = "What is the website about?"
    
    # Generate response
    response_url = generate_response(query, vectors, vector_db)
    print("The website that best matches the query is:", response_url)

if __name__ == "__main__":
    main()
