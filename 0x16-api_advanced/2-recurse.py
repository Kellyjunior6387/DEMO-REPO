#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    hot_list += [post['data']['title'] for post in data['data']['children']]
    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
