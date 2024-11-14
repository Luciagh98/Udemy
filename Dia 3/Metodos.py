texto = "Este es el texto, de Arnedo"

#para hacer un texto en mayusculas
resultado = texto.upper()
print(resultado)

#para escribir un fragmento de la frase en mayuscula
resultado = texto[2].upper()
print(resultado)

#para hacer un texto en minusculas
resultado = texto.lower()
print(resultado)

#para separar el texto y hacer una lista
resultado = texto.split()
print(resultado)

#para separar el texto y hacer una lista i separarlo por el elemento indicado
resultado = texto.split(",")
print(resultado)

#"unir" diferentes palabras a través de un separador, que determinamos nosotros (espacio)
a = "Aprender"
b = "es"
c = "python"
d = "genial"
e = " "
f = e.join([a,b,c,d])

print(f)

#encontrar una letra en el texto
texto = "Este es el texto, de Arnedo"
resultado = texto.find("e")
print(resultado)

#cuando busquemos un elemento que no esta en la frase, el resultado sera -1
texto = "Este es el texto, de Arnedo"
resultado = texto.find("<")
print(resultado)

#reemplazar palabras de la frase
texto = "Este es el texto, de Arnedo"
resultado = texto.replace("Arnedo","Lucia")
print(resultado)

