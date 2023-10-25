from tkinter import *

def verificar_datos():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    if usuario == "yerson" and contraseña == "12345678":
        mensaje.config(text="Bienvenido al sistema")
    else:
        mensaje.config(text="Ingrese bien sus datos")

# Crear la ventana principal
ventana = Tk()
ventana.title("Formulario de Inicio de Sesión")

# Crear etiquetas y entradas
etiqueta_usuario = Label(ventana, text="Usuario:")
etiqueta_contraseña = Label(ventana, text="Contraseña:")
entrada_usuario = Entry(ventana)
entrada_contraseña = Entry(ventana, show="*")  # Para ocultar la contraseña

# Crear botón de verificación
boton_verificar = Button(ventana, text="Verificar", command=verificar_datos)

# Crear etiqueta para mostrar el mensaje
mensaje = Label(ventana, text="")

# Colocar widgets en la ventana
etiqueta_usuario.pack()
entrada_usuario.pack()
etiqueta_contraseña.pack()
entrada_contraseña.pack()
boton_verificar.pack()
mensaje.pack()

# Iniciar la aplicación
ventana.mainloop()
