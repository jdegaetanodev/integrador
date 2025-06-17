import tkinter as tk
from tkinter import ttk
from presupuesto.pantalla import pantalla_presupuesto

# Importar Diccionario
from datos.presupuestos import presupuestos
from datos.categorias import categorias 


def presupuesto_grid():
    ventana = tk.Tk()
    ventana.title("Presupuesto")
    ventana.geometry("700x450")

    # Contenido superior
    etiqueta = tk.Label(ventana, text="Administración de Presupuestos", font=("Arial", 16, "bold"))
    etiqueta.grid(row=0, column=0, columnspan=3, pady=20)

    ventana.grid_rowconfigure(0, weight=1)

    # <Inicio Treeview>
    tabla = ttk.Treeview(ventana, columns=("ID", "Categoria","Monto","Descripcion","Mes","Año"), show="headings", height=15)
    tabla.heading("ID", text="ID Presupuesto")
    tabla.heading("Categoria", text="Categoria")
    tabla.heading("Monto", text="Monto")
    tabla.heading("Descripcion", text="Descripcion")
    tabla.heading("Mes", text="Mes")
    tabla.heading("Año", text="Año")

    # Configuración de columnas
    tabla.column("ID", width=80,anchor='center')
    tabla.column("Categoria", width=200,anchor='e')
    tabla.column("Monto", width=100,anchor='e')
    tabla.column("Descripcion", width=120,anchor='w')
    tabla.column("Mes", width=80,anchor='e')
    tabla.column("Año", width=80,anchor='e')

    tabla.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10)

    # Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
    categorias_dict = {c['id_categoria']: c for c in categorias}

    # Insertar datos en el Treeview
    for presupuesto in presupuestos:

        # Obtener el nombre de la categoría
        categoria_nombre = categorias_dict.get(presupuesto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')               

        tabla.insert("", "end", values=(presupuesto['id_presupuesto'], 
                                        categoria_nombre,
                                        presupuesto['monto_presupuesto'],
                                        presupuesto['descripcion'],
                                        presupuesto['mes'],
                                        presupuesto['anio']))

    # <Fin Treeview>


    # Ubicar la tabla con grid
    tabla.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Botones en la parte inferior
    boton_nuevo = tk.Button(ventana, text="Nuevo",command=lambda:pantalla_presupuesto())
    boton_nuevo.grid(row=1, column=0, pady=20, padx=10, sticky="ew")

    boton_informe = tk.Button(ventana, text="Informe")
    boton_informe.grid(row=1, column=1, pady=20, padx=10, sticky="ew")

    boton_salir = tk.Button(ventana, text="Salir", command=lambda:ventana.destroy())
    boton_salir.grid(row=1, column=2, pady=20, padx=10, sticky="ew")


    ventana.mainloop()

