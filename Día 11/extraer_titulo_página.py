#Extraer el título de la pestaña de la página web.
import bs4
import requests

#Creamos una variable que contenga el link de la web
resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

print(type(resultado)) #<class 'requests.models.Response'>
print(resultado.text) #Nos imprime todo el texto del código fuente en formato STR.

#Con beautifulsoup nos permite identificar los varios elementos de la web
sopa = bs4.BeautifulSoup(resultado.text,"lxml") #El string de la web, Formato lxml
print(sopa) #Nos lo imprime reeordenado, donde ya podemos navegar por él.

print(sopa.select("title")) #Nos permite obtener el elemento que venga encapsulado por ese STRING
#En este caso, el titulo
print(sopa.select("p")) #Para los parrafos
print(len(sopa.select("p"))) #Para saber cuantos párrafos tiene
print(sopa.select("h1")) #Para los encabezados

#Para obtener el titulo sin formato de lista, le decimos que queremos el elemento en la posición 0.
print(sopa.select("title")[0])
#Para obtener solo el texto, usamos el método getText
print(sopa.select("title")[0].getText())

#Queremos obtener un párafo en concreto
parrafo_especial = sopa.select("p") #Nos da una lista con todos los párrafos
print(parrafo_especial)
#Queremos obtener el tercer indice
parrafo_especial = sopa.select("p")[3]
print(parrafo_especial)
#Solo queremos el texto
parrafo_especial=sopa.select("p")[3].getText()
print(parrafo_especial)

#ESTO ES APLICABLE PARA EXTRAER TODOS LOS ELEMENTOS QUE QUERAMOS.


