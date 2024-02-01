import requests
from bs4 import BeautifulSoup
from extract_book_data_for_detail_page import scrap_book_data


def extract_total_page_number_from_footer(page_number):
    # except errors when there is only one page
    try:
        x = page_number.string.strip()
        page_element = x.split()
        page_element = page_element[-1]
    except AttributeError:
        page_element = "1"

    return page_element


def scrap_book_data_for_category(url, category_name):
    """scrap book data by category from bookToScrape.com"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    page_number = soup.find("li", {"class": "current"})
    page_element = extract_total_page_number_from_footer(page_number)

    list_book_element = soup.find_all("article", {"class": "product_pod"})
    found_books_details = []

    for i in range(int(page_element)):

        for book_element in list_book_element:

            a_tag = book_element.find("a")
            url = a_tag["href"]
            url = url.replace("../../../", "https://books.toscrape.com/catalogue/")

            book_details = scrap_book_data(url, category_name)
            found_books_details.append(book_details)

    return found_books_details
