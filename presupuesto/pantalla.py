import tkinter as tk
from tkinter import ttk
def pantalla_presupuesto():
    ventana = tk.Tk()
    ventana.title("Formulario de Presupuesto")
    ventana.geometry("400x300")
    # Nombre
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    # Categoría (Combo)
    tk.Label(ventana, text="Categoría:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    combo_categoria = ttk.Combobox(ventana, values=["Alimentos", "Transporte", "Salud", "Ocio"])
    combo_categoria.grid(row=1, column=1, padx=10, pady=5)

    # Monto
    tk.Label(ventana, text="Monto:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_monto = tk.Entry(ventana)
    entry_monto.grid(row=2, column=1, padx=10, pady=5)

    # Mes (Combo)
    tk.Label(ventana, text="Mes:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    combo_mes = ttk.Combobox(ventana, values=meses)
    combo_mes.grid(row=3, column=1, padx=10, pady=5)

    # Año (Combo)
    tk.Label(ventana, text="Año:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    anios = [str(anio) for anio in range(2020, 2031)]
    combo_anio = ttk.Combobox(ventana, values=anios)
    combo_anio.grid(row=4, column=1, padx=10, pady=5)

    # Descripción
    tk.Label(ventana, text="Descripción:").grid(row=5, column=0, padx=10, pady=5, sticky="nw")
    entry_descripcion = tk.Text(ventana, height=4, width=30)
    entry_descripcion.grid(row=5, column=1, padx=10, pady=5)
    # Botón Guardar
    boton_guardar = tk.Button(ventana, text="Guardar")
    boton_guardar.grid(row=6, column=0, padx=10, pady=20, sticky="e")

    # Botón Cancelar
    boton_cancelar = tk.Button(ventana, text="Cancelar",command=lambda:ventana.destroy())
    boton_cancelar.grid(row=6, column=1, padx=10, pady=20, sticky="w")
    ventana.mainloop()
