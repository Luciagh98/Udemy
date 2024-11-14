#Hay que saber qué imgen queremos, para no obtener todas
#A veces las imagenes NO estan en formato jpg.

import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/courses/")
sopa = bs4.BeautifulSoup(resultado.text,"lxml") #El string de la web, Formato lxml

#Hay que saber el elemento exacto, sabiendo que las imagenes estan en etiquetas img
imagenes = sopa.select("img")
print(imagenes)
#De esta manera lo imprime en formato lista uno debajo del otro
for imagen in imagenes:
    print(imagen)
#De todas estas, nos interesa las que tiene la clase course-box-image
imagenes_selecionadas = sopa.select(".course-box-image")
imagenes_selecionadas = sopa.select(".course-box-image")[0] #Nos muestra los componentes de la imagen
imagenes_selecionadas = sopa.select(".course-box-image")[0]["src"] #Nos muestra el link donde esta la imagen

#Para descargar la imagen:
imagen_curso1 = requests.get(imagenes_selecionadas)
print(imagen_curso1)#Response 200
print(imagen_curso1.content) #Archivo de la imgen de tipo binario

f = open("mi_imagen.jpg","wb") #Abrimos el archivo en modo lectura binario
f.write(imagen_curso1.content) #Se cargara la imagen con el archivo binario dentro de mi_imagen
f.close() #Para cerrar el archivo

