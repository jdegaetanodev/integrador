import tkinter as tk
from tkinter import ttk
from gastosfijos.pantalla import pantalla_gastosfijos

# Importar Diccionario 
from datos.gastos_fijos import gastos_fijos
from datos.categorias import categorias 


def gastosfijos_grid():
    ventana = tk.Tk()
    ventana.title("Gastos Fijos")
    ventana.geometry("950x300")

    # Contenido superior
    etiqueta = tk.Label(ventana, text="Administración de Gastos Fijos", font=("Arial", 16, "bold"))
    etiqueta.grid(row=0, column=0, columnspan=3, pady=20)

    ventana.grid_rowconfigure(0, weight=1)


    # <Inicio Treeview>
    tabla = ttk.Treeview(ventana, columns=("ID", "Categoria","Monto","Descripcion","Mes","Año","FechaPago"), show="headings", height=15)
    tabla.heading("ID", text="ID Presupuesto")
    tabla.heading("Categoria", text="Categoria")
    tabla.heading("Monto", text="Monto")
    tabla.heading("Descripcion", text="Descripcion")
    tabla.heading("Mes", text="Mes")
    tabla.heading("Año", text="Año")
    tabla.heading("FechaPago", text="Fecha Pago")

    # Configuración de columnas
    tabla.column("ID", width=80,anchor='center')
    tabla.column("Categoria", width=200,anchor='e')
    tabla.column("Monto", width=100,anchor='e')
    tabla.column("Descripcion", width=300,anchor='w')
    tabla.column("Mes", width=80,anchor='e')
    tabla.column("Año", width=80,anchor='e')
    tabla.column("FechaPago", width=80,anchor='e')

    tabla.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10)

    # Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
    categorias_dict = {c['id_categoria']: c for c in categorias}

    # Insertar datos en el Treeview

    for gasto_fijo in gastos_fijos:

        # Obtener el nombre de la categoría
        categoria_nombre = categorias_dict.get(gasto_fijo['id_categoria'], {}).get('nombre_categoria', 'Desconocida')       

        tabla.insert("", "end", values=(gasto_fijo['id_gasto_fijo'], 
                                        categoria_nombre,
                                        gasto_fijo['monto'],
                                        gasto_fijo['descripcion'],
                                        gasto_fijo['mes'],
                                        gasto_fijo['anio'],
                                        gasto_fijo['abonado'],
                                        gasto_fijo['fecha_pago']))

    # <Fin Treeview>

    # Ubicar la tabla con grid
    tabla.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")


    # Botones en la parte inferior
    boton_nuevo = tk.Button(ventana, text="Nuevo",command=lambda:pantalla_gastosfijos())
    boton_nuevo.grid(row=1, column=0, pady=20, padx=10, sticky="ew")

    boton_informe = tk.Button(ventana, text="Informe")
    boton_informe.grid(row=1, column=1, pady=20, padx=10, sticky="ew")

    boton_salir = tk.Button(ventana, text="Salir", command=lambda:ventana.destroy())
    boton_salir.grid(row=1, column=2, pady=20, padx=10, sticky="ew")


    ventana.mainloop()

