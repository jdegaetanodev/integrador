import tkinter as tk
from tkinter import ttk, messagebox
from funciones.funciones import centrar_ventana
from gastosfijos.funciones import add_gastofijo, update_gastofijo
from categorias.funciones import cargar_categorias

def pantalla_gastosfijos(accion, 
                         id_gasto_fijo=None,
                         id_categoria=None,
                         nombre_categoria="",
                         monto="",
                         descripcion="",
                         mes="",
                         anio="",
                         abonado="No",
                         fecha_pago="",
                         callback_actualizar=None):

    categorias = cargar_categorias()
    mapa_categorias = {c["nombre_categoria"]: c["id_categoria"] for c in categorias}

    ventana = tk.Tk()
    ventana.title("Formulario de Ingresos de Gastos Fijos")
    centrar_ventana(ventana, 450, 450)

    # Nombre
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    entry_nombre.insert(0, nombre_categoria)

    # Categoría
    tk.Label(ventana, text="Categoría:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    combo_categoria = ttk.Combobox(ventana, values=list(mapa_categorias.keys()))
    combo_categoria.grid(row=1, column=1, padx=10, pady=10,sticky="w")
    if nombre_categoria:
        combo_categoria.set(nombre_categoria)
    else:
        combo_categoria.current(0)

    # Monto
    tk.Label(ventana, text="Monto:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    entry_monto = tk.Entry(ventana)
    entry_monto.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    entry_monto.insert(0, monto)

    # Mes
    tk.Label(ventana, text="Mes:").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    combo_mes = ttk.Combobox(ventana, values=meses)
    combo_mes.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    if mes:
        combo_mes.set(mes)
    else:
        combo_mes.current(0)

    # Año
    tk.Label(ventana, text="Año:").grid(row=4, column=0, sticky="w", padx=10, pady=10)
    anios = [str(a) for a in range(2020, 2031)]
    combo_anio = ttk.Combobox(ventana, values=anios)
    combo_anio.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    if anio:
        combo_anio.set(anio)
    else:
        combo_anio.current(0)

    # Abonado
    tk.Label(ventana, text="¿Abonado?:").grid(row=5, column=0, sticky="w", padx=10, pady=10)
    combo_abonado = ttk.Combobox(ventana, values=["Sí", "No"])
    combo_abonado.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    combo_abonado.set(abonado)

    # Fecha de pago
    tk.Label(ventana, text="Fecha de pago:").grid(row=6, column=0, sticky="w", padx=10, pady=10)
    entry_fecha_pago = tk.Entry(ventana)
    entry_fecha_pago.grid(row=6, column=1, padx=10, pady=10, sticky="w")
    entry_fecha_pago.insert(0, fecha_pago)

    # Descripción
    tk.Label(ventana, text="Descripción:").grid(row=7, column=0, sticky="nw", padx=10, pady=10)
    text_descripcion = tk.Text(ventana, height=4, width=30)
    text_descripcion.grid(row=7, column=1, padx=10, pady=10, sticky="w")
    text_descripcion.insert("1.0", descripcion)

    def guardar():
        try:
            nombre = entry_nombre.get()
            id_categoria = mapa_categorias.get(combo_categoria.get(), None)
            if id_categoria is None:
                raise ValueError("Categoría inválida")
            gasto_fijo = {
                "id_categoria": id_categoria,
                "nombre": nombre,
                "monto": float(entry_monto.get()),
                "descripcion": text_descripcion.get("1.0", "end").strip(),
                "mes": combo_mes.get(),
                "anio": combo_anio.get(),
                "abonado": combo_abonado.get(),
                "fecha_pago": entry_fecha_pago.get()
            }

            if accion == "add":
                exito = add_gastofijo(gasto_fijo)
            else:
                exito = update_gastofijo(int(id_gasto_fijo), gasto_fijo)

            if exito:
                messagebox.showinfo("Éxito", "Gasto fijo guardado correctamente.")
                if callback_actualizar:
                    callback_actualizar()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo guardar el gasto fijo.")
        except Exception as e:
            print("Error en guardar gasto fijo:", e)
            messagebox.showerror("Error", "Datos inválidos o incompletos.")

    # Crear un frame para los botones y ubicarlo en la fila 5
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=8, column=0, columnspan=2, sticky="e", padx=10, pady=20)

    btn_cancelar = tk.Button(frame_botones, text="Cancelar",command=lambda:ventana.destroy())
    btn_guardar = tk.Button(frame_botones, text="Guardar", command=guardar)

    btn_guardar.pack(side="right", padx=(5, 0))
    btn_cancelar.pack(side="right")




    ventana.mainloop()