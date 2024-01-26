import os

import requests
from bs4 import BeautifulSoup
from all_pages import scrap_category

from csv_generator import generate_csv

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

url = url.replace("http://books.toscrape.com/catalogue/category/books/", "")
url = url.replace("/index.html", "")

#categories names
category_links = soup.find("ul", {"class": "nav nav-list"})
links = category_links.find_all("a")
del links[0]
print(links)
#loop for each category to create a category_name file csv
for link in links:
    url = link["href"]
    url = "https://books.toscrape.com/" + url
    print(url)


    category_name = link.string.strip()

    os.mkdir(category_name)

    found_books_details = scrap_category(url, category_name)


    generate_csv(category_name, found_books_details)
