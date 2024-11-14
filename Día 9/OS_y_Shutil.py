import os

#Saber el directorio actual:
print(os.getcwd()) #C:\Users\PrincesaPolar\OneDrive\Escritorio\Cursos y idiomas\Cursos\Python\venv\Día 9

#Crear un nuevo archivo con un texto dentro, y cerrarlo.
archivo = open("curs.txt","w")
archivo.write("texto de prueba")
archivo.close()

#Saber los archivos que tenemos actualmente en el directorio
print(os.listdir()) #['.idea', '.venv', 'Collections.py', 'curs.txt', 'OS_y_Shutil.py']

import shutil

#Mover archivos a otros sitios:
shutil.move("curs.txt","C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\venv\\Día 9\\Mover")

#Eliminar TODO lo que le pasamos de una ruta:
#shutil.rmtree

#Lo podemos hacer des del control de comandos de WINDOWS
#PIP INSTALL SEND2TRASH
#Una vez instalado, ya podemos operar con el des de Python

import send2trash

#Lo eliminamos pero va a la papelera de reciclaje:
send2trash.send2trash("curs.txt")

#Recore el directorio que le pasamos y nos muestra todos los archivos y carpetas que tenemos:
print(os.walk("C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\venv\\Día 9"))

ruta = "C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\venv\\Día 9"

for carpeta, subcarpeta, archivo in os.walk(ruta)
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")
#Pasa por el directorio y dice todos los elementos que contiene, pasando por
#subcarpetas y los archivos de dentro. Hace el loop entero cada vez que encuentra una carpeta.

#También le podemos meter condiciones, haciendo que solo nos muestre los elementos que queremos.





