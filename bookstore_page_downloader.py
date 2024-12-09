from playwright.sync_api import sync_playwright

# url = 'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html'

def download_bookstore_product_page(query, page_from=1, page_to=2, export_location='.'):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page =  browser.new_page()

        for page_num in range(page_from, page_to+1):
            print('process', f'http://books.toscrape.com/catalogue/category/books/{query}/page-{page_num}.html')
            page.goto(f'http://books.toscrape.com/catalogue/category/books/{query}/page-{page_num}.html')
            page.wait_for_load_state('domcontentloaded')

            with open(f'{export_location}/{query}_{page_num}.html', 'w', encoding='utf-8') as f:
                f.write(page.content())

        browser.close()

if __name__ == '__main__':
    query = 'nonfiction_13'
    export_location = './export'
    download_bookstore_product_page(query=query, page_from=1, page_to=3, export_location=export_location)