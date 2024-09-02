import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extracting all text data from the site
    text_data = soup.get_text(separator=" ", strip=True)
    
    return text_data

def scrape_entire_site(base_url):
    visited = set()
    to_visit = [base_url]
    
    all_content = []

    while to_visit:
        url = to_visit.pop(0)
        if url not in visited:
            print(f"Scraping: {url}")
            visited.add(url)

            # Scrape the page
            content = scrape_page(url)
            all_content.append(content)

            # Find all links on the current page and add them to the queue
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            for link in soup.find_all('a', href=True):
                full_url = urljoin(base_url, link['href'])
                
                # Ensure the link is within the same domain
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    if full_url not in visited and full_url not in to_visit:
                        to_visit.append(full_url)
    
    return all_content

# Example usage:
base_url = "https://www.shiksha.com/"  # Replace with the site you want to scrape
scraped_data = scrape_entire_site(base_url)

# Optionally, save or process the scraped data
for i, content in enumerate(scraped_data):
    print(f"Content from page {i+1}:")
    print(content)
    print("\n" + "="*80 + "\n")
