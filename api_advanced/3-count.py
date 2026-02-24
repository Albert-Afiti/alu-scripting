#!/usr/bin/python3
"""
Script that queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.

Requirements:
- Uses requests module
- Prototype: def count_words(subreddit, word_list)
- If not a valid subreddit, print nothing
- Must not follow redirects (invalid subreddits may redirect to search)
- Must set a custom User-Agent to avoid Too Many Requests errors
- Must use recursion (no loops)
- Case-insensitive keyword matching
- Duplicate keywords in word_list should be summed
- Results printed in descending order by count, then alphabetically
- Words with no matches should be skipped
"""

import requests


def count_words(subreddit, word_list, hot_list=None, after=None, counts=None):
    """
    Recursively fetch all hot article titles for a given subreddit and
    count occurrences of keywords in word_list.
    """
    if hot_list is None:
        hot_list = []
    if counts is None:
        # Normalize word_list to lowercase and handle duplicates
        counts = {}
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] = counts.get(word_lower, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:count.words:v1.0 (by /u/test_user)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json().get("data")
        if data is None:
            return

        children = data.get("children", [])
        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            words = title.split()
            for word in words:
                if word in counts:
                    counts[word] += 1

        after = data.get("after")
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after, counts)

        # Print results
        filtered = {k: v for k, v in counts.items() if v > 0}
        if not filtered:
            return

        sorted_counts = sorted(
            filtered.items(), key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    except Exception:
        return
