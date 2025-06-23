import tkinter as tk
from categorias.funciones import add_categoria,update_categoria

def pantalla_categoria(accion, id= 0, nombre='', callback_actualizar=None): # accion = add | update - id es opcional, solo se usa en update

    # Importar utilidades de funciones
    from funciones.funciones import centrar_ventana

    # Paso 1: Crear la ventana principal
    #ventana_categoria = tk.Tk()
    ventana_categoria = tk.Toplevel()
    ventana_categoria.title("Formulario de Categoría")

    centrar_ventana(ventana_categoria, 300, 150)

    etiqueta_categoria = tk.Label(ventana_categoria, text="Categoría:")
    etiqueta_categoria.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entrada_categoria = tk.Entry(ventana_categoria)
    entrada_categoria.grid(row=0, column=1, padx=10, pady=10)

    entrada_categoria.insert(0, nombre)  # Si es update, muestra el nombre de la categoría

    # Última fila de la ventana
    botonera = tk.Frame(ventana_categoria)
    botonera.grid(row=99, column=0, columnspan=2, sticky="e", pady=10, padx=10)

    btn_cancelar = tk.Button(botonera, text="Cancelar",command=lambda:ventana_categoria.destroy())

    if accion == "add":
        btn_guardar = tk.Button(botonera, text="Guardar",command=lambda:add_categoria(entrada_categoria.get(), ventana_categoria, callback_actualizar))
        print("Agregar nueva categoría")
    else:
        btn_guardar = tk.Button(botonera, text="Guardar",command=lambda:update_categoria(id, entrada_categoria.get(),ventana_categoria, callback_actualizar))
        print("Actualizar categoría existente")

    # Mostrar botones    
    btn_guardar.pack(side="right", padx=5)
    btn_cancelar.pack(side="right")

    # Paso 6: Ejecutar la ventana
    ventana_categoria.mainloop()