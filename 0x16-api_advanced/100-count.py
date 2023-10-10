#!/usr/bin/python3
"""count function"""
import requests


def count_words(subreddit, word_list, found_dict=None, after=None):
    if found_dict is None:
        found_dict = {}

    if after is None:
        word_list = [word.lower() for word in word_list]

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
        return

    data = response.json().get("data")
    children = data.get("children", [])

    for post in children:
        title = post["data"]["title"].lower()
        for word in title.split():
            if word in word_list:
                if word in found_dict:
                    found_dict[word] += 1
                else:
                    found_dict[word] = 1

    after = data.get("after")

    if after:
        return count_words(subreddit, word_list, found_dict, after)
    else:
        sorted_results = sorted(found_dict.items(),
                                key=lambda item: (-item[1], item[0]))
        for word, count in sorted_results:
            print(f"{word}: {count}")
