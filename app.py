# app.py
from flask import Flask, render_template, request
import os
import sys

# Ensure scraping folder is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scraping')))


from scraping.custom_scraper import custom_web_scraper
from langgraph_flow import build_graph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        scraped_data = custom_web_scraper(url)
        if not scraped_data:
            return render_template("result.html", answer="❌ Failed to scrape the website.")

        content = " ".join(scraped_data['text'])[:8000]  # Limiting characters

        graph = build_graph()

        result = graph.invoke({
            "input": content
        })

        return render_template("result.html", answer=result['final_answer'])

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
