# Web Scraping with Playwright

This repository contains a Python script that demonstrates how to scrape book data from the website [Books to Scrape](https://books.toscrape.com/) using **Playwright**. The script extracts book titles, prices, and availability details and saves the data in a JSON file.

## Features

-   Scrapes multiple pages of book data from the website.
-   Extracts:
    -   Book title
    -   Price
    -   Availability (number of copies in stock)
-   Saves the scraped data to a JSON file (`books.json`).

## Requirements

-   Python 3.7+
-   Playwright

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/atxpaul/python-playwright-example.git
    cd your-repo-name
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install playwright
    playwright install
    ```

## Usage

1. Run the script:

    ```bash
    python scrape_books.py
    ```

2. The script will:

    - Navigate through all the pages of the website.
    - Scrape book details.
    - Save the data to a file named `books.json` in the current directory.

3. Check the output in `books.json`:
    ```json
    [
        {
            "title": "A Light in the Attic",
            "price": "£51.77",
            "availability": 22
        },
        {
            "title": "Tipping the Velvet",
            "price": "£53.74",
            "availability": 20
        }
    ]
    ```

## How It Works

1. The script starts by navigating to the first page of the catalog.
2. It locates all the book links on the current page and extracts their details:
    - Title
    - Price
    - Availability
3. If there is a "next" page, it continues to scrape until all pages are processed.
4. The data is then saved into a JSON file for easy use.

## Customization

-   **Change the output file name**:
    Modify the following line in `main()`:
    ```python
    with open("books.json", "w", encoding="utf-8") as f:
    ```
-   **Scrape additional details**:
    Update the `scrape_book_details` function to extract more information from the book page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

Happy scraping! 🚀
