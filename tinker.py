"""""
Vianca Navarro.
Quiz 2, programación
"""
import tkinter as tk
from tkinter import messagebox

def conversion():
    try:
        tasa_conversion = 517.47 #Definir la tasa de conersión para el dinero a colocar.
        monto_usd = float(entrada_usd.get())
        monto_crc = monto_usd * tasa_conversion
        resultado_label.config(text=f"{monto_usd} USD = {monto_crc:.2f} CRC")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido.") #Control de entradas numéricas.

def limpiar_pantalla(): #Función para limpiar la pantalla una vez hecha una conversión.
    entrada_usd.delete(0, tk.END)
    resultado_label.config(text="")

def cerrar():
    if messagebox.askyesno("Salir", "¿Está seguro de que desea salir?"):
        ventana.destroy()

#1.Ventana principal.
ventana = tk.Tk() #Ventana principal.
ventana.title("Conversor de moneda. (USD a CRC)")
ventana.geometry("400x300") #Tamaño de ventana

#2.Entrada de datos.
tk.Label(ventana, text="Ingrese monto en USD:").grid(row=0, column=0, padx=10, pady=10)
entrada_usd = tk.Entry(ventana)
entrada_usd.grid(row=0, column=1)

#3,4,5.Botones, mostrar el resultado, diseño.
convertir_btn = tk.Button(ventana, text="Convertir", command=conversion) #Botones y diseño de widgets.
convertir_btn.grid(row=1, column=0, padx=10, pady=10)

limpiar_btn = tk.Button(ventana, text="Limpiar", command=limpiar_pantalla)
limpiar_btn.grid(row=1, column=1, padx=10, pady=10)

resultado_label = tk.Label(ventana, text="") #Resultado.
resultado_label.grid(row=2, column=0, columnspan=2)

#6.Salida del programa.
ventana.protocol("WM_DELETE_WINDOW", cerrar)

ventana.mainloop() #Iniciación del programa.