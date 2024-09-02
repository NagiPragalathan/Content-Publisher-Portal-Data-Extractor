import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = 'http://www.shiksha.com/engineering/ranking/top-engineering-colleges-in-india/44-2-0-0-0'
response = requests.get(url, headers=headers)
print(response.text)
