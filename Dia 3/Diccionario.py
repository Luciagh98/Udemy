diccionario = {"c1":"valor1","c2":"valor2","c3":"valor3"}
print(type(diccionario))
print(diccionario)

#consultar lo que tenemos en las claves
resultado = diccionario["c1"]
print(resultado)

cliente = {"Nombre":"Juan", "Apellido":"Garcia", "peso":55, "talla": 1.76}
consulta = (cliente["Apellido"])
print(consulta)

#imprimir un dato concreto del diccionario--> de la clave dos, el segundo indice
dic = {"clave1":55, "clave2":[10,20,30], "clave3" : {"si":100, "s2":200}}
print(dic["clave2"][1])
dic = {"clave1":55, "clave2":[10,20,30], "clave3" : {"si":100, "s2":200}}
print(dic["clave3"]["s2"])

#buscar un dato del diccionario y ponerlo en mayusculas
di = {"c1":["a","b","c"], "c2": ["d","e","f"]}
print(di)
print(di["c2"][1].upper())

#añadimos una variable nueva, asignando directamente el valor que queremos poner
di = {1:"a",2:"b"}
print(di)
di[3] = "c"
print(di)

#añadimos una variable nueva, eligiendo un nombre y asignando directamente el valor que queremos poner
di = {"v1":"a","v2":"b"}
print(di)
di["v3"] = "c"
print(di)

#podemos cambiar en el momento el valor de una clave
di[2] = "B"
print(di)

#nos imprime las claves del diccionario
print(di.keys())

#nos imprime los valores de las claves
print(di.values())

#nos muestra todos los valores del diccionario
print(di.items())


