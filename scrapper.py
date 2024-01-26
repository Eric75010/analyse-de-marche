import requests
from bs4 import BeautifulSoup


def scrap(url, category_name):
    '''Extracts datas from booktoscrape.com'''

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    url = url.replace("http://books.toscrape.com/catalogue/category/books/", "")
    url = url.replace("/index.html", "")

    print(category_name)

    #title
    title = soup.h1
    print(title.string)

    # prices
    mydivs = soup.find_all("p", {"class": "price_color"})
    print(mydivs)

    price_incl_tax = mydivs[0]
    print(price_incl_tax.string)

    price_exl_tax = mydivs[1]
    print("\n" + price_exl_tax.string)

    # STOCK
    information = soup.find_all("td")
    availability = information[5]
    print("\n" + availability.string)

    # description
    product = soup.find_all("p")
    description = product[3]

    # rate
    ratings = soup.find_all("p", {"class": "star-rating"})
    product_rating = ratings[0]
    string_rating = product_rating["class"][-1]

    match string_rating:
        case "One":
            final_number = 1
        case "two":
            final_number = 2
        case "three":
            final_number = 3
        case "four":
            final_number = 4

    print(string_rating)

    # cover

    cover = soup.find_all("img")
    book_cover = cover[0]
    image_link = book_cover["src"]
    image_link = image_link.replace("../..", "")
    print(image_link)

    url = "http://books.toscrape.com" + image_link
    print(url)
    print(title.string)
    data = requests.get(url).content
    print(data)

    # Opening a new file named img with extension .jpg
    # This file would store the data of the image file

    # category/img.jpg
    f = open(category_name + '/' + title.string + '.jpg', 'wb')

    # Storing the image data inside the data variable to the file
    f.write(data)
    f.close()
    print("http://books.toscrape.com" + image_link)

    # upc
    upc = information[0]
    print("\n" + upc.string)

    # tva
    tax = information[4]
    print("\n" + tax.string)

    # number of reviews
    review = information[6]
    print("\n" + review.string)

    return {
        "title": title.string,
        "price_incl_tax": price_incl_tax.string,
        "price_exl_tax": price_exl_tax.string,
        "availability": availability.string,
        "description": description.string,
        "star_rating": string_rating,
        "cover": image_link,

    }
