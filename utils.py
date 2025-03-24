import requests
from bs4 import BeautifulSoup

NEWS_API_KEY = "59f8653cb6cb4b708a176c0b9bcf0ecd"  # you can change your api key

def fetch_news(company_name):
    """Fetches latest news articles about the given company from NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={company_name}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()

    articles = []
    if "articles" in response:
        for item in response["articles"][:10]:
            articles.append({
                "title": item["title"],
                "content": item["description"] or "No summary available",
                "link": item["url"]
            })

    return articles
