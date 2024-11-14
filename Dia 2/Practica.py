nombre = input("Tu nombre es: ")
ventas = input("Tus ventas son: ")
tipo_comision = 13
comision = float(ventas)*(tipo_comision/100)

print(f"OK {nombre}, este mes ganaste ${round(comision,2)}")

