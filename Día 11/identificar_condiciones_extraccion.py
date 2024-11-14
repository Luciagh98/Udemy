#Queremos libros de más de 5 estrellas, por ello inspecionamos como se identifican esas 5 estrellas en HTML.
#Se identifican mediante star-rating Three (si tiene 3 estrellas)
#Para el título estan en encabezados dentro de cada bloque de libro.

#Las estrellas y los titulos estan en el mismo nivel, por ello debemos buscar una superior, en este caso,
#la etiqueta de ARTICLE, que contiene todos los datos del libro

import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

resultado = requests.get(url_base.format("1")) #Trabajamos con la primera página
sopa = bs4.BeautifulSoup(resultado.text,'lxml') #Hacemos que podamos trabajar con la url

print(sopa.select(".product_pod")) #Obtemos la clase product_pod, que seria el articulo del libro
print(len(sopa.select(".product_pod"))) #Nos permite confirmar que hemos imprimido los 20 articulos que se muestran
#en la primera página.



