import feedparser

# Five technology news RSS sources
RSS_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "MIT Technology Review": "https://www.technologyreview.com/feed/",
    "Wired": "https://www.wired.com/feed/rss"
}


def collect_news():
    all_news = []

    for source, url in RSS_FEEDS.items():
        print(f"\nFetching news from {source}...")

        feed = feedparser.parse(url)

        # Collect the latest 3 articles from each source
        for entry in feed.entries[:3]:
            news = {
                "source": source,
                "title": entry.get("title", "No title"),
                "summary": entry.get("summary", "No summary"),
                "link": entry.get("link", ""),
                "published": entry.get("published", "Unknown date")
            }

            all_news.append(news)

    return all_news


if __name__ == "__main__":
    news_list = collect_news()

    print("\n========== COLLECTED NEWS ==========")

    for index, news in enumerate(news_list, start=1):
        print(f"\n{index}. {news['title']}")
        print(f"Source: {news['source']}")
        print(f"Link: {news['link']}")

    print(f"\nTotal articles collected: {len(news_list)}")
