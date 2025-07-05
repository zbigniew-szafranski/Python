import threading
import time

def crawl(link, delay=3):
    print(f"Crawl started for {link}")
    time.sleep(delay)
    print(f"Crawl finished for {link}")

links = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.amazon.pl",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://www.wikipedia.org",
]

threads = []
for link in links:
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()