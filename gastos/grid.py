import tkinter as tk
from tkinter import ttk
from gastos.pantalla import pantalla_gastos

# Importar Diccionario
from datos.gastos import gastos
from datos.categorias import categorias

# Importar utilidades de funciones
from funciones.funciones import centrar_ventana


def gastos_grid():
    ventana = tk.Tk()
    ventana.title("Gastos")

    centrar_ventana(ventana, 1200, 450)

    # Contenido superior
    etiqueta = tk.Label(ventana, text="Administración de Gastos", font=("Arial", 16, "bold"))
    etiqueta.grid(row=0, column=0, columnspan=3, pady=10)

    # <Inicio Treeview>
    tabla = ttk.Treeview(ventana, columns=("ID", "Categoria","Nombre","Monto","Detalle","Fecha"), show="headings", height=15)
    tabla.heading("ID", text="ID Gasto")
    tabla.heading("Categoria", text="Categoría")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Monto", text="Monto")
    tabla.heading("Detalle", text="Detalle")
    tabla.heading("Fecha", text="Fecha")

    # Configuración de columnas
    tabla.column("ID", width=80,anchor='center')
    tabla.column("Categoria", width=200,anchor='w')
    tabla.column("Nombre", width=300,anchor='w')
    tabla.column("Monto", width=120,anchor='e')
    tabla.column("Detalle", width=400,anchor='w')
    tabla.column("Fecha", width=80,anchor='e')


    tabla.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10)

    # Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
    categorias_dict = {c['id_categoria']: c for c in categorias}

    # Insertar datos en el Treeview
    for gasto in gastos:

        # Obtener el nombre de la categoría
        categoria_nombre = categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')     

        tabla.insert("", "end", values=(gasto['id_gastos'], 
                                        categoria_nombre,
                                        gasto['nombre'],
                                        gasto['monto'],
                                        gasto['detalle'],
                                        gasto['fecha']))

    # <Fin Treeview>


    # Botones en la parte inferior
    boton_nuevo = tk.Button(ventana, text="Nuevo",command=lambda:pantalla_gastos())
    boton_nuevo.grid(row=2, column=0, pady=20, padx=10, sticky="ew")

    boton_informe = tk.Button(ventana, text="Informe")
    boton_informe.grid(row=2, column=1, pady=20, padx=10, sticky="ew")

    boton_salir = tk.Button(ventana, text="Salir", command=lambda:ventana.destroy())
    boton_salir.grid(row=2, column=2, pady=20, padx=10, sticky="ew")


    ventana.mainloop()

