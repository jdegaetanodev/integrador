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
        return categorias
    except Exception as e:
        print("Error al cargar categorías:", e)
        return []

def guardar_categorias(categorias):
    try:
        # Crear carpeta si no existe
        os.makedirs(os.path.dirname(RUTA_JSON), exist_ok=True)

        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(categorias, archivo, indent=4, ensure_ascii=False)
            archivo.flush()
            os.fsync(archivo.fileno())

        return True
    except Exception as e:
        print("Error en guardar_categorias:", e)
        return False

def guardar_diccionario(categorias):
    try:
        texto = "categorias = [\n"
        for c in categorias:
            texto += "    {\n"
            texto += f"        'id_categoria': {c['id_categoria']},\n"
            texto += f"        'nombre_categoria': \"{c['nombre_categoria']}\"\n"
            texto += "    },\n"
        texto += "]\n"
        with open(RUTA_DICT, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except Exception as e:
        print("Error en guardar_diccionario:", e)
        pass

def update_categoria(id_categoria, categoria_txt, ventana_categoria, callback_actualizar=None):
    try:
        categorias = cargar_categorias()
        for categoria in categorias:
            if categoria["id_categoria"] == int(id_categoria):
                categoria["nombre_categoria"] = categoria_txt
                guardado = guardar_categorias(categorias)
                if guardado:
                    messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
                    if callback_actualizar:
                        callback_actualizar()
                    ventana_categoria.destroy()
                    return True
                else:
                    messagebox.showerror("Error", "No se pudo guardar la categoría.")
                    return False
        messagebox.showerror("Error", "No se encontró la categoría con ese ID.")
        return False
    except Exception as e:
        print("Error en update_categoria:", e)
        messagebox.showerror("Error", "Ocurrió un error al actualizar la categoría.")
        return False

def add_categoria(categoria_txt, ventana_categoria, callback_actualizar=None):
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
        guardado = guardar_categorias(categorias)
        if guardado:
            messagebox.showinfo("Éxito", "Categoría añadida correctamente.")
            if callback_actualizar:
                callback_actualizar()
            ventana_categoria.destroy()
            return True
        else:
            messagebox.showerror("Error", "No se pudo guardar la nueva categoría.")
            return False
    except Exception as e:
        print("Error en add_categoria:", e)
        messagebox.showerror("Error", "Ocurrió un error al añadir la categoría.")
        return False

def delete_categoria(id_categoria):
    try:
        categorias = cargar_categorias()
        nuevas_categorias = [c for c in categorias if c["id_categoria"] != int(id_categoria)]
        if len(nuevas_categorias) == len(categorias):
            return False
        return guardar_categorias(nuevas_categorias)
    except Exception as e:
        print("Error en delete_categoria:", e)
        return False