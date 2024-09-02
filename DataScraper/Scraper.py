import asyncio
from playwright.async_api import async_playwright

tabs = ["fees","reviews"]
tabs=['']
async def main(tab):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('http://www.shiksha.com/engineering/ranking/top-engineering-colleges-in-india/44-2-0-0-0'+tab)
        
        # Get the HTML content of the page
        content = await page.content()

        # Write the HTML content to a new file
        with open(f'scraped_page{tab}.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        await browser.close()

# Run the async function
for i in tabs:
    asyncio.run(main(i))
