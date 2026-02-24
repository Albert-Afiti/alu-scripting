#!/usr/bin/python3
"""
Script that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit using recursion.

Requirements:
- Uses requests module
- Prototype: def recurse(subreddit, hot_list=[])
- If not a valid subreddit, return None
- Must not follow redirects (invalid subreddits may redirect to search)
- Must set a custom User-Agent to avoid Too Many Requests errors
- Must use recursion (no loops)
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetch all hot article titles for a given subreddit.
    Returns a list of titles, or None if invalid subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:recurse.hot.posts:v1.0 (by /u/test_user)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return None

        data = response.json().get("data")
        if data is None:
            return None

        children = data.get("children", [])
        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list if hot_list else None
    except Exception:
        return None
