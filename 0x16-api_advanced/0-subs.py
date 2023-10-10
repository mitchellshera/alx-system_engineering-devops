#!/usr/bin/python3
"""querying a redditapi"""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        subreddit_data = response.json().get("data")
        
        if subreddit_data and "subscribers" in subreddit_data:
            return subreddit_data["subscribers"]
    
    return 0
