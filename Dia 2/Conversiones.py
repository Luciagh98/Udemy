num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

#modificar el tipo de variable de float a int
num4 = 5.8
print(num4)
print(type(num4))

num5 = int(num4)
print(num5)
print(type(num5))

#Pedir al usuario que ponga su edad, para poder convertirla en un numero y sumar el valor
age = input("Dime tu edad: ")
age = int(age)
new_age = age + 1
print(new_age)

#optimizar la linea 19 y 20 en una
age = int(input("Dime tu edad: "))
new_age = age + 1
print(new_age)


