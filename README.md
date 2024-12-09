# Bookstore Web Scraper

This project is a web scraper for [Books to Scrape](http://books.toscrape.com/), an online bookstore for testing web scraping scripts. The scraper downloads HTML pages from the site and extracts product information, such as book titles, prices, and URLs saving the data into a csv file.

## Features

- **Download HTML Pages**: Retrieve pages from the bookstore site based on category and pagination.
- **Extract Product Information**: Parse downloaded pages to extract book details.
- **Save to CSV**: Export the extracted data into a CSV file for further analysis.

## Requirements

- Python 3.x
- Dependencies:
  - `playwright`
  - `beautifulsoup4`
  - `pandas`

Install dependencies using

```python
pip install playwright beautifulsoup4 pandas
```

## Scripts

1. `**bookstore_page_downloader.py**`
   This script downloads HTML page for a given book category and saves them locally
2. `**main.py**`
   This script processes the downloaded HTML file to extract product details and save them in a CSV file.

## Usage

1. **Download Pages**: Modify the `query`, `page_from`, and `page_to` parameters in `bookstore_page_downloader.py` to specify the book category and page range to download.

   ```python
   python bookstore_page_downloader.py
   ```

2. **Extract Data**: Modify the `query` and `source_dir` parameters in `main.py` to specify the category and location of the downloaded HTML files.

   ```python
   python main.py
   ```

3. The resulting CSV file will be saved in the project directory.

## Notes

- Ensure the `export` folder exists in the project root or specify a valid path.
- The script works with the `nonfiction_13` category by default. Adjust the `query` parameter for other categories.
