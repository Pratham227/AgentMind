# custom_scraper.py

import requests
from bs4 import BeautifulSoup

def custom_web_scraper(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all paragraphs
        paragraphs = [p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip()]
        # Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return {
            "text": paragraphs,
            "links": links
        }

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    data = custom_web_scraper("https://en.wikipedia.org/wiki/Artificial_intelligence")
    print("Sample Text:", data["text"][:3])
    print("Links:", data["links"][:5])
