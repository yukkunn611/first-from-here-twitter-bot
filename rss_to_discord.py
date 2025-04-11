import feedparser
import requests
import os

FEED_URL = os.getenv("FEED_URL")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
STATE_FILE = "last_link.txt"

def load_last_link():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_last_link(link):
    with open(STATE_FILE, "w") as f:
        f.write(link)

def main():
    feed = feedparser.parse(FEED_URL)
    if not feed.entries:
        print("No entries found in feed.")
        return

    latest = feed.entries[0]
    latest_link = latest.link
    latest_title = latest.title

    last_link = load_last_link()
    print(f"Last link: {last_link}")
    print(f"Latest link: {latest_link}")

    if latest_link == last_link:
        print("Already notified. Skipping.")
        return

    # 通知
    content = f"🆕 **{latest_title}**\n{latest_link}"
    data = {"content": content}
    response = requests.post(WEBHOOK_URL, json=data)
    print(f"Posted to Discord: {response.status_code}")

    # 記録更新
    save_last_link(latest_link)

if __name__ == "__main__":
    main()
