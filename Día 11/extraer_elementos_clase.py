#Extraer una clase completa.
##Hay diferentes simbolos para indicar que queremos extraer de una web.
#Si usamos " = nos trae todos los elementos que tengan la etiqueta entre esas comillas
#Si usamos # = nos muestra un id, los elementos que contengan id=texto puesto
#Si usamos . = nos muestra la clase que contenga ese elemento escrito
#Si usamos (espacio) = nos muestra todos los elementos de la segunda palabra que esten dentro de
#la primera.
#Si usamos > = nos muestra todos los elementos de la segunda palabra que esten dentro de la
#primera, sin que haya nada en el medio.

#Por ejemplo, queremos SOLO el texto de un cuadrado de una web, que a su vez contiene imagenes.

import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
sopa = bs4.BeautifulSoup(resultado.text,"lxml") #El string de la web, Formato lxml

columna_lateral = sopa.select(".sidebar-block") #Nos muestra la caja del lateral
print(columna_lateral)

columna_lateral = sopa.select(".content") #Nos muestra el texto de la columna
columna_lateral = sopa.select(".content p") #Nos muestra los parrafos de esa columna
columna_lateral = sopa.select(".content p")[0] #Nos muestra el primer elemento de los parrafos

#Queremos los textos de esa columna
for p in columna_lateral:
    print(p.getText())
#Por cada elemento p (parrafo) en la columna lateral, muestrame esos parrafos, pero solo
#extrayendo el texto.

