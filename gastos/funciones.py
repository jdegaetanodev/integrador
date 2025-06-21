import os
import json
from tkinter import messagebox

RUTA_JSON = os.path.join("gastos", "gastos.json")
RUTA_DICT = os.path.join("datos", "gastos.py")

def cargar_gastos():
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            gastos = json.load(archivo)
        return gastos
    except:
        return []

def guardar_gastos(gastos):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(gastos, archivo, indent=4, ensure_ascii=False)
        guardar_diccionario(gastos)
        return True
    except:
        return False

def guardar_diccionario(gastos):
    try:
        texto = "gastos_dict = {\n"
        for g in gastos:
            texto += f"    {g['id_gastos']}: {{\n"
            texto += f"        'id_categoria': {g['id_categoria']},\n"
            texto += f"        'nombre': \"{g['nombre']}\",\n"
            texto += f"        'monto': {g['monto']},\n"
            texto += f"        'detalle': \"{g['detalle']}\",\n"
            texto += f"        'fecha': \"{g['fecha']}\"\n"
            texto += f"    }},\n"
        texto += "}\n"
        with open(RUTA_DICT, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except:
        pass  # Opcional: loguear error

def add_gasto(gasto):
    """
    gasto es un diccionario con keys: id_categoria, nombre, monto, detalle, fecha
    """
    try:
        gastos = cargar_gastos()
        nuevo_id = 1
        if gastos:
            nuevo_id = max(g["id_gastos"] for g in gastos) + 1
        gasto["id_gastos"] = nuevo_id
        gastos.append(gasto)
        return guardar_gastos(gastos)
    except:
        return False

def update_gasto(id_gasto, nuevo_gasto):
    """
    nuevo_gasto es un diccionario con keys: id_categoria, nombre, monto, detalle, fecha
    """
    try:
        gastos = cargar_gastos()
        for gasto in gastos:
            if gasto["id_gastos"] == id_gasto:
                gasto.update(nuevo_gasto)
                return guardar_gastos(gastos)
        return False
    except:
        return False

def delete_gasto(id_gasto):
    try:
        gastos = cargar_gastos()
        nuevos_gastos = [g for g in gastos if g["id_gastos"] != id_gasto]
        if len(nuevos_gastos) == len(gastos):
            return False
        return guardar_gastos(nuevos_gastos)
    except:
        return False
