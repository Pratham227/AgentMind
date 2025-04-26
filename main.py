# main.py

from scraping.custom_scraper import custom_web_scraper
from langgraph_flow import build_graph

def main():
    url = input("Enter a URL to research: ")
    data = custom_web_scraper(url)

    if not data:
        print("Failed to scrape website.")
        return

    text_data = " ".join(data['text'])[:8000]  # limit token usage

    graph = build_graph()
    result = graph.invoke(text_data)
    
    print("\n🔍 Final Answer:\n")
    print(result)

if __name__ == "__main__":
    main()
