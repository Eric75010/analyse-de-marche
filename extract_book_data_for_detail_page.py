import requests
from bs4 import BeautifulSoup


def scrap_book_data(url, category_name):
    """Extracts book data from book page of booktoscrape.com"""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')


    # title
    title = soup.h1

    # prices
    mydivs = soup.find_all("p", {"class": "price_color"})

    price_incl_tax = mydivs[0]

    price_exl_tax = mydivs[1]

    # STOCK
    information = soup.find_all("td")
    availability = information[5]

    # description
    product = soup.find_all("p")
    description = product[3]

    # rate
    ratings = soup.find_all("p", {"class": "star-rating"})
    product_rating = ratings[0]
    string_rating = product_rating["class"][-1]
    rating = 0

    match string_rating:
        case "One":
            rating = 1
        case "Two":
            rating = 2
        case "Three":
            rating = 3
        case "Four":
            rating = 4
        case "Five":
            rating = 5

    print(rating)

    # cover

    cover = soup.find_all("img")
    book_cover = cover[0]
    image_link = book_cover["src"]
    image_link = image_link.replace("../..", "")

    url = "http://books.toscrape.com" + image_link
    data = requests.get(url).content

    # category/img.jpg
    f = open(category_name + '/' + title.string + '.jpg', 'wb')
    # Storing the image data inside the data variable to the file
    f.write(data)
    f.close()
    print("http://books.toscrape.com" + image_link)

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
        "star_rating": rating,
        "cover": image_link,
        "upc": upc.string,
        "tax": tax.string,
        "review": review.string,
    }
