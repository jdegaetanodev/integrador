import tkinter as tk  # Importamos la librería tkinter
from gastos.grid import gastos_grid
from gastosfijos.grid import gastosfijos_grid
from presupuesto.grid import presupuesto_grid
from categorias.grid import categoria_grid


# Creamos la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Finanzas Personales")  # Título de la ventana
ventana_principal.geometry("800x350")         # Tamaño de la ventana

# Crear un frame (marco) para contener los botones horizontalmente
frame_botones = tk.Frame(ventana_principal)
frame_botones.pack(pady=100)  # Añade espacio vertical y coloca el frame en la ventana

boton_gastos = tk.Button(
    frame_botones, 
    text="GASTOS", 
    command=lambda:gastos_grid(),
    width=12,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="blue",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_gastos.pack(side="left", padx=10)

boton_gastos_fijos = tk.Button(
    frame_botones, 
    text="GASTOS FIJOS", 
    command=lambda:gastosfijos_grid(),
    width=15,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="blue",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_gastos_fijos.pack(side="left", padx=10)

boton_presupuestos = tk.Button(
    frame_botones, 
    text="PRESUPUESTOS", 
    command=lambda:presupuesto_grid(),
    width=15,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="blue",             # color de fondo
    fg="white",           # color del texto
    font=("Helvetica", 10, "bold"),
    relief="raised",      # tipo de borde
    bd=4                  # grosor del borde
)
boton_presupuestos.pack(side="left", padx=10)

boton_categorias = tk.Button(
    frame_botones, 
    text="CATEGORIAS", 
    command=lambda:categoria_grid(),
    width=15,             # ancho en caracteres
    height=2,             # alto en líneas
    bg="blue",             # color de fondo
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