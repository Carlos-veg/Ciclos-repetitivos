from tkinter import *
def cambiar_texto():
    etiqueta.config(text="bye")

def obtener_seleccion():
    seleccion = variable.get()
    if seleccion ==1:
        print("Opción 1 seleccionada")
    elif seleccion ==2:
        print("Opción 2 seleccionada")
    elif seleccion ==3:
        print("Opción 3 seleccionada")
def obtener_estado():
    if variable.get() ==1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)

ventana = Tk()

ventana.geometry("1024x920")
ventana.resizable(True, True)
ventana.config(bg="blue")
etiqueta = Label(ventana, text="hello world", bg="black", fg="blue", font=("calibri", 18), width=20, height=2, anchor="center")
etiqueta.pack()
etiquet = Label(ventana, text="hello world", bg="black", fg="blue", font=("calibri", 18), width=20, height=2, anchor="center")
etiquet.pack()
etiqueta.place(x=350, y=700)

boton1 = Button(ventana, text="Cambiar", command=cambiar_texto, bg="pink",fg="white",font=("calibri", 18), width=20, height=2, anchor="center")
boton1.pack()
boton2 = Button(ventana, text="Botón 2", bg="pink", fg="white",font=("calibri", 18), width=20, height=2, anchor="center")
boton2.pack()
boton3 = Button(ventana, text="Deshabilitado", state="disabled",bg="pink", fg="white", font=("calibri", 18), width=20, height=2, anchor="center")
boton3.pack()
cuadro_texto = Entry(ventana, font=("calibri", 18))

cuadro_texto.pack()
boton = Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()
marco1 = Frame(ventana, width=300, height=200, bd=5, relief="solid")
marco1.pack()
etiqueta3 = Label(marco1, text="Marco 1")
etiqueta3.pack()
marco2 = Frame(ventana, width=200, height=100, bd=5, relief="raised")
marco2.pack()
etiqueta2 = Label(marco2, text="Marco 2")
etiqueta2.pack()

cuadro_lista = Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
for elemento in elementos:
    cuadro_lista.insert(END, elemento)

boton = Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

variable = IntVar()

casilla_verificacion = Checkbutton(ventana, text="Opción 1", variable=variable, command=obtener_estado)
casilla_verificacion.pack()
opcion2 = Radiobutton(ventana, text="Opción 2", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()
opcion3 = Radiobutton(ventana, text="Opción 3", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()

ventana.mainloop()