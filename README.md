# P2 Utilisez les bases de Python pour l'analyse de marché
Récupération de données à partir du site Books.toscrape.com, dans le cadre d'une formation développeur Python.

## Installation
L'application est écrite en Python et développée sur Pycharm.
Il est nécessaire d'avoir installé Python, https://www.python.org/downloads/

## Création de l'environnement virtuel via le terminal
```
python -m venv nom_environnement
```
## Activation de l'environnement virtuel du projet
```
pip install -r requirements.txt
```
## Git

https://github.com/Eric75010/analyse-de-marche/edit/master

## Fonctions
```
extract_book_data_for_detail_page.py: scrapper les informations des livres

extract_book_data_for_category.py: scrapper les informations de toutes les pages par catégorie

csv_generator.py: créer un fichier csv à partir des informations scrappées
```


## Exécuter la récupération de données

```
python all_categories.py
```
