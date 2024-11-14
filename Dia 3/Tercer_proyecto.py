# Pedimos al usuario la informacion
poema = input("Dime un poema: ")
letra1 = input("Dime la primera letra a buscar: ")
letra2 = input("Dime la segunda letra a buscar: ")
letra3 = input("Dime la tercera letra a buscar: ")

#Contamos el total de apariciones de cada letra.
total_apariciones1 = poema.lower().count(letra1.lower())
total_apariciones2 = poema.lower().count(letra2.lower())
total_apariciones3 = poema.lower().count(letra3.lower())

#lista = [letra1,letra2,letra3]
#print(type(lista))

print(f"\tLa primera letra aparece {total_apariciones1} veces.\n\tLa segunda letra aparece {total_apariciones2} veces.\n\tLa tercera letra aparece {total_apariciones3} veces.")

#Pasamos el poema a lista, para poder contar cuantas palabras hay
lista = poema.split()

print(f"\nEl texto contiene un total de {len(lista)} palabras.")


#Buscamos la primera y la última letra del texto
primera_letra = poema[0].upper()
ultima_letra = poema[len(poema)-1].upper()

print(f"\nLa primera letra es la {primera_letra}, y la última letra es la {ultima_letra} letra.")

#Invertimos el orden del poema y lo unimos
poema_invertido = lista[::-1]
separador = (" ")
print(f"\nTu texto invertido es {separador.join(poema_invertido)}.")

#Buscamos si existe la palabra (python) en el poema.
texto_buscar = "python"
texto_encontrado = poema.lower().find(texto_buscar) > -1

diccionario = {
    True:f"Palabra {texto_buscar} encontrada",
    False:f"La palabra {texto_buscar} no aparece en el poema."
}

print(f"\n{diccionario[texto_encontrado]}")


