import tkinter as tk
from tkinter import ttk
from gastosfijos.pantalla import pantalla_gastosfijos
def gastosfijos_grid():
    ventana = tk.Tk()
    ventana.title("Gastos Fijos")
    ventana.geometry("650x300")

    # Contenido superior
    etiqueta = tk.Label(ventana, text="Contenido en la parte superior")
    #etiqueta.grid(row=0, column=0, columnspan=3, pady=20)

    ventana.grid_rowconfigure(0, weight=1)

    # Crear Treeview (como una tabla)
    columnas = ("Nombre", "Edad", "Email")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

    # Definir encabezados
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")

    # Agregar filas de ejemplo
    tabla.insert("", tk.END, values=("Ana", 30, "ana@email.com"))
    tabla.insert("", tk.END, values=("Carlos", 25, "carlos@email.com"))

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

