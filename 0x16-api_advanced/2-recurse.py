#!/usr/bin/python3
"""returns hot articles in reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if after is None:
        after = ""

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    children = data.get("children", [])

    for post in children:
        title = post["data"].get("title")
        if title:
            hot_list.append(title)

    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
