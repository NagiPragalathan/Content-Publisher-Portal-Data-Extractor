### **Explanation of `ExtractJson.py`**

This Python script is designed to extract JSON objects embedded in HTML files. The script uses the `BeautifulSoup` library to parse the HTML and the `json` library to process JSON data.

**Steps:**

1. **Import Libraries**:
    
    - `BeautifulSoup` from `bs4` is used to parse HTML content.
    - `json` is used to decode JSON strings into Python dictionaries.
2. **`extract_json_objects_from_html(html_content)` Function**:
    
    - This function takes HTML content as input and searches for all `<script>` tags of type `application/ld+json`.
    - It then extracts the JSON data from each found script tag.
    - The extracted JSON data is appended to the `json_objects` list, which is returned at the end of the function.
3. **Reading the HTML File**:
    
    - The script reads an HTML file located at `Root Folder You can see it after run the ScraperV2.py`.
    - The content of this file is passed to the `extract_json_objects_from_html` function.
4. **Printing the Extracted JSON**:
    
    - The script loops through the list of JSON objects and prints each one in a pretty-printed format.

**Key Points:**

- This script is useful for extracting and printing JSON data embedded in HTML, particularly from websites that use structured data in `<script>` tags.

---

### **Explanation of `ScraperV2.py`**

This Python script uses the Playwright library to scrape web pages. It automates the process of loading a webpage, scrolling to ensure all dynamic content is loaded, and then saving the entire HTML content of the page.

**Steps:**

1. **Import Libraries**:
    
    - `asyncio` is used to handle asynchronous operations.
    - `async_playwright` from the Playwright library is used for browser automation.
2. **`scroll_page(page)` Function**:
    
    - This function scrolls down the webpage repeatedly until no new content is loaded.
    - It evaluates the height of the page before and after scrolling. If the height remains the same, the loop breaks, indicating that all dynamic content has been loaded.
3. **`main(tab)` Function**:
    
    - This is the main function that orchestrates the scraping process.
    - It launches a Chromium browser instance in non-headless mode (visible) and navigates to a specific URL (based on the `tab` parameter).
    - After loading the page, it calls `scroll_page` to ensure all content is loaded.
    - The complete HTML content of the page is then saved to a file named `scraped_page{tab}.html`.
    - Finally, the browser is closed.
4. **Running the Scraping Process**:
    
    - The script loops through the `tabs` list, which contains different URL parameters (`fees` and `reviews`), running the `main` function for each.
    - This allows the script to scrape different pages of the same website.

**Key Points:**

- This script is particularly useful for scraping web pages that load content dynamically as you scroll down (infinite scroll).
- The scraped HTML files can then be processed by other scripts, such as `ExtractJson.py`.

---

### **README.md for DataScraper**

# DataScraper

## Overview

DataScraper is a Python project designed to scrape web pages and extract JSON data embedded within them. The project is divided into two main scripts:

1. **`ScraperV2.py`**: A web scraper that automates the process of loading web pages, scrolling to load all content, and saving the HTML content to a file.
2. **`ExtractJson.py`**: A script that parses the saved HTML files, extracts JSON data from `<script>` tags of type `application/ld+json`, and prints the extracted data.

## Prerequisites

- **Python 3.7+**
- **BeautifulSoup 4** (`bs4`): For HTML parsing.
- **Playwright**: For browser automation.
- **asyncio**: For handling asynchronous operations.

### Installing Dependencies

You can install the required dependencies using `pip`:

To set up Playwright:

```bash
python -m playwright install
```

## Usage

### 1\. Scraping Web Pages

To scrape web pages and save their HTML content:

- Modify the `tabs` list in `ScraperV2.py` to include the URL parameters for the pages you want to scrape.
- Run the script:

```bash
python ScraperV2.py
```

This will generate HTML files (`scraped_page.html`) in the root directory.

### 2\. Extracting JSON Data

After scraping, you can extract JSON data from the saved HTML files using `ExtractJson.py`.

- Ensure the `file_path` variable in `ExtractJson.py` points to the correct HTML file.
- Run the script:

```bash
python ExtractJson.py
```

This will print the extracted JSON data in a readable format.

## Project Structure

```bash
C:. │   ExtractJson.py
    │   Scraper.py 
    │   test3.py 
    │ 
    └───Scraper         
          ScraperV1.py         
          ScraperV2.py
```

- **`ExtractJson.py`**: Script to extract and print JSON data from HTML files.
- **`ScraperV2.py`**: Script to scrape web pages, scroll, and save their HTML content.
- **`ScraperV1.py`**: (Placeholder) Older version of the scraper script, if any.
- **`Scraper` Folder**: Contains different versions of the scraping scripts.

## Notes

- The scraping process can be customized by modifying the `tabs` list in `ScraperV2.py`.
- The extracted JSON can be further processed or saved as needed.
- Ensure that you comply with the website's `robots.txt` file and terms of service when scraping.