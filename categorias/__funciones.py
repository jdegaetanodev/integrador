import os
import json
from tkinter import messagebox
from datos.categorias import categorias

RUTA_JSON = os.path.join("categorias", "categorias.json")

def cargar_categorias():
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            categorias = json.load(archivo)
        return categorias
    except:
        return []

def guardar_categorias(categorias):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(categorias, archivo, indent=4, ensure_ascii=False)
        return True
    except:
        return False

def update_categoria(id_categoria, categoria_txt):
    try:
        categorias = cargar_categorias()
        for categoria in categorias:
            if categoria["id_categoria"] == id_categoria:
                categoria["nombre_categoria"] = categoria_txt
                messagebox.showinfo("Éxito", "La categoría se guardó correctamente.")
                return guardar_categorias(categorias)
        
        messagebox.showinfo("Éxito", "Se produjo un error al guardar la categoría. 1")
        return False
    except:
        messagebox.showinfo("Éxito", "Se produjo un error al guardar la categoría. 2")
        return False

def add_categoria(categoria_txt):
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
        return guardar_categorias(categorias)
    except:
        return False

def delete_categoria(id_categoria):
    try:
        categorias = cargar_categorias()
        nuevas_categorias = [c for c in categorias if c["id_categoria"] != id_categoria]

        if len(nuevas_categorias) == len(categorias):
            #No se encontró la categoría a eliminar
            return False

        return guardar_categorias(nuevas_categorias)
    except:
        return False
