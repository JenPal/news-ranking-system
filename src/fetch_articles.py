# fetch_articles.py

import feedparser
from newsapi import NewsApiClient

# Set up News API
news_api_key = os.getenv("NEWS_API_KEY")

# RSS Feed URLs
rss_urls = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    "https://www.reuters.com/rssfeeds/technology/",
    "https://www.theguardian.com/world/rss",
    "https://www.cnbc.com/id/10000664/device/rss/rss.html"
]

def get_rss_articles(rss_urls, max_articles=10):
    articles = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_articles]:
            articles.append({"title": entry.title, "summary": entry.summary, "link": entry.link})  # Added link
    return articles

def get_newsapi_articles(max_articles=10):
    top_headlines = newsapi.get_top_headlines(language='en', page_size=max_articles)
    return [{"title": a["title"], "description": a["description"], "link": a["url"]} for a in top_headlines["articles"]]  # Added link
