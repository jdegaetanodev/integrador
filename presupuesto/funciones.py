import os
import json
from tkinter import messagebox

RUTA_JSON = os.path.join("presupuesto", "presupuesto.json")
RUTA_DICT = os.path.join("datos", "presupuesto.py")

def cargar_presupuestos():
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            presupuestos = json.load(archivo)
        return presupuestos
    except:
        return []

def guardar_presupuestos(presupuestos):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(presupuestos, archivo, indent=4, ensure_ascii=False)
        guardar_diccionario(presupuestos)
        return True
    except:
        return False

def guardar_diccionario(presupuestos):
    try:
        texto = "presupuesto_dict = {\n"
        for p in presupuestos:
            texto += f"    {p['id_presupuesto']}: {{\n"
            texto += f"        'id_categoria': {p['id_categoria']},\n"
            texto += f"        'monto_presupuesto': {p['monto_presupuesto']},\n"
            texto += f"        'descripcion': \"{p['descripcion']}\",\n"
            texto += f"        'mes': {p['mes']},\n"
            texto += f"        'anio': {p['anio']}\n"
            texto += f"    }},\n"
        texto += "}\n"
        with open(RUTA_DICT, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except:
        pass  # Podés loguear o imprimir error si querés

def add_presupuesto(presupuesto):
    """
    presupuesto es un dict con keys: id_categoria, monto_presupuesto, descripcion, mes, anio
    """
    try:
        presupuestos = cargar_presupuestos()
        nuevo_id = 1
        if presupuestos:
            nuevo_id = max(p["id_presupuesto"] for p in presupuestos) + 1
        presupuesto["id_presupuesto"] = nuevo_id
        presupuestos.append(presupuesto)
        return guardar_presupuestos(presupuestos)
    except:
        return False

def update_presupuesto(id_presupuesto, nuevo_presupuesto):
    """
    nuevo_presupuesto es un dict con keys: id_categoria, monto_presupuesto, descripcion, mes, anio
    """
    try:
        presupuestos = cargar_presupuestos()
        for p in presupuestos:
            if p["id_presupuesto"] == id_presupuesto:
                p.update(nuevo_presupuesto)
                return guardar_presupuestos(presupuestos)
        return False
    except:
        return False

def delete_presupuesto(id_presupuesto):
    try:
        presupuestos = cargar_presupuestos()
        nuevos_presupuestos = [p for p in presupuestos if p["id_presupuesto"] != id_presupuesto]
        if len(nuevos_presupuestos) == len(presupuestos):
            return False
        return guardar_presupuestos(nuevos_presupuestos)
    except:
        return False
