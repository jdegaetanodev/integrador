import os
import json
from tkinter import messagebox

RUTA_JSON = os.path.join("categorias", "categorias.json")
RUTA_DICT = os.path.join("datos", "categorias.py")

def cargar_categorias():
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            categorias = json.load(archivo)
            print(f"Se han cargado {len(categorias)} categorías desde el archivo JSON.")
        return categorias
    except:
        return []

def guardar_categorias(categorias):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(categorias, archivo, indent=4, ensure_ascii=False)
            archivo.flush() 
            os.fsync(archivo.fileno())

        return True
    except:
        return False

    
def update_categoria(id_categoria, categoria_txt, ventana_categoria, callback_actualizar=None):

    try:
        categorias = cargar_categorias()
        for categoria in categorias:

            if categoria["id_categoria"] == int(id_categoria):
                categoria["nombre_categoria"] = categoria_txt
                messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")    
                ventana_categoria.destroy()  # Cerrar la ventana de actualización    
                callback_actualizar()  # Actualizar la tabla de categorías        
                return guardar_categorias(categorias)                
        return False
        messagebox.showerror("Error", "No se pudo actualizar la categoría.")
    except:        
        return False

def add_categoria(categoria_txt,ventana_categoria,callback_actualizar=None):
    try:
        categorias = cargar_categorias()
        nuevo_id = 1
        if categorias:
            nuevo_id = max(c["id_categoria"] for c in categorias) + 1
        nueva_categoria = {
            "id_categoria": nuevo_id,
            "nombre_categoria": categoria_txt
        }
        categorias.append(nueva_categoria)
        messagebox.showinfo("Éxito", "Categoría añadida correctamente.")
        callback_actualizar()  # Actualizar la tabla de categorías
        ventana_categoria.destroy()  # Cerrar la ventana de actualización            
        return guardar_categorias(categorias)
    except:
        return False

def delete_categoria(id_categoria):
    try:
        categorias = cargar_categorias()
        nuevas_categorias = [c for c in categorias if c["id_categoria"] != id_categoria]
        if len(nuevas_categorias) == len(categorias):
            return False
        return guardar_categorias(nuevas_categorias)
    except:
        return False

