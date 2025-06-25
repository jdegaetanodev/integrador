import tkinter as tk
from tkinter import ttk # Importo el TreeView
from categorias.funciones import cargar_categorias
import os
import matplotlib.pyplot as plt # Libreria para gráficos

# Funciones

def ocultar_frames():

    frame_gastos.grid_forget()
    frame_gastos_fijos.grid_forget()
    frame_presupuestos.grid_forget()
    frame_categorias.grid_forget()
    frame_reportes.grid_forget()


def mostrar_frame(nombre_frame):

    ocultar_frames()
    nombre_frame.grid(row=0, column=0, sticky="nsew")


# Funcion para centrar la ventana horizontal y verticalmente
from funciones.funciones import centrar_ventana

# Importar funciones para exportar
from categorias.funciones import exportar_categorias
from gastos.funciones import exportar_gastos
from gastosfijos.funciones import exportar_gastos_fijos
from presupuesto.funciones import exportar_presupuesto

# Importar pantallas
from gastos.pantalla import pantalla_gastos
from categorias.pantalla import pantalla_categoria
from gastosfijos.pantalla import pantalla_gastosfijos

# Cargar datos desde funciones JSON
from gastos.funciones import cargar_gastos
from gastosfijos.funciones import cargar_gastosfijos
from categorias.funciones import cargar_categorias
from presupuesto.funciones import cargar_presupuestos

categorias = cargar_categorias()
gastos = cargar_gastos()
gastos_fijos = cargar_gastosfijos()
presupuestos = cargar_presupuestos()

# Para Usar imágenes en botones
from PIL import Image, ImageTk

# ventana principal
ventana = tk.Tk()
centrar_ventana(ventana, ancho=890, alto=710)

ruta_icono = os.path.join("imagenes", "pie-chart.ico")
ventana.iconbitmap(ruta_icono)

ventana.resizable(width=False, height=False)
ventana.title('Gestión de Gastos Personales')

frame_contenedor = tk.Frame(ventana)
frame_contenedor.grid(row=0, column=0, sticky="nsew")

frame_contenedor.lift()

# <-----Inicio Frame Gastos----->

frame_gastos = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_gastos, text="Gastos", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, columnspan=5,column=0, sticky="w", padx=0)


# <Inicio Treeview>
tabla_gastos = ttk.Treeview(frame_gastos, columns=("ID", "IdCat", "Categoria","Nombre","Monto","Detalle","Fecha"), show="headings", height=26)
tabla_gastos.heading("ID", text="ID Gasto")
tabla_gastos.heading("IdCat", text="Id Cat")
tabla_gastos.heading("Categoria", text="Categoría")
tabla_gastos.heading("Nombre", text="Nombre")
tabla_gastos.heading("Monto", text="Monto")
tabla_gastos.heading("Detalle", text="Detalle")
tabla_gastos.heading("Fecha", text="Fecha")

# Configuración de columnas [w=izquierda - e=derecha]
tabla_gastos.column("ID", width=50,anchor='center')
tabla_gastos.column("IdCat", width=50, anchor='center')
tabla_gastos.column("Categoria", width=120,anchor='w')
tabla_gastos.column("Nombre", width=120,anchor='w')
tabla_gastos.column("Monto", width=80,anchor='e')
tabla_gastos.column("Detalle", width=200,anchor='w')
tabla_gastos.column("Fecha", width=80,anchor='e')

tabla_gastos.grid()

# Paso importante: Convertir la lista de categorías a un diccionario para acceso rápido
categorias_dict = {c['id_categoria']: c for c in categorias}

# Insertar datos en el Treeview
for gasto in gastos:

    # Obtener el nombre de la categoría
    categoria_nombre = categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')     

    tabla_gastos.insert("", "end", values=(gasto['id_gastos'], 
                                    gasto['id_categoria'],
                                    categoria_nombre,
                                    gasto['nombre'],
                                    gasto['monto'],
                                    gasto['descripcion'],
                                    gasto['fecha']))

# <Fin Treeview>

# Crear un frame para agrupar los botones a la derecha
frame_botones_gastos = tk.Frame(frame_gastos)
frame_botones_gastos.grid(row=2, column=0, sticky="e", pady=20)


# Button Exportar Gasto
btn_exportar = tk.Button(  frame_botones_gastos,
                            width=15,
                            height=2,
                            text="EXPORTAR",
                            command=lambda: exportar_gastos(),
                            bg="#9D9BB5",
                            fg="white",
                            font=("Helvetica", 10, "bold"),
                            relief="raised")

btn_exportar.pack(side="left", padx=(0, 10))  # Espacio a la derecha
# Fin Button Exportar Gasto

# Button Nuevo
btn_nuevo = tk.Button(  frame_botones_gastos,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos("add", callback_actualizar=actualizar_tabla_gastos),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.pack(side="left")
# Fin Button Nuevo

def actualizar_tabla_gastos():

    # 1. Borrar todo lo que tiene actualmente
    for fila in tabla_gastos.get_children():
        tabla_gastos.delete(fila)

    # 2. Volver a cargar desde el JSON
    gastos_actualizados = cargar_gastos()

    # 3. Insertar los gastos nuevamente
    for gasto in gastos_actualizados:

        # Obtener el nombre de la categoría
        categoria_nombre = categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')     

        tabla_gastos.insert("", "end", values=(gasto['id_gastos'], 
                                        gasto['id_categoria'],
                                        categoria_nombre,
                                        gasto['nombre'],
                                        gasto['monto'],
                                        gasto['descripcion'],
                                        gasto['fecha']))


def clic_grid_gastos(event):
    item_seleccionado = tabla_gastos.focus()  # obtiene el "item ID" seleccionado

    if item_seleccionado:
        valores = tabla_gastos.item(item_seleccionado, "values")  # obtengo los valores de la fila
        
        print(valores)

        id_gasto = valores[0]
        id_categoria = valores[1]
        nombre = valores[3]        
        monto = valores[4]
        detalle = valores[5]
        fecha = valores[6]

        pantalla_gastos(
            accion="update",
            id_gasto=id_gasto,
            id_categoria=id_categoria,
            nombre=nombre,
            monto=monto,
            detalle=detalle,
            fecha=fecha,
            callback_actualizar=actualizar_tabla_gastos)        

tabla_gastos.bind("<ButtonRelease-1>", clic_grid_gastos)    

# </-----Fin Frame Gastos----->

#frame_gastos.grid(row=0, column=0, sticky="nsew")

# <-----Inicio Frame Gastos Fijos ----->

frame_gastos_fijos = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_gastos_fijos, text="Gastos Fijos", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# <Inicio Treeview>
tabla_gastos_fijos = ttk.Treeview(frame_gastos_fijos, columns=("ID", "Categoria","Monto","Descripcion","Mes","Año","Pago","FechaPago"), show="headings", height=26)
tabla_gastos_fijos.heading("ID", text="ID Gasto")
tabla_gastos_fijos.heading("Categoria", text="Id Cat")
tabla_gastos_fijos.heading("Monto", text="Monto")
tabla_gastos_fijos.heading("Descripcion", text="Descrip")
tabla_gastos_fijos.heading("Mes", text="Mes")
tabla_gastos_fijos.heading("Año", text="Año")
tabla_gastos_fijos.heading("Pago", text="Pago")
tabla_gastos_fijos.heading("FechaPago", text="Fecha Pago")

# Configuración de columnas
tabla_gastos_fijos.column("ID", width=80,anchor='center')
tabla_gastos_fijos.column("Categoria", width=100,anchor='w')
tabla_gastos_fijos.column("Monto", width=100,anchor='e')
tabla_gastos_fijos.column("Descripcion", width=200,anchor='w')
tabla_gastos_fijos.column("Mes", width=50,anchor='e')
tabla_gastos_fijos.column("Año", width=50,anchor='e')
tabla_gastos_fijos.column("Pago", width=50,anchor='center')
tabla_gastos_fijos.column("FechaPago", width=70,anchor='e')

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

# Crear un frame para agrupar los botones a la derecha
frame_botones_gastos_fijos = tk.Frame(frame_gastos_fijos)
frame_botones_gastos_fijos.grid(row=2, column=0, sticky="e", pady=20)


# Button Exportar Gasto
btn_exportar = tk.Button(  frame_botones_gastos_fijos,
                            width=15,
                            height=2,
                            text="EXPORTAR",
                            command=lambda: exportar_gastos_fijos(),
                            bg="#9D9BB5",
                            fg="white",
                            font=("Helvetica", 10, "bold"),
                            relief="raised")

btn_exportar.pack(side="left", padx=(0, 10))  # Espacio a la derecha
# Fin Button Exportar Gasto

# Button Nuevo
btn_nuevo = tk.Button(  frame_botones_gastos_fijos,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos("add", callback_actualizar=actualizar_tabla_gastos_fijos),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.pack(side="left")
# Fin Button Nuevo


def actualizar_tabla_gastos_fijos():
    for fila in tabla_gastos_fijos.get_children():
        tabla_gastos_fijos.delete(fila)

    gastosfijos_actualizados = cargar_gastosfijos()

    for gasto_fijo in gastosfijos_actualizados:
        categoria_nombre = categorias_dict.get(gasto_fijo['id_categoria'], {}).get('nombre_categoria', 'Desconocida')
        tabla_gastos_fijos.insert("", "end", values=(
            gasto_fijo['id_gasto_fijo'],
            categoria_nombre,
            gasto_fijo['monto'],
            gasto_fijo['descripcion'],
            gasto_fijo['mes'],
            gasto_fijo['anio'],
            gasto_fijo['abonado'],
            gasto_fijo['fecha_pago']
        ))


def clic_grid_gastos_fijos(event):
    item_seleccionado = tabla_gastos_fijos.focus()
    if item_seleccionado:
        valores = tabla_gastos_fijos.item(item_seleccionado, "values")
        id_gasto_fijo = valores[0]
        nombre_categoria = valores[1]
        monto = valores[2]
        descripcion = valores[3]
        mes = valores[4]
        anio = valores[5]
        abonado = valores[6]
        fecha_pago = valores[7]

        # Buscar ID de categoría por nombre
        id_categoria = next((k for k, v in categorias_dict.items() if v['nombre_categoria'] == nombre_categoria), None)

        pantalla_gastosfijos(
            accion="update",
            id_gasto_fijo=id_gasto_fijo,
            id_categoria=id_categoria,
            nombre_categoria=nombre_categoria,
            monto=monto,
            descripcion=descripcion,
            mes=mes,
            anio=anio,
            abonado=abonado,
            fecha_pago=fecha_pago,
            callback_actualizar=actualizar_tabla_gastos_fijos
        )

# VINCULAR EL EVENTO AL TREEVIEW
tabla_gastos_fijos.bind("<ButtonRelease-1>", clic_grid_gastos_fijos)

# <-----Fin Frame Gastos Fijos ----->


# <-----Inicio Frame Categorias ----->

frame_categorias = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_categorias, text="Categorias", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# <Inicio Treeview>
tabla_categorias = ttk.Treeview(frame_categorias, columns=("ID", "Nombre"), show="headings", height=26)
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

    # 1. Borrar todo lo que tiene actualmente
    for fila in tabla_categorias.get_children():
        tabla_categorias.delete(fila)

    # 2. Volver a cargar desde el JSON
    categorias_actualizadas = cargar_categorias()

    # 3. Insertar las categorías nuevamente
    for categoria in categorias_actualizadas:
        tabla_categorias.insert("", "end", values=(categoria['id_categoria'], categoria['nombre_categoria']))


def clic_grid(event):
    tabla_categorias.after(100, procesar_click)  # Espera 100 ms antes de procesar

def procesar_click():
    item_seleccionado = tabla_categorias.focus()  # obtiene el "item ID" seleccionado

    if item_seleccionado:
        valores = tabla_categorias.item(item_seleccionado, "values")  # obtengo los valores de la fila
        id_categoria = valores[0]
        nombre = valores[1]

        pantalla_categoria("update", id_categoria, nombre, callback_actualizar=actualizar_tabla_categorias)  # Llama a la función pantalla_categoria con los valores seleccionados

tabla_categorias.bind("<<TreeviewSelect>>", clic_grid)

# Crear un frame para agrupar los botones a la derecha
frame_botones_categorias = tk.Frame(frame_categorias)
frame_botones_categorias.grid(row=2, column=0, sticky="e", pady=20)

# Button Exportar Categorias
btn_exportar = tk.Button(  frame_botones_categorias,
                            width=15,
                            height=2,
                            text="EXPORTAR",
                            command=lambda: exportar_categorias(),
                            bg="#9D9BB5",
                            fg="white",
                            font=("Helvetica", 10, "bold"),
                            relief="raised")

btn_exportar.pack(side="left", padx=(0, 10))  # Espacio a la derecha
# Fin Button Exportar Categorias

# Button Nuevo
btn_nuevo = tk.Button(  frame_botones_categorias,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos("add", callback_actualizar=actualizar_tabla_categorias),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.pack(side="left")
# Fin Button Nuevo



# <-----Fin Frame Categorias ----->

frame_categorias.grid(row=0, column=0, sticky="nsew")



# <-----Inicio Frame Presupuestos ----->

frame_presupuestos = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_presupuestos, text="Presupuestos", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

# <Inicio Treeview>
tabla_presupuestos = ttk.Treeview(frame_presupuestos, columns=("ID", "Categoria","Monto","Descripcion","Mes","Año"), show="headings", height=26)
tabla_presupuestos.heading("ID", text="ID Presupuesto")
tabla_presupuestos.heading("Categoria", text="Categoria")
tabla_presupuestos.heading("Monto", text="Monto")
tabla_presupuestos.heading("Descripcion", text="Descripcion")
tabla_presupuestos.heading("Mes", text="Mes")
tabla_presupuestos.heading("Año", text="Año")

# Configuración de columnas
tabla_presupuestos.column("ID", width=80,anchor='center')
tabla_presupuestos.column("Categoria", width=200,anchor='w')
tabla_presupuestos.column("Monto", width=100,anchor='e')
tabla_presupuestos.column("Descripcion", width=220,anchor='w')
tabla_presupuestos.column("Mes", width=50,anchor='e')
tabla_presupuestos.column("Año", width=50,anchor='e')


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

# Crear un frame para agrupar los botones a la derecha
frame_botones_presupuestos = tk.Frame(frame_presupuestos)
frame_botones_presupuestos.grid(row=2, column=0, sticky="e", pady=20)

# Button Exportar Presupuestos
btn_exportar = tk.Button(  frame_botones_presupuestos,
                            width=15,
                            height=2,
                            text="EXPORTAR",
                            command=lambda: exportar_presupuesto(),
                            bg="#9D9BB5",
                            fg="white",
                            font=("Helvetica", 10, "bold"),
                            relief="raised")

btn_exportar.pack(side="left", padx=(0, 10))  # Espacio a la derecha
# Fin Button Exportar Presupuestos

# Button Nuevo
btn_nuevo = tk.Button(  frame_botones_presupuestos,
                        width=15,
                        height=2,
                        text="NUEVO",
                        command=lambda: pantalla_gastos("add", callback_actualizar=actualizar_tabla_presupuestos),
                        bg="#B57EDC",
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        relief="raised")

btn_nuevo.pack(side="left")
# Fin Button Nuevo



def actualizar_tabla_presupuestos():
    from presupuesto.funciones import cargar_presupuestos
    presupuestos_actualizados = cargar_presupuestos()

    for fila in tabla_presupuestos.get_children():
        tabla_presupuestos.delete(fila)

    for presupuesto in presupuestos_actualizados:
        categoria_nombre = categorias_dict.get(presupuesto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')
        tabla_presupuestos.insert("", "end", values=(
            presupuesto['id_presupuesto'],
            categoria_nombre,
            presupuesto['monto_presupuesto'],
            presupuesto['descripcion'],
            presupuesto['mes'],
            presupuesto['anio']
        ))

from presupuesto.pantalla import pantalla_presupuesto

def clic_grid_presupuestos(event):
    item = tabla_presupuestos.focus()
    if item:
        valores = tabla_presupuestos.item(item, "values")
        id_presupuesto = valores[0]
        nombre_categoria = valores[1]
        monto = valores[2]
        descripcion = valores[3]
        mes = valores[4]
        anio = valores[5]

        # Buscar ID de categoría por nombre
        id_categoria = next((k for k, v in categorias_dict.items() if v['nombre_categoria'] == nombre_categoria), None)

        pantalla_presupuesto(
            accion="update",
            id_presupuesto=id_presupuesto,
            id_categoria=id_categoria,
            monto_presupuesto=monto,
            descripcion=descripcion,
            mes=mes,
            anio=anio,
            callback_actualizar=actualizar_tabla_presupuestos
        )

tabla_presupuestos.bind("<ButtonRelease-1>", clic_grid_presupuestos)


# <-----Fin Frame Presupuestos ----->


# <-----Inicio Frame Reportes ----->

frame_reportes = tk.Frame(frame_contenedor, padx=20, pady=20)

label = tk.Label(frame_reportes, text="Reportes", pady="15",anchor="w",font=("Helvetica", 12, "bold"))
label.grid(row=0, column=0, sticky="w", padx=0)

frame_filtros = tk.Frame(frame_reportes, padx=0, pady=20)
frame_filtros.grid(row=1, column=0, sticky="nsew")

# --- Campo Categoría ---
label_categoria = tk.Label(frame_filtros, text="Categoría:")
label_categoria.grid(row=0, column=0, padx=5)

# Completar el ComboBox
mapa_categorias = {}

for categoria in categorias:     
    mapa_categorias[categoria["nombre_categoria"]] = categoria["id_categoria"]

# Agregar la opción "Todas" al inicio
valores_categorias = ["Todas"] + list(mapa_categorias.keys())

combo_categoria = ttk.Combobox(frame_filtros, width=25, values=list(mapa_categorias.keys()))

combo_categoria.grid(row=0, column=1, padx=5)
combo_categoria.set("Todas")

# Fin Completar el ComboBox


# --- Campo Año ---
label_anio = tk.Label(frame_filtros, text="Año:")
label_anio.grid(row=0, column=2, padx=5)
combo_anio = ttk.Combobox(frame_filtros, values=["Todos", "2024", "2025"])
combo_anio.grid(row=0, column=3, padx=5)
combo_anio.set("2025")

# --- Campo Mes ---
label_mes = tk.Label(frame_filtros, text="Mes:")
label_mes.grid(row=0, column=4, padx=5)
combo_mes = ttk.Combobox(frame_filtros, values=["Todos"] + [str(m) for m in range(1, 13)])
combo_mes.grid(row=0, column=5, padx=5)
combo_mes.set("1")

# --- Botón Filtrar ---
btn_filtrar = tk.Button(frame_filtros, text="Filtrar", command=lambda: mostrar_reportes())
btn_filtrar.grid(row=0, column=6, padx=10)


# <Inicio Treeview>
tabla_reportes = ttk.Treeview(frame_reportes, columns=("ID", "IdCat", "Categoria","Nombre","Monto","Detalle","Fecha"), show="headings", height=15)
tabla_reportes.heading("ID", text="ID Gasto")
tabla_reportes.heading("IdCat", text="Id Cat")
tabla_reportes.heading("Categoria", text="Categoría")
tabla_reportes.heading("Nombre", text="Nombre")
tabla_reportes.heading("Monto", text="Monto")
tabla_reportes.heading("Detalle", text="Detalle")
tabla_reportes.heading("Fecha", text="Fecha")

# Configuración de columnas [w=izquierda - e=derecha]
tabla_reportes.column("ID", width=50,anchor='center')
tabla_reportes.column("IdCat", width=50, anchor='center')
tabla_reportes.column("Categoria", width=120,anchor='w')
tabla_reportes.column("Nombre", width=120,anchor='w')
tabla_reportes.column("Monto", width=80,anchor='e')
tabla_reportes.column("Detalle", width=200,anchor='w')
tabla_reportes.column("Fecha", width=80,anchor='e')

from datetime import datetime


def mostrar_reportes():
    for fila in tabla_reportes.get_children():
        tabla_reportes.delete(fila)

    categoria_seleccionada = combo_categoria.get()
    anio_seleccionado = combo_anio.get()
    mes_seleccionado = combo_mes.get()

    total = 0

    for gasto in gastos:
        try:
            fecha_gasto = datetime.strptime(gasto["fecha"], "%d/%m/%Y")
        except ValueError:
            continue

        anio_gasto = str(fecha_gasto.year)
        mes_gasto = str(fecha_gasto.month)

        anio_valido = (anio_seleccionado == "Todos" or anio_gasto == anio_seleccionado)
        mes_valido = (mes_seleccionado == "Todos" or mes_gasto == mes_seleccionado)

        categoria_valida = (
            categoria_seleccionada == "Todas"
            or categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria') == categoria_seleccionada
        )

        if categoria_valida and anio_valido and mes_valido:
            categoria_nombre = categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')
            tabla_reportes.insert("", "end", values=(
                gasto['id_gastos'],
                gasto['id_categoria'],
                categoria_nombre,
                gasto['nombre'],
                gasto['monto'],
                gasto['descripcion'],
                gasto['fecha']
            ))
            total += float(gasto['monto'])

    # Intentando mostrar el grafico !!!!
    # Datos para el gráfico
    distribucion = {}

    for gasto in gastos:
        try:
            fecha_gasto = datetime.strptime(gasto["fecha"], "%d/%m/%Y")
        except ValueError:
            continue

        anio_gasto = str(fecha_gasto.year)
        mes_gasto = str(fecha_gasto.month)

        anio_valido = (anio_seleccionado == "Todos" or anio_gasto == anio_seleccionado)
        mes_valido = (mes_seleccionado == "Todos" or mes_gasto == mes_seleccionado)

        categoria_valida = (
            categoria_seleccionada == "Todas"
            or categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria') == categoria_seleccionada
        )

        if categoria_valida and anio_valido and mes_valido:
            cat = categorias_dict.get(gasto['id_categoria'], {}).get('nombre_categoria', 'Desconocida')
            monto = float(gasto['monto'])
            distribucion[cat] = distribucion.get(cat, 0) + monto

    # Mostrar gráfico si hay datos
    if distribucion:
        categorias = list(distribucion.keys())
        montos = list(distribucion.values())

        plt.figure(figsize=(7, 7))
        plt.pie(montos, labels=categorias, autopct='%1.1f%%', startangle=90)
        plt.title("Distribución de Gastos por Categoría")
        plt.axis('equal')  # Para que sea circular
        plt.show()
        # Fin Intentando mostrar el grafico !!!!



    total_label = tk.Label(frame_reportes, text=f"Total: $ {total:.2f}")
    total_label.grid(row=5, column=0, padx=10, pady=20, sticky="w")


tabla_reportes.grid()

# <-----Fin Frame Reportes ----->


# Frame para los botones
frame_botones = tk.Frame(frame_contenedor, padx=10, pady=10)
frame_botones.grid(row=0, column=2,rowspan=5)

# Botón Gastos
#  Imagenes para los iconos
ruta_imagen = os.path.join("imagenes", "wallet.png")
img_gastos = Image.open(ruta_imagen)

img_gastos = img_gastos.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_gastos = ImageTk.PhotoImage(img_gastos)

boton_gastos = tk.Button(
    frame_botones, 
    width=70,
    height=63,
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
ruta_imagen = os.path.join("imagenes", "categorias.png")
img_categorias = Image.open(ruta_imagen)

img_categorias = img_categorias.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_categorias = ImageTk.PhotoImage(img_categorias)

boton_categorias = tk.Button(
    frame_botones,
    width=70,
    height=63, 
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
ruta_imagen = os.path.join("imagenes", "money.png")
img_gastosfijos = Image.open(ruta_imagen)

img_gastosfijos = img_gastosfijos.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_gastosfijos = ImageTk.PhotoImage(img_gastosfijos)

boton_gastosfijos = tk.Button(
    frame_botones, 
    width=70,
    height=63,
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
ruta_imagen = os.path.join("imagenes", "budget.png")
img_presupuesto = Image.open(ruta_imagen)

img_presupuesto = img_presupuesto.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_presupuesto = ImageTk.PhotoImage(img_presupuesto)

boton_presupuesto = tk.Button(
    frame_botones, 
    width=70,
    height=63,
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

# Botón presupuesto
#  Imagenes para los iconos
ruta_imagen = os.path.join("imagenes", "report.png")
img_reportes = Image.open(ruta_imagen)

img_reportes = img_reportes.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_reportes = ImageTk.PhotoImage(img_reportes)

boton_reportes = tk.Button(
    frame_botones, 
    width=70,
    height=63,
    text="REPORTES", 
    command=lambda: mostrar_frame(frame_reportes),
    image=img_reportes,
    compound="top",        # Muestra imagen arriba y texto debajo
    bg="#B57EDC",
    fg="white",
    font=("Helvetica", 8, "bold"),
    relief="raised",
    bd=4,
    padx=10,
    pady=10
)
boton_reportes.image = img_reportes  # Esto es necesario para que no se pierda la imagen
boton_reportes.pack( padx=10,pady=10)

# Botón salir
#  Imagenes para los iconos
ruta_imagen = os.path.join("imagenes", "exit.png")
img_salir = Image.open(ruta_imagen)

img_salir = img_salir.resize((40, 40))  # Ajustá el tamaño según lo que necesites
img_salir = ImageTk.PhotoImage(img_salir)

boton_salir = tk.Button(
    frame_botones, 
    width=70,
    height=63,
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