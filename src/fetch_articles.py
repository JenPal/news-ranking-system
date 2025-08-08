# fetch_articles.py

import os
import feedparser
from newsapi import NewsApiClient

# Set up News API using the API key from the environment variables
news_api_key = os.getenv("NEWS_API_KEY")

# Ensure the API key is loaded correctly
if not news_api_key:
    raise ValueError("NEWS_API_KEY environment variable not set")

newsapi = NewsApiClient(api_key=news_api_key)

# RSS Feed URLs
rss_urls = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    "https://www.reuters.com/rssfeeds/technology/",
    "https://www.theguardian.com/world/rss",
    "https://www.cnbc.com/id/10000664/device/rss/rss.html"
]

def get_rss_articles(rss_urls, max_articles=10):
    """
    Fetch articles from the given RSS feed URLs.
    """
    articles = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_articles]:
            articles.append({"title": entry.title, "summary": entry.summary, "link": entry.link})  # Added link
    return articles

def get_newsapi_articles(max_articles=10):
    """
    Fetch top news articles using the NewsAPI.
    """
    top_headlines = newsapi.get_top_headlines(language='en', page_size=max_articles)
    return [{"title": a["title"], "description": a["description"], "link": a["url"]} for a in top_headlines["articles"]]  # Added link
