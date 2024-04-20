import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text content from HTML
            text = " ".join([p.text for p in soup.find_all('p')])
            return text
        else:
            st.error(f"Failed to fetch website content. Error code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching website content: {str(e)}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        return None

def main():
    st.title("Website Content Crawler & Indexer")

    # Input URL
    url = st.text_input("Enter website URL:")

    if st.button("Crawl and Index"):
        if url:
            st.info("Crawling and indexing in progress...")
            text = scrape_website(url)
            if text:
                st.subheader("Website Content:")
                st.write(text)
            else:
                st.error("Failed to crawl and index the website.")

if __name__ == "__main__":
    main()
