#devolverá TRUE si la funcion es cierta
mi_bool = 4 < 5 < 6
print(mi_bool)

#devolvera TRUE si se cumples LAS DOS CONDICIONES
mi_bool2 = 4 < 5 and 5 > 6
print(mi_bool2)

mi_bool3 = 4 < 5 and 5 == 2+3
print(mi_bool3)

#también válido para srtings
mi_bool4 = (55 == 66) and ("perro" == "perro")
print(mi_bool4)

#que se cumpla una de las dos condiciones
mi_bool5 = 4 < 5 or 5 > 6
print(mi_bool5)

texto = "esta frase es breve"
mi_bool6 = ("frase" in  texto) and ("python" in texto)
print(mi_bool)

#devolvera FALSO ya que los dos conceptos SI que son iguales
mi_bool7 = not "a" == "a"
print(mi_bool7)

#devolvera TRUE porque las dos variables NO son diferentes (doble negativa)
mi_bool8= not "a" != "a"
print(mi_bool8)


