import tkinter as tk
def pantalla_categoria():
    # Paso 1: Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Formulario de Categoría")
    ventana.geometry("300x150")  # Tamaño ancho x alto

    # Paso 2: Crear etiqueta "Categoría"
    etiqueta_categoria = tk.Label(ventana, text="Categoría:")
    etiqueta_categoria.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Paso 3: Crear campo de entrada de texto
    entrada_categoria = tk.Entry(ventana)
    entrada_categoria.grid(row=0, column=1, padx=10, pady=10)

    # Paso 4: Crear botón "Guardar"
    boton_guardar = tk.Button(ventana, text="Guardar")
    boton_guardar.grid(row=1, column=0, padx=10, pady=20, sticky="e")

    # Paso 5: Crear botón "Cancelar"
    boton_cancelar = tk.Button(ventana, text="Cancelar",command=lambda:ventana.destroy())
    boton_cancelar.grid(row=1, column=1, padx=10, pady=20, sticky="w")

    # Paso 6: Ejecutar la ventana
    ventana.mainloop()

