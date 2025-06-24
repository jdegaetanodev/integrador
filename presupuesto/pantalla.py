import tkinter as tk
from tkinter import ttk, messagebox
from funciones.funciones import centrar_ventana
from categorias.funciones import cargar_categorias
from presupuesto.funciones import add_presupuesto, update_presupuesto

def pantalla_presupuesto(
    accion,
    id_presupuesto=None,
    id_categoria=None,
    monto_presupuesto="",
    descripcion="",
    mes="",
    anio="",
    callback_actualizar=None
):
    categorias = cargar_categorias()
    mapa_categorias = {c["nombre_categoria"]: c["id_categoria"] for c in categorias}

    ventana = tk.Toplevel()
    ventana.title("Formulario de Presupuesto")
    centrar_ventana(ventana, 450, 400)

    # Categoría
    tk.Label(ventana, text="Categoría:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    combo_categoria = ttk.Combobox(ventana, values=list(mapa_categorias.keys()))
    combo_categoria.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    if id_categoria:
        nombre_categoria = next((k for k, v in mapa_categorias.items() if v == int(id_categoria)), "")
        combo_categoria.set(nombre_categoria)
    else:
        combo_categoria.current(0)

    # Monto
    tk.Label(ventana, text="Monto:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    entry_monto = tk.Entry(ventana)
    entry_monto.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    entry_monto.insert(0, monto_presupuesto)

    # Mes
    tk.Label(ventana, text="Mes:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    meses = [str(m) for m in range(1, 13)]
    combo_mes = ttk.Combobox(ventana, values=meses)
    combo_mes.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    combo_mes.set(str(mes) if mes else meses[0])

    # Año
    tk.Label(ventana, text="Año:").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    anios = [str(a) for a in range(2020, 2031)]
    combo_anio = ttk.Combobox(ventana, values=anios)
    combo_anio.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    combo_anio.set(str(anio) if anio else anios[0])

    # Descripción
    tk.Label(ventana, text="Descripción:").grid(row=4, column=0, sticky="nw", padx=10, pady=10)
    text_descripcion = tk.Text(ventana, height=4, width=30)
    text_descripcion.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    text_descripcion.insert("1.0", descripcion)

    def guardar():
        try:
            categoria_nombre = combo_categoria.get()
            id_categoria = mapa_categorias.get(categoria_nombre)

            if not id_categoria:
                raise ValueError("Categoría inválida")

            nuevo_presupuesto = {
                "id_categoria": id_categoria,
                "monto_presupuesto": float(entry_monto.get()),
                "descripcion": text_descripcion.get("1.0", "end").strip(),
                "mes": int(combo_mes.get()),
                "anio": int(combo_anio.get())
            }

            if accion == "add":
                exito = add_presupuesto(nuevo_presupuesto)
            else:
                exito = update_presupuesto(int(id_presupuesto), nuevo_presupuesto)

            if exito:
                messagebox.showinfo("Éxito", "Presupuesto guardado correctamente.")
                if callback_actualizar:
                    callback_actualizar()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo guardar el presupuesto.")
        except Exception as e:
            print("Error al guardar presupuesto:", e)
            messagebox.showerror("Error", "Datos inválidos o incompletos.")

    # Crear un frame para los botones y ubicarlo en la fila 5
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=8, column=0, columnspan=2, sticky="e", padx=10, pady=20)

    btn_cancelar = tk.Button(frame_botones, text="Cancelar",command=lambda:ventana.destroy())
    btn_guardar = tk.Button(frame_botones, text="Guardar", command=guardar)

    btn_guardar.pack(side="right", padx=(5, 0))
    btn_cancelar.pack(side="right")

    ventana.mainloop()