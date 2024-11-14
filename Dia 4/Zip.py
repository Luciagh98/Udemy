nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42]

combinados = zip(nombres,edades)
print(combinados)

#para poder mostrar el zip, lo tenemos que transformar en lista
combinados = list(zip(nombres,edades))
print(combinados)

#si tenemos una lista con más valores que otra, se contemplará hasta la mas corta
nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42,55]

#podemos convinar infinitas listas
nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42]
ciudades = ["Lima","Madrid","Mexico"]

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

#podemos hacer un loop con las 3 frases, combinando todos los elementos
for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

