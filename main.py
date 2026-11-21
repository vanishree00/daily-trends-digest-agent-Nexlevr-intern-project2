from datetime import datetime
import os
from rss_feeds import collect_news
from ai_summarizer import generate_digest


def main():

    print("\n===== DAILY TRENDS DIGEST AGENT =====")

    # Step 1: Collect news
    print("\nCollecting technology news...")

    news_articles = collect_news()

    if not news_articles:
        print("No news articles found.")
        return

    print(f"\nCollected {len(news_articles)} articles.")

    # Step 2: Generate AI digest
    print("\nGenerating AI-powered digest...")

    digest = generate_digest(news_articles)

    # Step 3: Display final digest
    print("\n========== DAILY DIGEST ==========\n")

    print(digest)

        # Save digest to a Markdown file
    os.makedirs("output", exist_ok=True)

    filename = "output/daily_digest.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("# Daily Technology Trends Digest\n\n")
        file.write(f"**Date:** {datetime.now().strftime('%d-%m-%Y')}\n\n")
        file.write(digest)

    print(f"\nDigest successfully saved to {filename}")


if __name__ == "__main__":
    main()
