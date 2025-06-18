import tkinter as tk
from tkinter import ttk

# Importar utilidades de funciones
from funciones.funciones import centrar_ventana


def pantalla_gastos():
    #crea una ventana
    ventana = tk.Tk()
    ventana.title("Formulario de ingreso de  Gastos")

    centrar_ventana(ventana, 400, 300)

    #campos
    # Nombre
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    # Categoría (Combo)
    tk.Label(ventana, text="Categoría:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    combo_categoria = ttk.Combobox(ventana, values=["Alimentos", "Transporte", "Salud", "Educación"])
    combo_categoria.grid(row=1, column=1, padx=10, pady=5)
    combo_categoria.current(0)  # Selecciona la primera opción por defecto

    # Monto
    tk.Label(ventana, text="Monto:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_monto = tk.Entry(ventana)
    entry_monto.grid(row=2, column=1, padx=10, pady=5)

    # Fecha
    tk.Label(ventana, text="Fecha:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_fecha = tk.Entry(ventana)
    entry_fecha.grid(row=3, column=1, padx=10, pady=5)

    # Descripción
    tk.Label(ventana, text="Descripción:").grid(row=4, column=0, padx=10, pady=5, sticky="nw")
    text_descripcion = tk.Text(ventana, height=4, width=25)
    text_descripcion.grid(row=4, column=1, padx=10, pady=5)

    #botones
    # Botones
    btn_guardar = tk.Button(ventana, text="Guardar")
    btn_cancelar = tk.Button(ventana, text="Cancelar",command=lambda:ventana.destroy())

    # Colocarlos en una fila debajo (fila 5)
    btn_cancelar.grid(row=5, column=1, padx=10, pady=20, sticky="w")
    btn_guardar.grid(row=5, column=0, padx=10, pady=20, sticky="e")

    ventana.mainloop()
