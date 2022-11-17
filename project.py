import requests
from bs4 import BeautifulSoup
import csv


Product_page_url = []
Universal_product_code = []
Title = []
Price_including_tax = []
Price_excluding_tax = []
Number_available = []
Product_description = []
Category = []
Review_rating = []
Image_url = []


def Caracteristique1():
    #extension = [f"page-{i}" for i in range()]
    # site de la premiere page de tous les livres
    url = 'http://books.toscrape.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #for i in range(250):

    # premier livre de la premiere page de tous les livres
    for i in range(20):
        UrlpremierLivre = url + soup.findAll('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')[i].find('a')['href']
        #print(UrlpremierLivre)

        # Caractéristiques du premier livre
        page1 = requests.get(UrlpremierLivre)
        soup1 = BeautifulSoup(page1.text, 'html.parser')
        Urlgenerale = soup1.find('table', class_='table table-striped').findAll('td')
        #print(Urlgenerale)
        product_page_url = UrlpremierLivre
        universal_product_code = Urlgenerale[0].text
        title = soup1.findAll('h1')[0].text
        price_including_tax = Urlgenerale[3].text
        price_excluding_tax = Urlgenerale[2].text
        number_available = Urlgenerale[5].text
        product_description = [soup1.findAll('p')[3].text]
        category = soup1.findAll('a')[3].text
        review_rating = Urlgenerale[6].text
        image_url = soup1.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
        Product_page_url.append(product_page_url)
        Universal_product_code.append(universal_product_code)
        Title.append(title)
        Price_including_tax.append(price_including_tax)
        Price_excluding_tax.append(price_excluding_tax)
        Number_available.append(number_available)
        Product_description.append(product_description)
        Category.append(category)
        Review_rating.append(review_rating)
        Image_url.append(image_url)
    print('test1' + ' terminé')


def Caracteristiques(number):
    # extension = [f"page-{i}" for i in range()]
    # site de la premiere page de tous les livres
    url1 = 'http://books.toscrape.com/catalogue/'
    url = 'http://books.toscrape.com/catalogue/page-' + f'{number}' + '.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #for i in range(250):

    # premier livre de la premiere page de tous les livres
    for i in range(20):
        UrlpremierLivre = url1 + soup.findAll('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')[i].find('a')['href']
        #print(UrlpremierLivre)

        # Caractéristiques du premier livre
        page1 = requests.get(UrlpremierLivre)
        soup1 = BeautifulSoup(page1.text, 'html.parser')
        Urlgenerale = soup1.find('table', class_='table table-striped').findAll('td')
        #print(Urlgenerale)
        product_page_url = UrlpremierLivre
        universal_product_code = Urlgenerale[0].text
        title = soup1.findAll('h1')[0].text
        price_including_tax = Urlgenerale[3].text
        price_excluding_tax = Urlgenerale[2].text
        number_available = Urlgenerale[5].text
        product_description = [soup1.findAll('p')[3].text]
        category = soup1.findAll('a')[3].text
        review_rating = Urlgenerale[6].text
        image_url = soup1.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
        Product_page_url.append(product_page_url)
        Universal_product_code.append(universal_product_code)
        Title.append(title)
        Price_including_tax.append(price_including_tax)
        Price_excluding_tax.append(price_excluding_tax)
        Number_available.append(number_available)
        Product_description.append(product_description)
        Category.append(category)
        Review_rating.append(review_rating)
        Image_url.append(image_url)
    print('test' + f'{number}' + ' terminé')


Caracteristique1()
for number in range(2, 51):
    Caracteristiques(number)
Colonnes = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
            'price_excluding_tax', 'number_available', 'product_description', 'category',
            'review_rating']
with open('data.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(Colonnes)
    for a, b, c, d, e, f, g, h, i in zip(Product_page_url, Universal_product_code,
                                            Title, Price_including_tax, Price_excluding_tax,
                                            Number_available, Product_description, Category,
                                            Review_rating):
        ligne = [a, b, c, d.replace('Â', ''), e.replace('Â', ''), f, g, h, i]
        writer.writerow(ligne)

with open('images.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['image_url'])
    for j in Image_url:
        writer.writerow([j])

