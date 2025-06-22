import tkinter as tk  # Importamos la librería tkinter
from gastos.grid import gastos_grid
from gastosfijos.grid import gastosfijos_grid
from presupuesto.grid import presupuesto_grid
from categorias.grid import categoria_grid

# Importar utilidades de funciones
from funciones.funciones import centrar_ventana

# Para Usar imágenes en botones
from PIL import Image, ImageTk

# Creamos la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Finanzas Personales")  # Título de la ventana

centrar_ventana(ventana_principal, 800, 400)

# Cargar y redimensionar la imagen del gráfico
img_grafico = Image.open("fondo.jpg")
img_grafico = img_grafico.resize((800, 400))  # Ajustá tamaño según necesidad
img_grafico = ImageTk.PhotoImage(img_grafico)

# Colocar imagen como fondo usando un Label
label_fondo = tk.Label(ventana_principal, image=img_grafico)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
label_fondo.image = img_grafico  # mantener referencia

# Crear frame encima del fondo para contener botones
frame_botones = tk.Frame(ventana_principal, bg="", bd=0)
frame_botones.place(relx=0.5, rely=0.8, anchor="center")  # Ubicado cerca del pie


#  Imagenes para los iconos
img_categorias = Image.open("categorias.png")
img_categorias = img_categorias.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_categorias = ImageTk.PhotoImage(img_categorias)

# Crear un frame (marco) para contener los botones horizontalmente
#frame_botones = tk.Frame(ventana_principal)
#frame_botones.pack(pady=100)  # Añade espacio vertical y coloca el frame en la ventana

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

# Botón con imagen + texto (imagen arriba del texto)
boton_categorias = tk.Button(
    frame_botones, 
    text="CATEGORIAS", 
    command=lambda: categoria_grid(),
    image=img_categorias,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="blue",
    fg="white",
    font=("Helvetica", 10, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_categorias.image = img_categorias  # 🔐 Esto es necesario para que no se pierda la imagen
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