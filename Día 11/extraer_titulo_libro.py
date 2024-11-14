import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

resultado = requests.get(url_base.format("1")) #Trabajamos con la primera página
sopa = bs4.BeautifulSoup(resultado.text,'lxml') #Hacemos que podamos trabajar con la url

libros = sopa.select(".product_pod") #En esta variable tenemos todos los libros de la pagina en formato lista
ejemplo = libros[0] #Para obtener el primer libro
ejemplo2 = libros[0].select("star-rating.Three") #Confirma si el libro tiene 3 estrellas

print(libros)
print(ejemplo2)

titulo = libros[0].select("a")[1]["title"]#Para obtener el titulo con la etiqueta "a", en la posicion 1,
#con la etiqueta title