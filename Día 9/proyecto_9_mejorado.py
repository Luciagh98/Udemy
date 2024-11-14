import re
import os
import time
import datetime
import math

inicio = time.time()

ruta = 'C:\\Users\\Usuario\\Desktop\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []


def buscar_numeros(archivo, patron):
    try:
        with open(archivo, 'r') as f:
            texto = f.read()
            return re.findall(patron, texto)
    except FileNotFoundError:
        return []


def crear_listas():
    for carpeta, _, archivos in os.walk(ruta):
        for archivo in archivos:
            resultados = buscar_numeros(os.path.join(carpeta, archivo), mi_patron)
            for resultado in resultados:
                nros_encontrados.append(resultado)


def mostrar_todo():
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}\n')
    print('{:<30}{}'.format('ARCHIVO', 'NRO. SERIE'))
    print('-' * 40)
    for archivo, numero in zip(archivos_encontrados, nros_encontrados):
        print(f'{archivo:<30}{numero}')
    print('-' * 40)
    print(f'\nNúmeros encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()
