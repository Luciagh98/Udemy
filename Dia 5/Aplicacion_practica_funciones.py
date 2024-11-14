precios_cafe = [("capucchino",1.50),("expresso",1.20),("moka",1.9)]

for elemento in precios_cafe:
    print(elemento)

#si solo queremos el cafe de las tuples, lo hacemos de la siguiente manera:
for cafe,precio  in precios_cafe:
    print(cafe)

#si queremos saber solo el precio
for cafe,precio  in precios_cafe:
    print(precio  * 0.45)

#_______________________________

precios_cafe = [("capucchino",1.50),("expresso",1.20),("moka",1.9)]

#Hacemos una funcion con dos variables, precio mayor y cafe mas caro. Le decimos , en el FOR, que por el cafe y el precio haga diferentes cosas
#que por cada valor que el precio sea mayor, que devuelva el valor mas alto, y su correspondiente cafe
def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = " "

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe,precio = cafe_mas_caro(precios_cafe)

print(f"El cafe más caro es {cafe}, cuyo precio es {precio}.")