#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.

Requirements:
- Uses requests module
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None
- Must not follow redirects (invalid subreddits may redirect to search)
- Must set a custom User-Agent to avoid Too Many Requests errors
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    If subreddit is invalid, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:top.ten.checker:v1.0 (by /u/test_user)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")
        if data is None:
            print(None)
            return

        posts = data.get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
