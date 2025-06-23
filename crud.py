import tkinter as tk
from tkinter import ttk # Importo el TreeView
from categorias.funciones import cargar_categorias

# Funciones

def ocultar_frames():

    frame_gastos.grid_forget()
    frame_gastos_fijos.grid_forget()
    frame_presupuestos.grid_forget()
    frame_categorias.grid_forget()


def mostrar_frame(nombre_frame):

    ocultar_frames()
    nombre_frame.grid(row=0, column=0, sticky="nsew")


# Importar Diccionarios
from datos.gastos import gastos 

from categorias.funciones import cargar_categorias
categorias = cargar_categorias()

from datos.gastos_fijos import gastos_fijos
from datos.presupuesto import presupuesto_dict as presupuestos

# Funcion para centrar la ventana horizontal y verticalmente
from funciones.funciones import centrar_ventana


# Importar Gastos
from gastos.pantalla import pantalla_gastos
from categorias.pantalla import pantalla_categoria


ventana = tk.Tk()
centrar_ventana(ventana, ancho=890, alto=630)

ventana.iconbitmap("pie-chart.ico") # Asignar un icono personalizado
ventana.resizable(width=False, height=False)
ventana.title('Gestión de Gastos Personales')


frame_contenedor = tk.Frame(ventana) # El el frame que va a cargar dinamicamente los demás frames
frame_contenedor.grid(row=0, column=0, sticky="nsew")

# <-----Inicio Frame Gastos----->

frame_gastos = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_gastos, text="Gastos", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# Para Usar imágenes en botones
from PIL import Image, ImageTk

# <Inicio Treeview>
tabla_gastos = ttk.Treeview(frame_gastos, columns=("ID", "Categoria","Nombre","Monto","Detalle","Fecha"), show="headings", height=22)
tabla_gastos.heading("ID", text="ID Gasto")
tabla_gastos.heading("Categoria", text="Categoría")
tabla_gastos.heading("Nombre", text="Nombre")
tabla_gastos.heading("Monto", text="Monto")
tabla_gastos.heading("Detalle", text="Detalle")
tabla_gastos.heading("Fecha", text="Fecha")

# Configuración de columnas [w=izquierda - e=derecha]
tabla_gastos.column("ID", width=100,anchor='center')
tabla_gastos.column("Categoria", width=100,anchor='w')
tabla_gastos.column("Nombre", width=100,anchor='w')
tabla_gastos.column("Monto", width=100,anchor='e')
tabla_gastos.column("Detalle", width=200,anchor='w')
tabla_gastos.column("Fecha", width=100,anchor='e')

tabla_gastos.grid()

# Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
categorias_dict = {c['id_categoria']: c for c in categorias}

# Insertar datos en el Treeview
for gasto in gastos:

    # Obtener el nombre de la categoría
    categoria_nombre = categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')     

    tabla_gastos.insert("", "end", values=(gasto['id_gastos'], 
                                    categoria_nombre,
                                    gasto['nombre'],
                                    gasto['monto'],
                                    gasto['detalle'],
                                    gasto['fecha']))

# <Fin Treeview>


# Button Nuevo
btn_nuevo = tk.Button(  frame_gastos,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos(),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.grid(row=2, column=0, sticky="e", pady=20)
# Fin Button Nuevo

def clic_grid(event):
    item_seleccionado = tabla_gastos.focus()  # obtiene el "item ID" seleccionado

    if item_seleccionado:
        valores = tabla_gastos.item(item_seleccionado, "values")  # obtengo los valores de la fila
        id_categoria = valores[0]
        nombre = valores[1]

        pantalla_categoria("update", id_categoria, nombre)  # Llama a la función pantalla_categoria con los valores seleccionados

tabla_gastos.bind("<ButtonRelease-1>", clic_grid)    

# </-----Fin Frame Gastos----->

frame_gastos.grid(row=0, column=0, sticky="nsew")

# <-----Inicio Frame Gastos Fijos ----->

frame_gastos_fijos = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_gastos_fijos, text="Gastos Fijos", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# <Inicio Treeview>
tabla_gastos_fijos = ttk.Treeview(frame_gastos_fijos, columns=("ID", "Categoria","Monto","Descripcion","Mes","Año","FechaPago"), show="headings", height=22)
tabla_gastos_fijos.heading("ID", text="ID Presupuesto")
tabla_gastos_fijos.heading("Categoria", text="Categoria")
tabla_gastos_fijos.heading("Monto", text="Monto")
tabla_gastos_fijos.heading("Descripcion", text="Descripcion")
tabla_gastos_fijos.heading("Mes", text="Mes")
tabla_gastos_fijos.heading("Año", text="Año")
tabla_gastos_fijos.heading("FechaPago", text="Fecha Pago")

# Configuración de columnas
tabla_gastos_fijos.column("ID", width=100,anchor='center')
tabla_gastos_fijos.column("Categoria", width=100,anchor='e')
tabla_gastos_fijos.column("Monto", width=100,anchor='e')
tabla_gastos_fijos.column("Descripcion", width=250,anchor='w')
tabla_gastos_fijos.column("Mes", width=50,anchor='e')
tabla_gastos_fijos.column("Año", width=50,anchor='e')
tabla_gastos_fijos.column("FechaPago", width=50,anchor='e')

# Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
categorias_dict = {c['id_categoria']: c for c in categorias}

# Insertar datos en el Treeview

for gasto_fijo in gastos_fijos:

    # Obtener el nombre de la categoría
    categoria_nombre = categorias_dict.get(gasto_fijo['id_categoria'], {}).get('nombre_categoria', 'Desconocida')       

    tabla_gastos_fijos.insert("", "end", values=(gasto_fijo['id_gasto_fijo'], 
                                    categoria_nombre,
                                    gasto_fijo['monto'],
                                    gasto_fijo['descripcion'],
                                    gasto_fijo['mes'],
                                    gasto_fijo['anio'],
                                    gasto_fijo['abonado'],
                                    gasto_fijo['fecha_pago']))

# <Fin Treeview>

# Ubicar la tabla con grid
tabla_gastos_fijos.grid()

# Button Nuevo
btn_nuevo = tk.Button(  frame_gastos_fijos,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos(),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.grid(row=2, column=0, sticky="e", pady=20)
# Fin Button Nuevo


# <-----Fin Frame Gastos Fijos ----->


# <-----Inicio Frame Categorias ----->

frame_categorias = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_categorias, text="Categorias", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# <Inicio Treeview>
tabla_categorias = ttk.Treeview(frame_categorias, columns=("ID", "Nombre"), show="headings", height=22)
tabla_categorias.heading("ID", text="ID Categoría")
tabla_categorias.heading("Nombre", text="Nombre Categoría")

# Configuración de columnas
tabla_categorias.column("ID", width=100,anchor='center')
tabla_categorias.column("Nombre", width=600,anchor='w')

# Insertar datos en el Treeview
for categoria in categorias:
    tabla_categorias.insert("", "end", values=(categoria['id_categoria'], categoria['nombre_categoria']))

# <Fin Treeview>

# Ubicar la tabla con grid
tabla_categorias.grid()

def actualizar_tabla_categorias():

    print("Actualizando tabla de categorías...")

    # 1. Borrar todo lo que tiene actualmente
    for fila in tabla_categorias.get_children():
        tabla_categorias.delete(fila)

    # 2. Volver a cargar desde el JSON
    categorias_actualizadas = cargar_categorias()
    print("Categorías cargadas:", categorias_actualizadas)  # <- DEBUG    

    # 3. Insertar las categorías nuevamente
    for categoria in categorias_actualizadas:
        tabla_categorias.insert("", "end", values=(categoria['id_categoria'], categoria['nombre_categoria']))
        print(f"Insertando categoría: {categoria['id_categoria']} - {categoria['nombre_categoria']}")


def clic_grid(event):
    tabla_categorias.after(100, procesar_click)  # Espera 100 ms antes de procesar

def procesar_click():
    item_seleccionado = tabla_categorias.focus()  # obtiene el "item ID" seleccionado

    if item_seleccionado:
        valores = tabla_categorias.item(item_seleccionado, "values")  # obtengo los valores de la fila
        id_categoria = valores[0]
        nombre = valores[1]

        pantalla_categoria("update", id_categoria, nombre, callback_actualizar=actualizar_tabla_categorias)  # Llama a la función pantalla_categoria con los valores seleccionados

# tabla.bind("<ButtonRelease-1>", clic_grid)     

tabla_categorias.bind("<<TreeviewSelect>>", clic_grid)

# Button Nuevo
btn_nuevo = tk.Button(  frame_categorias,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_categoria("add"),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.grid(row=2, column=0, sticky="e", pady=20)
# Fin Button Nuevo

# <-----Fin Frame Categorias ----->


# <-----Inicio Frame Presupuestos ----->

frame_presupuestos = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_presupuestos, text="Presupuestos", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# <Inicio Treeview>
tabla_presupuestos = ttk.Treeview(frame_presupuestos, columns=("ID", "Categoria","Monto","Descripcion","Mes","Año"), show="headings", height=22)
tabla_presupuestos.heading("ID", text="ID Presupuesto")
tabla_presupuestos.heading("Categoria", text="Categoria")
tabla_presupuestos.heading("Monto", text="Monto")
tabla_presupuestos.heading("Descripcion", text="Descripcion")
tabla_presupuestos.heading("Mes", text="Mes")
tabla_presupuestos.heading("Año", text="Año")

# Configuración de columnas
tabla_presupuestos.column("ID", width=80,anchor='center')
tabla_presupuestos.column("Categoria", width=200,anchor='e')
tabla_presupuestos.column("Monto", width=100,anchor='e')
tabla_presupuestos.column("Descripcion", width=120,anchor='w')
tabla_presupuestos.column("Mes", width=100,anchor='e')
tabla_presupuestos.column("Año", width=100,anchor='e')


# Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
categorias_dict = {c['id_categoria']: c for c in categorias}

# Insertar datos en el Treeview
for presupuesto in presupuestos:

    # Obtener el nombre de la categoría
    categoria_nombre = categorias_dict.get(presupuesto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')               

    tabla_presupuestos.insert("", "end", values=(presupuesto['id_presupuesto'], 
                                    categoria_nombre,
                                    presupuesto['monto_presupuesto'],
                                    presupuesto['descripcion'],
                                    presupuesto['mes'],
                                    presupuesto['anio']))
    

tabla_presupuestos.grid()

# <Fin Treeview>

# Button Nuevo
btn_nuevo = tk.Button(  frame_presupuestos,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos(),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.grid(row=2, column=0, sticky="e", pady=20)
# Fin Button Nuevo


# <-----Fin Frame Presupuestos ----->


# Frame para los botones
frame_botones = tk.Frame(frame_contenedor, padx=10, pady=10)
frame_botones.grid(row=0, column=2,rowspan=5)

# Botón Gastos
#  Imagenes para los iconos
img_gastos = Image.open("wallet.png")
img_gastos = img_gastos.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_gastos = ImageTk.PhotoImage(img_gastos)

boton_gastos = tk.Button(
    frame_botones, 
    width=70,
    height=70,
    text="GASTOS", 
    command=lambda: mostrar_frame(frame_gastos),
    image=img_gastos,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="#B57EDC",
    fg="white",
    font=("Helvetica", 8, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_gastos.image = img_gastos  # Esto es necesario para que no se pierda la imagen
boton_gastos.pack( padx=10,pady=10)

# Fin Botón gastos


# Botón categoria

#  Imagenes para los iconos
img_categorias = Image.open("categorias.png")
img_categorias = img_categorias.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_categorias = ImageTk.PhotoImage(img_categorias)

boton_categorias = tk.Button(
    frame_botones,
    width=70,
    height=70, 
    text="CATEGORIAS", 
    command=lambda: mostrar_frame(frame_categorias),
    image=img_categorias,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="#B57EDC",
    fg="white",
    font=("Helvetica", 8, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_categorias.image = img_categorias  # Esto es necesario para que no se pierda la imagen
boton_categorias.pack( padx=10)

# Fin Botón categoria

# Botón Gastos fijos

#  Imagenes para los iconos
img_gastosfijos = Image.open("money.png")
img_gastosfijos = img_gastosfijos.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_gastosfijos = ImageTk.PhotoImage(img_gastosfijos)

boton_gastosfijos = tk.Button(
    frame_botones, 
    width=70,
    height=70,
    text="GASTOS FIJOS", 
    command=lambda: mostrar_frame(frame_gastos_fijos),
    image=img_gastosfijos,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="#B57EDC",
    fg="white",
    font=("Helvetica", 8, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_gastosfijos.image = img_gastosfijos  # Esto es necesario para que no se pierda la imagen
boton_gastosfijos.pack( padx=10,pady=10)

# Fin Botón Gastosfijos


# Botón presupuesto
#  Imagenes para los iconos
img_presupuesto = Image.open("budget.png")
img_presupuesto = img_presupuesto.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_presupuesto = ImageTk.PhotoImage(img_presupuesto)

boton_presupuesto = tk.Button(
    frame_botones, 
    width=70,
    height=70,
    text="PRESUPUESTO", 
    command=lambda: mostrar_frame(frame_presupuestos),
    image=img_presupuesto,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="#B57EDC",
    fg="white",
    font=("Helvetica", 8, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_presupuesto.image = img_presupuesto  # Esto es necesario para que no se pierda la imagen
boton_presupuesto.pack( padx=10,pady=10)

# Fin Botón presupuesto

# Botón salir
#  Imagenes para los iconos
img_salir = Image.open("exit.png")
img_salir = img_salir.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_salir = ImageTk.PhotoImage(img_salir)

boton_salir = tk.Button(
    frame_botones, 
    width=70,
    height=70,
    text="SALIR", 
    command=lambda: quit(),
    image=img_salir,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="#B57EDC",
    fg="white",
    font=("Helvetica", 8, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_salir.image = img_salir  # Esto es necesario para que no se pierda la imagen
boton_salir.pack( padx=10,pady=10)

# Fin Botón salir


# Iniciamos el bucle principal de la interfaz gráfica
ventana.mainloop()