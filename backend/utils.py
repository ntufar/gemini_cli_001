import requests
from bs4 import BeautifulSoup

def fetch_url_content(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text from common elements, you might want to refine this
        text_content = ' '.join(p.get_text() for p in soup.find_all('p'))
        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
