from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.shiksha.com/engineering/ranking/top-engineering-colleges-in-india/44-2-0-0-0')
r.html.render()  # Execute JavaScript

# Extract data
data = r.html.find('div')
for item in data:
    print(item.text)
