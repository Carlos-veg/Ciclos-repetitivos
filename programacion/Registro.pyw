import tkinter
from tkinter import *
from tkinter import messagebox


ventana = tkinter.Tk()
ventana.title = "Registro de usuario"
ventana.geometry("350x400")

ventana.resizable(True, True)

nombre = tkinter.Label(ventana, text="Nombre: ")
nombre.grid(row=1 ,column= 0,)

medidas1 = tkinter.Entry(ventana,width= 30)
medidas1.grid(row= 1, column= 1)

apellido = tkinter.Label(ventana, text="Apellido: ")
apellido.grid(row=2 ,column= 0)

medidas2 = tkinter.Entry(ventana, width= 30)
medidas2.grid(row=2 ,column= 1)

edad = tkinter.Label(ventana, text="Edad: ")
edad.grid(row=3 ,column= 0)


medidas3 = tkinter.Entry(ventana, width= 30)
medidas3.grid(row=3 ,column= 1)

direccion = tkinter.Label(ventana, text="Direccion: ")
direccion.grid(row=4 , column= 0)

medidas4 = tkinter.Entry(ventana, width= 30)
medidas4.grid(row=4 , column= 1)

telefono = tkinter.Label(ventana, text="Telefono: ")
telefono.grid(row=5 , column= 0)

medidas5 = tkinter.Entry(ventana, width= 30)
medidas5.grid(row=5 , column= 1)

sexo = tkinter.Label(ventana, text="Sexo: ")
sexo.grid(row=6 , column= 0)

ciudad= Label(ventana, text="Ciudad: ")
ciudad.grid(row=7 ,column= 0)


def obtener_seleccion():
    global valor
    valor = variable.get()
    

variable = tkinter.StringVar(value="Ninguno")
boton_1 = Radiobutton(ventana, text="Femenino", variable = variable,value="Femenino", command=obtener_seleccion)
boton_2 = Radiobutton(ventana, text="Masculino",variable = variable, value="Masculino", command=obtener_seleccion)

boton_1.grid(row=6, column=1)
boton_2.grid(row=6, column=2)

lista = Listbox(ventana, width=20,height=5, selectmode="multiple")
lista.grid(row=8, column= 1)



def ciudadx8():

    global elemento
    ciud = lista.curselection()
    for index in ciud:
        elemento = lista.get(index)
        

ciudades = ["Santa Marta", "Barranquilla", "Cali", "Cartagena"]

for elemento in ciudades:
    lista.insert(tkinter.END, elemento)
    elemento = ""



def registro():
   x1 = medidas1.get()
   x2= medidas2.get()
   x3= medidas3.get()
   x4= medidas4.get()
   x5=  medidas5.get()
   obtener_seleccion()
   ciudadx8()
   x6= valor
   x7 = elemento

   messagebox.showinfo("","NOMBRE: " + x1 + "\n" + "APELLIDO: " + x2 + "\n" + "EDAD: " + x3 + "\n" + "DIRECCION: " + x4 + "\n" + "TELEFONO: " + x5 + "\n" + "SEXO: " + x6 +"\n" + "CIUDAD: " + x7 )
   

registrar= Button(ventana, text="Registrar", command= registro)
registrar.grid(row=9, column=1)


ventana.mainloop()