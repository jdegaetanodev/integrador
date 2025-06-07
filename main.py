import tkinter as tk  # Importamos la librería tkinter

# Función que se ejecuta al hacer clic en el botón "Abrir nueva ventana"
def abrir_ventana(ventana):
    # Creamos una nueva ventana (Toplevel es una ventana secundaria de la ventana principal)
    nueva_ventana = tk.Toplevel(ventana_principal)
    
    nueva_ventana.title("Nueva Ventana")  # Título de la nueva ventana
    nueva_ventana.geometry("300x200")     # Tamaño de la nueva ventana

    # Etiqueta dentro de la nueva ventana
    etiqueta = tk.Label(nueva_ventana, text="¡Esta es una nueva ventana!")        
    etiqueta.pack(pady=20)

# Creamos la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Finanzas Personales")  # Título de la ventana
ventana_principal.geometry("800x300")         # Tamaño de la ventana

# Crear un frame (marco) para contener los botones horizontalmente
frame_botones = tk.Frame(ventana_principal)
frame_botones.pack(pady=100)  # Añade espacio vertical y coloca el frame en la ventana

boton_gastos = tk.Button(
    frame_botones, 
    text="GASTOS", 
    command=lambda:abrir_ventana("gastos"),
    width=12,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="red",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_gastos.pack(side="left", padx=10)

boton_gastos_fijos = tk.Button(
    frame_botones, 
    text="GASTOS FIJOS", 
    command=lambda:abrir_ventana("gastos_fijos"),
    width=15,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="red",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_gastos_fijos.pack(side="left", padx=10)

boton_presupuestos = tk.Button(
    frame_botones, 
    text="PRESUPUESTOS", 
    command=lambda:abrir_ventana("presupuestos"),
    width=15,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="red",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_presupuestos.pack(side="left", padx=10)

boton_categorias = tk.Button(
    frame_botones, 
    text="CATEGORIAS", 
    command=lambda:abrir_ventana("categorias"),
    width=15,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="red",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_categorias.pack(side="left", padx=10)

boton_salir = tk.Button(
    frame_botones, 
    text="SALIR", 
    command=ventana_principal.quit,
    width=12,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="#999",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_salir.pack(side="left", padx=10)



# Iniciamos el bucle principal de la interfaz gráfica
ventana_principal.mainloop()