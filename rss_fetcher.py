import feedparser

RSS_FEEDS = {
    "Tech": "https://techcrunch.com/feed/",
    "Sports": "https://www.espn.com/espn/rss/news",
    "Business": "https://www.investing.com/rss/news_25.rss"
}

def get_articles(category="Tech"):
    feed_url = RSS_FEEDS.get(category, RSS_FEEDS["Tech"])
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries[:5]:
        # Fallback if summary is not available
        summary = getattr(entry, "summary", None) or getattr(entry, "description", "No summary available")
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary
        })

    return articles
