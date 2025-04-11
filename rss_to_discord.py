import feedparser
import requests
import os

FEED_URL = os.getenv("https://rss.app/feeds/dSZqf0Vbx9g8N7IF.xml")
WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1360145434777096294/Kn6dRgJlJerbkeZlHxBRlksHU_CjHcEsSPSQswfDu0l1D4ISxgOwY8QZXsa4vI6q07ln")

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
