from datetime import datetime

import feedparser
import grequests as requests
from newspaper import Article, fulltext

# import requests

if __name__ == "__main__":
    feed = feedparser.parse(
        "https://linkstacks.io/@preslavrachev/stacks/programming-go/feed"
    )

    urls = list(map(lambda entry: entry.link, feed.entries))
    original_urls = requests.map([requests.get(u) for u in urls])
    url_map = dict(zip(urls, original_urls))

    for entry in feed.entries:
        original_url = url_map[entry.link].url
        a = Article(original_url)
        a.download(input_html=url_map[entry.link].text)
        a.parse()
        print('!!! abstract "[' + a.title + "](" + original_url + ')"')

        print(
            '\t<img src="'
            + a.top_image
            + '" style="float:left; margin-right: 1rem; margin-bottom: 1rem; width: 4rem" />'
        )
        print("\t" + entry.description)
        print("\n")
        print("\t_**Date Added**: " + entry.date + "_\n")
        print("\n")
