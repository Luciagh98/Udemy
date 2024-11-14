from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador += numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    try:
        resultado = str(eval(operador))
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, resultado)
        operador = ""
    except:
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, "Error")


def revisar_check(lista_cuadros, lista_variables, lista_textos):
    for i in range(len(lista_cuadros)):
        if lista_variables[i].get() == 1:
            lista_cuadros[i].config(state=NORMAL)
            if lista_cuadros[i].get() == "0":
                lista_cuadros[i].delete(0, END)
            lista_cuadros[i].focus()
        else:
            lista_cuadros[i].config(state=DISABLED)
            lista_textos[i].set("0")


def calcular_total(lista_textos, precios):
    return sum(float(cantidad.get()) * precio for cantidad, precio in zip(lista_textos, precios))


def total():
    sub_total_comida = calcular_total(texto_comida, precios_comida)
    sub_total_bebida = calcular_total(texto_bebida, precios_bebida)
    sub_total_postres = calcular_total(texto_postres, precios_postres)

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postres.set(f"$ {round(sub_total_postres, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuesto.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"Nº - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"{'*' * 75}\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"{'-' * 90}\n")

    for lista, precios, nombres in zip([texto_comida, texto_bebida, texto_postres],
                                       [precios_comida, precios_bebida, precios_postres],
                                       [lista_comidas, lista_bebidas, lista_postres]):
        for i in range(len(lista)):
            if lista[i].get() != "0":
                texto_recibo.insert(END, f"{nombres[i]}\t\t{lista[i].get()}\t${int(lista[i].get()) * precios[i]}\n")

    texto_recibo.insert(END, f"{'-' * 90}\n")
    texto_recibo.insert(END, f"Costo de la Comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo de los Postres: \t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(END, f"{'-' * 90}\n")
    texto_recibo.insert(END, f"Sub-total:  \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos: \t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"{'*' * 75}\n")
    texto_recibo.insert(END, "Lo esperamos pronto")


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if archivo:
        archivo.write(info_recibo)
        archivo.close()
        messagebox.showinfo("Información", "Su recibo ha sido guardado.")


def resetear():
    texto_recibo.delete(1.0, END)
    for lista_textos in [texto_comida, texto_bebida, texto_postres]:
        for texto in lista_textos:
            texto.set("0")

    for lista_cuadros in [cuadros_comida, cuadros_bebida, cuadros_postres]:
        for cuadro in lista_cuadros:
            cuadro.config(state=DISABLED)

    for lista_vars in [variables_comida, variables_bebida, variables_postres]:
        for v in lista_vars:
            v.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")


def crear_checkbuttons(panel, lista_items, lista_vars, lista_textos, lista_cuadros, precios):
    for i, item in enumerate(lista_items):
        var = IntVar()
        lista_vars.append(var)
        check = Checkbutton(panel, text=item.title(), font=("Dosis", 19, "bold"), onvalue=1, offvalue=0, variable=var,
                            command=lambda: revisar_check(lista_cuadros, lista_vars, lista_textos))
        check.grid(row=i, column=0, sticky=W)

        texto = StringVar()
        texto.set("0")
        lista_textos.append(texto)
        entry = Entry(panel, font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable=texto)
        entry.grid(row=i, column=1)
        lista_cuadros.append(entry)


# Crear una instancia de Tkinter (la ventana principal)
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry("1140x630+0+0")
# Evitar que el usuario maximice la pantalla
aplicacion.resizable(False, False)
# Establecer un encabezado a la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")
# Establecer un color de fondo
aplicacion.config(bg="aquamarine2")

# Panel superior, con el titulo del programa
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4", font=("Dosis", 58),
                        bg="aquamarine2", width=20)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50)
panel_costos.pack(side=BOTTOM)

# Panel de comida
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

# Panel de postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

# Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel de calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="aquamarine2")
panel_calculadora.pack()

# Panel de recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="aquamarine2")
panel_recibo.pack()

# Panel de botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="aquamarine2")
panel_botones.pack()

# Lista de productos
lista_comidas = ["pollo", "cordero", "salmon", "merluza", "kebab", "pizza1", "pizza2", "pizza3"]
lista_bebidas = ["agua", "soda", "jugo", "cola", "vino1", "vino2", "cerveza1", "cerveza2"]
lista_postres = ["helado", "fruta", "brownie", "flan", "mousse", "pastel1", "pastel2", "pastel3"]

# Variables, cuadros de texto y checks para comida
variables_comida, texto_comida, cuadros_comida = [], [], []
crear_checkbuttons(panel_comidas, lista_comidas, variables_comida, texto_comida, cuadros_comida, precios_comida)

# Variables, cuadros de texto y checks para bebida
variables_bebida, texto_bebida, cuadros_bebida = [], [], []
crear_checkbuttons(panel_bebidas, lista_bebidas, variables_bebida, texto_bebida, cuadros_bebida, precios_bebida)

# Variables, cuadros de texto y checks para postres
variables_postres, texto_postres, cuadros_postres = [], [], []
crear_checkbuttons(panel_postres, lista_postres, variables_postres, texto_postres, cuadros_postres, precios_postres)

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos, text="Costo Comida", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly",
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos, text="Costo Bebida", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos, text="Costo Postres", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_costo_postres.grid(row=2, column=0)
texto_costo_postres = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly",
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos, text="Sub-total", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly",
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos, text="Impuestos", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly",
                        textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos, text="Total", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ["total", "recibo", "guardar", "resetear"]
comandos = [total, recibo, guardar, resetear]
columnas = 0
for boton, comando in zip(botones, comandos):
    Button(panel_botones, text=boton.title(), font=("Dosis", 14, "bold"), fg="white", bg="azure4", bd=1, width=9,
           command=comando).grid(row=0, column=columnas)
    columnas += 1

# Area de recibo
texto_recibo = Text(panel_recibo, font=("Dosis", 12, "bold"), bd=1, width=42, height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=("Dosis", 16, "bold"), width=32, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "R", "B", "0", "/"]
fila = 1
columna = 0

for boton in botones_calculadora:
    if boton == "R":
        Button(panel_calculadora, text=boton.title(), font=("Dosis", 16, "bold"), fg="white", bg="azure4", bd=1,
               width=8, command=obtener_resultado).grid(row=fila, column=columna)
    elif boton == "B":
        Button(panel_calculadora, text=boton.title(), font=("Dosis", 16, "bold"), fg="white", bg="azure4", bd=1,
               width=8, command=borrar).grid(row=fila, column=columna)
    else:
        Button(panel_calculadora, text=boton.title(), font=("Dosis", 16, "bold"), fg="white", bg="azure4", bd=1,
               width=8, command=lambda x=boton: click_boton(x)).grid(row=fila, column=columna)

    columna += 1
    if columna == 4:
        fila += 1
        columna = 0

# Evitar que la pantalla se cierre
aplicacion.mainloop()
