#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

from collections import Counter
import re
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print a sorted count of given keywords in the titles of all
    hot articles for a given subreddit.
    """
    if counts is None:
        counts = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json()
    titles = [post['data']['title'] for post in data['data']['children']]
    for title in titles:
        words = re.findall(r'\b\w+\b', title.lower())
        for word in words:
            if word in word_list:
                counts[word] += 1

    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, counts, after)

    for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, count))
