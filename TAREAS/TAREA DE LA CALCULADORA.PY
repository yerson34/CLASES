import tkinter as tk

def sumar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 + num2)

def restar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 - num2)

def multiplicar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 * num2)

def dividir():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    if num2 == 0:
        resultado_var.set("No se puede dividir por cero")
    else:
        resultado_var.set(num1 / num2)

def limpiar():
    numero1_entry.delete(0, tk.END)
    numero2_entry.delete(0, tk.END)
    resultado_var.set("")

ventana = tk.Tk()
ventana.title("Calculadora")

# Marco para los números
marco_numeros = tk.Frame(ventana)
marco_numeros.pack()

numero1_label = tk.Label(marco_numeros, text="Primer número:")
numero1_label.grid(row=0, column=0, padx=10, pady=10)

numero1_entry = tk.Entry(marco_numeros)
numero1_entry.grid(row=0, column=1)

numero2_label = tk.Label(marco_numeros, text="Segundo número:")
numero2_label.grid(row=1, column=0, padx=10, pady=10)

numero2_entry = tk.Entry(marco_numeros)
numero2_entry.grid(row=1, column=1)

# Marco para los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack()

boton_sumar = tk.Button(marco_botones, text="+", width=5, command=sumar)
boton_sumar.grid(row=0, column=0, padx=5, pady=5)

boton_restar = tk.Button(marco_botones, text="-", width=5, command=restar)
boton_restar.grid(row=0, column=1, padx=5, pady=5)

boton_multiplicar = tk.Button(marco_botones, text="*", width=5, command=multiplicar)
boton_multiplicar.grid(row=1, column=0, padx=5, pady=5)

boton_dividir = tk.Button(marco_botones, text="/", width=5, command=dividir)
boton_dividir.grid(row=1, column=1, padx=5, pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=10)

resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var)
resultado_label.pack(pady=10)

ventana.mainloop()
