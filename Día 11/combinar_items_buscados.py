import bs4
import requests

#Crear una url sin numero de página
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

#Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

#Iterar por las páginas
for pagina in range(1,51): #Tenemos 50 páginas

    #Crear una "sopa" que nos permite extraer los elementos
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,"lxml")

    #Seleccionar los libros de cada pagina, y sus datos
    libros = sopa.select(".product_pod")

    #Loop para iterar en los libros
    for libro in libros:
        #Con la condicion de que el libro tenga 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0: #Si la lista es igual a 0 quiere decir que no tiene 4 o 5 estrellas

            #Guardar titulo en una variable
            titulo_libro= libro.select("a")[1]["title"]

            #Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

#Ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)