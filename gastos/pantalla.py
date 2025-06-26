import tkinter as tk
from tkinter import ttk

# Importar utilidades de funciones
from funciones.funciones import centrar_ventana

from categorias.funciones import cargar_categorias
categorias = cargar_categorias()

from gastos.funciones import add_gasto,update_gasto

def pantalla_gastos(accion, id_gasto=None, id_categoria=None, nombre=None, monto=None, detalle=None, fecha=None, callback_actualizar=None):
    
    #crea una ventana
    ventana = tk.Tk()
    ventana.title("Formulario de ingreso de  Gastos")

    centrar_ventana(ventana, 410, 350)

    # Nombre
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")    
    entry_nombre = tk.Entry(ventana, width=35)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Categoría (Combo)
    tk.Label(ventana, text="Categoría:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # Completar el ComboBox
    mapa_categorias = {}

    for categoria in categorias:     
        mapa_categorias[categoria["nombre_categoria"]] = categoria["id_categoria"]

    combo_categoria = ttk.Combobox(ventana, width=35, values=list(mapa_categorias.keys()))

    combo_categoria.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Fin Completar el ComboBox

    # Monto
    tk.Label(ventana, text="Monto:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_monto = tk.Entry(ventana, width=35)
    entry_monto.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    
    # Fecha
    tk.Label(ventana, text="Fecha:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_fecha = tk.Entry(ventana, width=35)
    entry_fecha.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # Descripción
    tk.Label(ventana, text="Descripción:").grid(row=4, column=0, padx=10, pady=10, sticky="w")    
    text_descripcion = tk.Text(ventana, height=5, width=35)
    text_descripcion.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    
    if accion == 'update':
        entry_nombre.insert(0, nombre)
        entry_monto.insert(0, monto)
        entry_fecha.insert(0, fecha)    
        text_descripcion.insert("1.0", detalle)

        nombre_categoria_seleccionada = next(
            (nombre for nombre, id_cat in mapa_categorias.items() if id_cat == int(id_categoria)),
            None
        )

        if nombre_categoria_seleccionada:
            combo_categoria.set(nombre_categoria_seleccionada)  

    # Crear un frame para los botones y ubicarlo en la fila 5
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=5, column=0, columnspan=2, sticky="e", padx=10, pady=20)

    if accion == "add":
        btn_guardar = tk.Button(frame_botones, text="Guardar", command=lambda: add_gasto(
                                                                                            entry_nombre.get(),
                                                                                            mapa_categorias.get(combo_categoria.get()),
                                                                                            entry_monto.get(),
                                                                                            entry_fecha.get(),
                                                                                            text_descripcion.get("1.0", "end").strip(),
                                                                                            ventana,
                                                                                            callback_actualizar
                                                                                        ))
    else:
        btn_guardar = tk.Button(frame_botones, text="Guardar",command=lambda:update_gasto(  id_gasto,
                                                                                            id_categoria, 
                                                                                            entry_nombre.get(),
                                                                                            combo_categoria.get(),
                                                                                            entry_monto.get(),
                                                                                            entry_fecha.get(),
                                                                                            text_descripcion.get("1.0", "end").strip(),
                                                                                            ventana, 
                                                                                            callback_actualizar))

    btn_cancelar = tk.Button(frame_botones, text="Cancelar",command=lambda:ventana.destroy())

    btn_guardar.pack(side="right", padx=(5, 0))
    btn_cancelar.pack(side="right")

    ventana.mainloop()