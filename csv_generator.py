import csv


def generate_csv(category_name, found_books_details):
    """generates  a csv file by category from books details"""

    en_tete = ["title", "price_incl_tax", "price_exl_tax", "availability",
               "description", "star_rating", "cover", "upc", "tax", "review"]

    with open(category_name + '/books.csv', 'w') as fichier_csv:
        # Créer un objet writer (écriture) avec ce fichier
        writer = csv.DictWriter(fichier_csv, fieldnames=en_tete)
        writer.writeheader()
        writer.writerows(found_books_details)
