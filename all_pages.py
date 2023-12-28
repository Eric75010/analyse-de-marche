import requests
from bs4 import BeautifulSoup
from scrapper import scrap
def scrap_category(url, category_name):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #category name extract from url..
    url = url.replace("http://books.toscrape.com/catalogue/category/books/", "")
    url = url.replace("/index.html", "")
    print(category_name)

    category_links = soup.find_all("h1", {"class": "page-header action"})
    print(category_links)

    page_number = soup.find("li", {"class": "current"})

    try:
        x = page_number.string.strip()

        page_element = x.split()
        page_element = page_element[-1]
    except AttributeError:

        page_element = "1"

    list_book_element = soup.find_all("article", {"class": "product_pod"})
    found_books_details = []

    for i in range(int(page_element)):

        for book_element in list_book_element:
            a_tag = book_element.find("a")
            url = a_tag["href"]
            url = url.replace("../../../", "https://books.toscrape.com/catalogue/")

            book_details = scrap(url, category_name)
            found_books_details.append(book_details)

            print(url)
            print(page_element)
            print(url)

    return found_books_details

