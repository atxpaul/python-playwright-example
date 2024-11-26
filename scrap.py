import asyncio
import json
from playwright.async_api import async_playwright

CATALOGUE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"

async def scrape_page(page, browser, url):
    await page.goto(url)
    books = []

    book_links = await page.query_selector_all("div.col-sm-8.col-md-9 a[title]")
    for link in book_links:
        book_href = await link.get_attribute("href")
        if book_href:
            book_url = CATALOGUE_URL + book_href
            try:
                book_details = await scrape_book_details(browser, book_url)
                books.append(book_details)
            except Exception as e:
                print(f"Failed to scrape book at {book_url}: {e}")

    next_page = await page.query_selector("a:has-text('next')")
    next_url = None
    if next_page:
        next_href = await next_page.get_attribute("href")
        if next_href:
            next_url = CATALOGUE_URL + next_href

    return books, next_url

async def scrape_book_details(browser, book_url):
    page = await browser.new_page()
    await page.goto(book_url)

    title = await page.text_content("h1")
    price = await page.text_content("p.price_color")
    availability = await page.text_content("tr:has(th:has-text('Availability')) td")

    availability_number = 0
    if "In stock" in availability:
        availability_number = int(availability.split("(")[1].split(" ")[0])

    await page.close()

    return {
        "title": title.strip() if title else None,
        "price": price.strip() if price else None,
        "availability": availability_number,
    }

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        url = START_URL
        all_books = []

        while url:
            print(f"Scraping page: {url}")
            try:
                books, next_url = await scrape_page(page, browser, url)
                all_books.extend(books)
                url = next_url
            except Exception as e:
                print(f"Failed to scrape page {url}: {e}")
                break

        with open("books.json", "w", encoding="utf-8") as f:
            json.dump(all_books, f, ensure_ascii=False, indent=4)

        print("Books have been saved to books.json")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
