import tkinter as tk
from categorias.funciones import guardar_categoria


def pantalla_categoria():
    # Paso 1: Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Formulario de Categoría")
    ventana.geometry("300x150")  # Tamaño ancho x alto

    etiqueta_categoria = tk.Label(ventana, text="Categoría:")
    etiqueta_categoria.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entrada_categoria = tk.Entry(ventana)
    entrada_categoria.grid(row=0, column=1, padx=10, pady=10)

    boton_cancelar = tk.Button(ventana, text="Cancelar",command=lambda:ventana.destroy())
    boton_cancelar.grid(row=1, column=0, padx=10, pady=20, sticky="w")

    boton_guardar = tk.Button(ventana, text="Guardar",command=lambda:guardar_categoria())
    #boton_guardar = tk.Button(ventana, text="Guardar",command=lambda:guardar_categoria(entrada_categoria.get()))
    boton_guardar.grid(row=1, column=1, padx=10, pady=20, sticky="e")


    # Paso 6: Ejecutar la ventana
    ventana.mainloop()


def pantalla_categoria_edicion(id, nombre):
    # Paso 1: Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Formulario de Categoría")
    ventana.geometry("300x150")  # Tamaño ancho x alto

    etiqueta_categoria = tk.Label(ventana, text="Categoría:")
    etiqueta_categoria.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entrada_categoria = tk.Entry(ventana)
    entrada_categoria.grid(row=0, column=1, padx=10, pady=10)
    entrada_categoria.insert(0, nombre)  # Insertar el nombre de la categoría en el campo de entrada

    boton_cancelar = tk.Button(ventana, text="Cancelar",command=lambda:ventana.destroy())
    boton_cancelar.grid(row=1, column=0, padx=10, pady=20, sticky="w")

    boton_guardar = tk.Button(ventana, text="Guardar",command=lambda:guardar_categoria())

    # boton_guardar = tk.Button(ventana, text="Guardar",command=lambda:guardar_categoria_edicion(id, entrada_categoria.get()))

    boton_guardar.grid(row=1, column=1, padx=10, pady=20, sticky="e")


    # Paso 6: Ejecutar la ventana
    ventana.mainloop()    

