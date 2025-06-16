import tkinter as tk
from tkinter import ttk
def pantalla_gastosfijos():
# Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Formulario de Ingresos de Gastos Fijos")
    ventana.geometry("450x400")

    # --------- CAMPO: Nombre ---------
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    # --------- CAMPO: Categoría ---------
    tk.Label(ventana, text="Categoría:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    combo_categoria = ttk.Combobox(ventana, values=["Servicio", "Producto", "Otro"])
    combo_categoria.grid(row=1, column=1, padx=10, pady=5)
    combo_categoria.current(0)

    # --------- CAMPO: Monto ---------
    tk.Label(ventana, text="Monto:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_monto = tk.Entry(ventana)
    entry_monto.grid(row=2, column=1, padx=10, pady=5)

    # --------- CAMPO: Mes ---------
    tk.Label(ventana, text="Mes:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    combo_mes = ttk.Combobox(ventana, values=meses)
    combo_mes.grid(row=3, column=1, padx=10, pady=5)
    combo_mes.current(0)

    # --------- CAMPO: Año ---------
    tk.Label(ventana, text="Año:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    anios = [str(a) for a in range(2020, 2031)]
    combo_anio = ttk.Combobox(ventana, values=anios)
    combo_anio.grid(row=4, column=1, padx=10, pady=5)
    combo_anio.current(0)

    # --------- CAMPO: Abonado ---------
    tk.Label(ventana, text="¿Abonado?:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
    combo_abonado = ttk.Combobox(ventana, values=["Sí", "No"])
    combo_abonado.grid(row=5, column=1, padx=10, pady=5)
    combo_abonado.current(0)

    # --------- CAMPO: Fecha de pago ---------
    tk.Label(ventana, text="Fecha de pago:").grid(row=6, column=0, sticky="w", padx=10, pady=5)
    entry_fecha_pago = tk.Entry(ventana)
    entry_fecha_pago.grid(row=6, column=1, padx=10, pady=5)

    # --------- CAMPO: Descripción ---------
    tk.Label(ventana, text="Descripción:").grid(row=7, column=0, sticky="nw", padx=10, pady=5)
    text_descripcion = tk.Text(ventana, height=4, width=30)
    text_descripcion.grid(row=7, column=1, padx=10, pady=5)

    # --------- BOTONES: Guardar y Cancelar ---------
    btn_guardar = tk.Button(ventana, text="Guardar")
    btn_cancelar = tk.Button(ventana, text="Cancelar",command=lambda:ventana.destroy())

    btn_guardar.grid(row=8, column=0, padx=10, pady=20, sticky="e")
    btn_cancelar.grid(row=8, column=1, padx=10, pady=20, sticky="w")

    # Ejecutar la ventana
    ventana.mainloop()
