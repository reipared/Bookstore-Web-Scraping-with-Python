from pathlib import Path
from collections import namedtuple
from bs4 import BeautifulSoup
import pandas as pd
from bookstore_page_downloader import download_bookstore_product_page

BookstoreProduct = namedtuple('BookstoreProduct', ['title', 'price', 'url'])

def extract_product_summary(product_element):
    product_name = product_element.h3.a['title']
    product_url = 'http://books.toscrape.com/' + product_element.h3.a['href']
    price = product_element.find('p', 'price_color').text if product_element.find('p', 'price_color') else None
    return BookstoreProduct(title=product_name, price=price, url=product_url)

if __name__ == '__main__':
    query = 'nonfiction_13'
    source_dir = Path('./export')
    if not source_dir.exists():
        raise FileNotFoundError(f'{source_dir} is not found')
    download_bookstore_product_page(query=query, page_from=1, page_to=3, export_location=source_dir)

    records = []
    ignore_sponsored = False
    # html_search_string = 'nonfiction_13'

    for html_file in source_dir.glob(f'{query}*.html'):
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        print(f'Processing file {html_file}')
        products = soup.find_all('article', class_='product_pod')
        for product in products:
            product_summary = extract_product_summary(product)
            records.append(product_summary)

    df = pd.DataFrame(records)
    df.to_csv(f'./{query}.csv', index=False)
    print('Done!')