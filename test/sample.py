import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031')

        # Get the HTML content of the page
        content = await page.content()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Container for all the sections' data
        all_sections_data = []

        # Find all section tags
        sections = soup.find_all('section')

        # Iterate over each section and extract data
        for i, section in enumerate(sections):
            section_data = {}

            # Extract the section ID
            section_id = section.get('id')
            section_data['id'] = section_id

            # Extract text within divs
            divs = section.find_all('div')
            divs_data = []
            for div in divs:
                text = div.get_text(strip=True)
                if text:  # Only add if the div contains text
                    divs_data.append(text)
            section_data['divs'] = divs_data

            # Extract tables within the section
            tables = section.find_all('table')
            tables_data = []
            for table in tables:
                table_data = []
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    table_data.append(row_data)
                tables_data.append(table_data)
            section_data['tables'] = tables_data

            # Add the section data to the container
            all_sections_data.append(section_data)

        # Convert the data to JSON format
        json_data = json.dumps(all_sections_data, indent=4)

        # Write the JSON data to a file
        with open('output.json', 'w', encoding='utf-8') as f:
            f.write(json_data)

        await browser.close()

# Run the async function
asyncio.run(main())
