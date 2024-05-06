from tkinter import *

from PIL import Image, ImageTk 

from tkinter import messagebox

ventana = Tk()

ventana.title = "Iniciar sesion"

ventana.geometry("800x500")

ventana.resizable(FALSE, FALSE)

framex = Frame(ventana,bg="dark blue")
framey = Frame(ventana,bg="blue")

framex.place(x=0,y=0,width=400,height=800)
framey.place(x=400,y=0,width=400,height=800)

logo = Image.open("\\Users\\Usuario\\OneDrive\\Escritorio\\carlos\\LOGO UNITECNAR.jpg")
logo = logo.resize((300,150))
logo = ImageTk.PhotoImage(logo)

label = Label(image=logo)
label.place(x=60,y=150)

titulo = Label(ventana, text="INICIO SESION",font= "consolas 13")
titulo.place(x=500, y=80, width=200)

nombre = Label(ventana, text= "USUARIO: ", bg="gray",font= "consolas 11")
nombre.place(x=440, y= 160, width=200)

clave = Label(ventana, text= "CLAVE: ", bg="gray",font= "consolas 11")
clave.place(x= 440, y=220, width=200)

medidas1= Entry(ventana, bg="white",bd= 3)
medidas1.place(x= 600, y=160,width=120)

medidas2= Entry(ventana, width=30, bd=3)
medidas2.place(x=600, y=220, width= 120)

def IS():

    
    messagebox.showinfo("","La Sesion Ha Sido Iniciada")


boton_sesion = Button(ventana,background= "white",text="INGRESAR",font= "consolas 12",command=IS)

boton_sesion.place(x=550,y=300,width= 100)


ventana.mainloop()