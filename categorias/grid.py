import tkinter as tk
from tkinter import ttk
from categorias.pantalla import pantalla_categoria

# Importar Diccionario
from datos.categorias import categorias

# Importar utilidades de funciones
from funciones.funciones import centrar_ventana


def categoria_grid():
    ventana = tk.Tk()
    ventana.title("Categoria")

    centrar_ventana(ventana, 430, 300)

    # Contenido superior
    etiqueta = tk.Label(ventana, text="Administración de Categorías", font=("Arial", 16, "bold"))
    etiqueta.grid(row=0, column=0, columnspan=3, pady=10)


    ventana.grid_rowconfigure(0, weight=1)

    # <Inicio Treeview>
    tabla = ttk.Treeview(ventana, columns=("ID", "Nombre"), show="headings", height=8)
    tabla.heading("ID", text="ID Categoría")
    tabla.heading("Nombre", text="Nombre Categoría")
    tabla.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10)

    # Insertar datos en el Treeview
    for categoria in categorias:
        tabla.insert("", "end", values=(categoria['id_categoria'], categoria['nombre_categoria']))

    # <Fin Treeview>

    # Botones en la parte inferior
    boton_nuevo = tk.Button(ventana, text="Nuevo",command=lambda:pantalla_categoria("add"))
    boton_nuevo.grid(row=2, column=0, pady=20, padx=10, sticky="ew")

    boton_informe = tk.Button(ventana, text="Informe")
    boton_informe.grid(row=2, column=1, pady=20, padx=10, sticky="ew")

    boton_salir = tk.Button(ventana, text="Salir", command=lambda:ventana.destroy())
    boton_salir.grid(row=2, column=2, pady=20, padx=10, sticky="ew")


    def clic_grid(event):
        item_seleccionado = tabla.focus()  # obtiene el "item ID" seleccionado
    
        if item_seleccionado:
            valores = tabla.item(item_seleccionado, "values")  # obtengo los valores de la fila
            id_categoria = valores[0]
            nombre = valores[1]

            pantalla_categoria("update", id_categoria, nombre)  # Llama a la función pantalla_categoria con los valores seleccionados

    tabla.bind("<ButtonRelease-1>", clic_grid)    


    ventana.mainloop()