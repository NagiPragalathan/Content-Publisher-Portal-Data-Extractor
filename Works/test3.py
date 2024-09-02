import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.shiksha.com/mba/ranking/top-mba-colleges-in-india/2-2-0-0-0?pageNo=3')
        content = await page.content()
        print(content)
        with open("sample1.html", "w", encoding="utf-8") as f:
            f.write(content)
        await browser.close()

asyncio.run(main())
