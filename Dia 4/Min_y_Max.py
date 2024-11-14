menor = min(58,96,72,64,35)
print (menor)

mayor = max(58,96,72,64,35)
print (mayor)

lista = [58,96,72,64,35]
print (max(lista))
print(f"El menor es {min(lista)} y el mayor es {max(lista)}.")

#tambien nos permite encontrar el primero en orden alfabético
nombres = ["Juan","Pablo","Alicia","Carlos"]
print(min(nombres))

#primero busca el orden en MAYUSCULAS, y luego busca por minisculas
nombres = "Carlos"
print(min(nombres))
print(min(nombres.lower())) #para evitar errores de mayusculas y minusculas

#en los diccionarios, nos muestra la clave que tiene el valor min o max
dic = {"C1":45,"C2":11}
print(min(dic))

#si queremos obtener el valor, usamos el metodo de .values
print(min(dic.values()))