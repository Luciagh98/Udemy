#abrir y manipular archivos
mi_archivo= open("prueba.txt") #transferimos el archivo a python

print(mi_archivo) #<_io.TextIOWrapper name='prueba.txt' mode='r' encoding='cp1252'>

print(mi_archivo.read()) #queremos leer el archivo

una_linea = mi_archivo.readline() #nos imprime una linea
print(una_linea)

#si queremos imprimir las horas, podemos ir generado el mismo código debajo, ya que irá leyendo la última linea leida.

una_linea = mi_archivo.readline() #nos imprime la segunda linea
print(una_linea)

una_linea = mi_archivo.readline() #nos imprime la tercera linea
print(una_linea)

#Podemos aplicar todos los metodos de strings.

print(mi_archivo.read().upper())

#Podemos concatenar lineas

for linea in mi_archivo:
    print("Aqui dice: " + linea)

todas = mi_archivo.readline()
print(todas) #nos lo imprime  en formato de listas

todas = todas.pop() #nos muestra una linea de la lista de todas las lineas

mi_archivo.close #nos permite cerrar el arcivo para que no perjudique al ordenador