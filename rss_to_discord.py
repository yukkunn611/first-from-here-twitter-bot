import feedparser
import requests
import os

FEED_URL = os.getenv("FEED_URL")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def main():
    feed = feedparser.parse(FEED_URL)
    if not feed.entries:
        print("No entries found in feed.")
        return

    latest = feed.entries[0]
    title = latest.title
    link = latest.link

    content = f"🆕 **{title}**\n{link}"
    data = {"content": content}
    response = requests.post(WEBHOOK_URL, json=data)

    print(f"Posted to Discord: {response.status_code}")

if __name__ == "__main__":
    main()
