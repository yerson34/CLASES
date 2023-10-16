#importamos tkinter
from tkinter import *
#instanciar la clase Tk()
ventana=Tk()
ventana.geometry("400x500")
#creo mid dos widget de orden con la clase Flame()
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=100,height=30)

#creacion de etiquetas
etiqueta=Label(ventana,text="INGRESA TU NOMBRE")
etiqueta.grid(row=1,column=0)


#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=1,column=1)

etiqueta=Label(ventana,text="DNI")
etiqueta.grid(row=4,column=0)


#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=4,column=1)

etiqueta=Label(ventana,text="CELULAR")
etiqueta.grid(row=7,column=0)


#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=7,column=1)

cuadro_rojo = Frame(ventana, bg='white', width=240, height=100)
cuadro_rojo.grid(row=10, column=0, columnspan=6)

#usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()