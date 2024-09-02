from bs4 import BeautifulSoup
import requests

url = 'https://www.shiksha.com/engineering/ranking/top-engineering-colleges-in-india/44-2-0-0-0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
for item in soup.find_all('div'):
    print(item.text)
