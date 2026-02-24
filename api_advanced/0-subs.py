#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the number of subscribers
for a given subreddit.

Requirements:
- Uses requests module
- Prototype: def number_of_subscribers(subreddit)
- If not a valid subreddit, return 0
- Must not follow redirects (invalid subreddits may redirect to search)
- Must set a custom User-Agent to avoid Too Many Requests errors
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subscribers.checker:v1.0 (by /u/test_user)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json().get("data")
        if data is None:
            return 0

        return data.get("subscribers", 0)
    except Exception:
        return 0
