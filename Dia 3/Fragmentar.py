texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:3]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::3]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1]
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::-2]
print(fragmento)

# ---------------------------
text = "Calle de los dolores nº3 \"Masies de Voltregà\""
separator = "\""
first_pos = text.index(separator) + 1
second_pos = text.rindex(separator)
sliced_text = text[first_pos: second_pos]

print(f"Text: {text}\nPosition: {first_pos} / {second_pos}\nResult: {sliced_text}")
