def chequear_3_cifras(numero):
    return numero in range(100,1000) #con IN hacemos una comprovacion booleana

resultado = chequear_3_cifras(658)
print(resultado)

resultado = chequear_3_cifras(68)
print(resultado)

suma = 586+402
resultado = chequear_3_cifras(suma)
print(resultado)

#________________________________________
#hacemos una funcion de una lista, donde decimos que de cada número en la lista, si el numero esta entre el
#rango 100 y 1000, nos devuelva true, y en caso contrario, que pase al siguiente

def chequear_3_cifras(lista):
    for numero in lista:
        if numero in range(100,1000):
            return True
        else:
            pass

resultado2 = chequear_3_cifras([55,99,6000])
print(resultado2) #nos retorna NONE, significa que no ha encontrado nada en la lista con 3 cifras
print(type(resultado2))

resultado2 = chequear_3_cifras([550,99,6000])
print(resultado2) #nos devuelve TRUE porque ya encontro uno de 3 cifras, el 550

#queremos que nos devuelva FALSE, no es correcto:
def chequear_3_cifras(lista):
    for numero in lista:
        if numero in range(100,1000):
            return True
        else:
            return False

#la forma correcta:
def chequear_3_cifras(lista):
    for numero in lista:
        if numero in range(100,1000):
            return True
        else:
            pass
    return False

#asi, hace el loop del if y en caso de que ninguna cumpla la condición, sale y nos da FALSE.

#imagina que tenemos varios valores con 3 cifras

def chequear_3_cifras(lista):

    lista_3_cifras = []

    for numero in lista:
        if numero in range(100,1000):
            lista_3_cifras.append(numero)
        else:
            pass

    return lista_3_cifras

#añadimos una lista vacia. En el FOR decimos que nos mire cada numero de la lista, y que si (IF) esta en un rango
#entre 100 y 1000 nos lo añana (APPEND) en al lsita. Si no, que PASS al siguiente numero.
#Finalmente, hacemos un return para que nos devuelva el resultado de la lista

resultado3 = chequear_3_cifras([550,99,600])
print(resultado3)
