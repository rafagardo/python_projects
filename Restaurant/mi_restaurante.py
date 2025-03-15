from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
precios_bebida = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
precios_postre = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            c.config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            c.config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for b in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            b.config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            b.focus()
        else:
            b.config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for p in cuadros_postres:
        if variables_postres[x].get() == 1:
            p.config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            p.focus()
        else:
            p.config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida += (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas += (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres += (float(cantidad.get()) * precios_postre[p])
        p += 1

    subtotal = sub_total_comida + sub_total_bebidas + sub_total_postres
    impuesto = subtotal * 0.16
    total = subtotal + impuesto

    var_costo_comida.set(f'$ {sub_total_comida:.2f}')
    var_costo_bebida.set(f'$ {sub_total_bebidas:.2f}')
    var_costo_postre.set(f'$ {sub_total_postres:.2f}')
    var_subtotal.set(f'$ {subtotal:.2f}')
    var_impuesto.set(f'$ {impuesto:.2f}')
    var_total.set(f'$ {total:.2f}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = fecha.strftime('%d-%m-%Y %H:%M:%S')
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n\n')
    texto_recibo.insert(END, f'*' * 70 + '\n')
    texto_recibo.insert(END, 'Items\t\tCantidad\t\tPrecio\n')
    texto_recibo.insert(END, f'-' * 70 + '\n')

    p = 0
    for comida in texto_comida:
        if float(comida.get()) > 0:
            texto_recibo.insert(END, f'{lista_comidas[p]}\t\t{comida.get()}\t\t'
                                        f'$ {int(comida.get()) * precios_comida[p]}\n')
        p += 1

    p = 0
    for bebidas in texto_bebidas:
        if float(bebidas.get()) > 0:
            texto_recibo.insert(END, f'{lista_bebidas[p]}\t\t{bebidas.get()}\t\t'
                                        f'$ {int(bebidas.get()) * precios_bebida[p]}\n')
        p += 1

    p = 0
    for postres in texto_postres:
        if float(postres.get()) > 0:
            texto_recibo.insert(END, f'{lista_postres[p]}\t\t{postres.get()}\t\t'
                                        f'$ {int(postres.get()) * precios_postre[p]}\n')
        p += 1

    texto_recibo.insert(END, f'-' * 70 + '\n')
    texto_recibo.insert(END, f'Subtotal:\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuesto:\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 70 + '\n')
    texto_recibo.insert(END, 'Gracias por su compra\n')
    texto_recibo.insert(END, f'*' * 70 + '\n')

def guardar():
    archivo = texto_recibo.get(1.0, END)
    guardar_archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    guardar_archivo.write(archivo)
    guardar_archivo.close()
    messagebox.showinfo('Guardado', 'El recibo ha sido guardado correctamente')

def resetear():
    texto_recibo.delete(1.0, END)

    for texto in texto_comida:
        texto.set('0')

    for texto in texto_bebidas:
        texto.set('0')

    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for variable in variables_comida:
        variable.set(0)

    for variable in variables_bebidas:
        variable.set(0)

    for variable in variables_postres:
        variable.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# Iniciar tkinter
aplicacion = Tk()


# Configurar la ventana
aplicacion.geometry("1020x630+0+0")


# Evitar maximizar la ventana
aplicacion.resizable(0, 0)


# Titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")


# Color del fondo de la ventana
aplicacion.config(bg="burlywood")


# Panel superior
panel_superior = Frame(aplicacion, bd=1 , relief=FLAT)
panel_superior.pack(side=TOP)


# Etiqueta del titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4",
                        font=("Dosis", 48), bg="burlywood", width=27)
etiqueta_titulo.grid(row=0, column=0)


# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)


# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50, pady=20)
panel_costos.pack(side=BOTTOM)


# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=("Arial", 16, 'bold'),
                           bd=1, relief=FLAT, fg="azure4", pady=40)
panel_comidas.pack(side=LEFT)


# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=("Arial", 16, 'bold'),
                           bd=1, relief=FLAT, fg="azure4", pady=40)
panel_bebidas.pack(side=LEFT)


# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=("Arial", 16, 'bold'),
                           bd=1, relief=FLAT, fg="azure4", pady=40)
panel_postres.pack(side=LEFT)


# Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)


# Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()


# Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()


# Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()

# Lista de comidas
lista_comidas = ['Hamburguesa', 'Pizza', 'Tacos', 'Sushi', 'Pasta', 'Ensalada', 'Pollo', 'Carne', 'Pescado', 'Sopa']
lista_bebidas = ['Agua', 'Refresco', 'Cerveza', 'Vino', 'Café', 'Té', 'Jugo', 'Leche', 'Licuado', 'Smoothie']
lista_postres = ['Pastel', 'Helado', 'Gelatina', 'Galletas', 'Brownie', 'Pay', 'Flan', 'Churros', 'Crepa', 'Fruta']

# Generar lista de variables para comidas
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    # Crear checkbox para comidas
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=("Dosis", 12, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=("Arial", 12, 'bold'), bd=1,
                                     width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

# Generar lista de variables para bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebidas in lista_bebidas:
    # Crear checkbox para bebidas
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=bebidas.title(), font=("Dosis", 12, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebidas[contador], command=revisar_check)
    bebidas.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas, font=("Arial", 12, 'bold'), bd=1,
                                     width=6, state=DISABLED, textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador, column=1)
    contador += 1

# Generar lista de variables para postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    # Crear checkbox para postres
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=("Dosis", 12, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador], command=revisar_check)
    postres.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=("Arial", 12, 'bold'), bd=1,
                                     width=6, state=DISABLED, textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)
    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos, text="Costo Comida: ", font=("Arial", 12, 'bold'), bg="azure4",
                              fg="white")

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=("Arial", 12, 'bold'), bd=1, width=6,
                           state = 'readonly', textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos, text="Costo Bebida: ", font=("Arial", 12, 'bold'), bg="azure4",
                              fg="white")

etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font=("Arial", 12, 'bold'), bd=1, width=6,
                           state = 'readonly', textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos, text="Costo Bebida: ", font=("Arial", 12, 'bold'), bg="azure4",
                              fg="white")

etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, font=("Arial", 12, 'bold'), bd=1, width=6,
                           state = 'readonly', textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos, text="Subtotal:", font=("Arial", 12, 'bold'), bg="azure4",
                              fg="white")

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos, font=("Arial", 12, 'bold'), bd=1, width=6,
                           state = 'readonly', textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuesto = Label(panel_costos, text="Impuesto:", font=("Arial", 12, 'bold'), bg="azure4",
                              fg="white")

etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos, font=("Arial", 12, 'bold'), bd=1, width=6,
                           state = 'readonly', textvariable=var_impuesto)

texto_impuesto.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos, text="Total:", font=("Arial", 12, 'bold'), bg="azure4",
                              fg="white")

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, font=("Arial", 12, 'bold'), bd=1, width=6,
                           state = 'readonly', textvariable=var_total)

texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_guardados = []

columnas = 0

for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("Arial", 12, 'bold'),
                   fg = 'white', bg = 'azure4', bd=1, width=10)

    botones_guardados.append(boton)

    boton.grid(row=0, column=columnas)
    columnas += 1

botones_guardados[0].config(command=total)
botones_guardados[1].config(command=recibo)
botones_guardados[2].config(command=guardar)
botones_guardados[3].config(command=resetear)

# Área de recibo
texto_recibo = Text(panel_recibo, font=("Arial", 12, 'bold'), bd=1, width=47, height=18)

texto_recibo.grid(row=0, column=0)


# Calculadora
visor_calculadora = Entry(panel_calculadora, font=("Arial", 12, 'bold'), bd=1, width=47)

visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                        '4', '5', '6', '-',
                        '1', '2', '3', '*',
                        'CE', '0', '=', '/']

botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=("Arial", 12, 'bold'),
                   fg = 'white', bg = 'azure4', bd=1, width=10)


    botones_guardados.append(boton)

    boton.grid(row=fila, column=columna)
    columna += 1

    if columna > 3:
        columna = 0
        fila += 1

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=borrar)
botones_guardados[13].config(command=lambda: click_boton('0'))
botones_guardados[14].config(command=obtener_resultado)
botones_guardados[15].config(command=lambda: click_boton('/'))


# Evitar que la ventana se cierre
aplicacion.mainloop()