#!/usr/bin/python3
""" top ten in reddit api """

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            if "data" in data:
                children = data["data"].get("children", [])
                for post in children:
                    title = post["data"].get("title")
                    if title:
                        print(title)
                return

        print("None")
    except Exception as e:
        print(f"An error occurred: {e}")
