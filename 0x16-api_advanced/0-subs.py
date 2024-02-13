# This function queries the Reddit API and returns the number of subscribers for a given subreddit.
# If the subreddit is invalid, it returns 0.

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit (e.g., 'python')
    :return: The number of subscribers if the subreddit is valid, otherwise 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
