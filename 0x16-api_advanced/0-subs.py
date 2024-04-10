import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My User Agent"}  # Set a custom User-Agent header

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, requests.RequestException):
        return 0

# For testing purposes
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))

