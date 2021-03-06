import requests
from pprint import pprint

twitter_url = "https://twitter.com/login"

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer': 'https://twitter.com/explore',
}

s = requests.Session()
response = s.post(twitter_url, headers=headers)

pprint(response.status_code)
pprint(response.url)
