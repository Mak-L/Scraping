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


def caracteristiques_livres_page1():
    # site de la premiere page de tous les livres
    url = 'http://books.toscrape.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    for i in range(20):
        url_premier_livre = url + soup.findAll('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')[i].find('a')['href']
        page1 = requests.get(url_premier_livre)
        soup1 = BeautifulSoup(page1.text, 'html.parser')
        url_generale = soup1.find('table', class_='table table-striped').findAll('td')
        product_page_url = url_premier_livre
        universal_product_code = url_generale[0].text
        title = soup1.findAll('h1')[0].text
        price_including_tax = url_generale[3].text
        price_excluding_tax = url_generale[2].text
        number_available = url_generale[5].text
        product_description = [soup1.findAll('p')[3].text]
        category = soup1.findAll('a')[3].text
        review_rating = url_generale[6].text
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


def caracteristiques_livres_autres_pages(number):
    url1 = 'http://books.toscrape.com/catalogue/'
    url = 'http://books.toscrape.com/catalogue/page-' + f'{number}' + '.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    for i in range(20):
        url_premier_livre = url1 + soup.findAll('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')[i].find('a')['href']
        page1 = requests.get(url_premier_livre)
        soup1 = BeautifulSoup(page1.text, 'html.parser')
        url_generale = soup1.find('table', class_='table table-striped').findAll('td')
        product_page_url = url_premier_livre
        universal_product_code = url_generale[0].text
        title = soup1.findAll('h1')[0].text
        price_including_tax = url_generale[3].text
        price_excluding_tax = url_generale[2].text
        number_available = url_generale[5].text
        product_description = [soup1.findAll('p')[3].text]
        category = soup1.findAll('a')[3].text
        review_rating = url_generale[6].text
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


caracteristiques_livres_page1()
for number in range(2, 51):
    caracteristiques_livres_autres_pages(number)
colonnes = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
            'price_excluding_tax', 'number_available', 'product_description', 'category',
            'review_rating', 'image_url']
with open('data.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(colonnes)
    for a, b, c, d, e, f, g, h, i, j in zip(Product_page_url, Universal_product_code,
                                            Title, Price_including_tax, Price_excluding_tax,
                                            Number_available, Product_description, Category,
                                            Review_rating, Image_url):
        ligne = [a, b, c, d.replace('Â', ''), e.replace('Â', ''), f, g, h, i, j]
        writer.writerow(ligne)


