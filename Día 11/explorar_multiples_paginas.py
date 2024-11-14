import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html" #cambiamos el numero de pagina por {} = x
print(url_base.format("15")) #https://books.toscrape.com/catalogue/page-15.html

for n in range(1,11):
    print(url_base.format(n)) #Obtemeos los url que van de la página 1 a la 10.

