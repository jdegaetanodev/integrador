import os
import json
from tkinter import messagebox

RUTA_JSON = os.path.join("gastosfijos", "gastosfijos.json")
RUTA_DICT = os.path.join("datos", "gastosfijos.py")

def cargar_gastosfijos():
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_gastosfijos(gastosfijos):
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(gastosfijos, archivo, indent=4, ensure_ascii=False)
        guardar_diccionario(gastosfijos)
        return True
    except:
        return False

def guardar_diccionario(gastosfijos):
    try:
        texto = "gastosfijos_dict = {\n"
        for g in gastosfijos:
            texto += f"    {g['id_gasto_fijo']}: {{\n"
            texto += f"        'id_categoria': {g['id_categoria']},\n"
            texto += f"        'nombre': \"{g['nombre']}\",\n"
            texto += f"        'monto': {g['monto']},\n"
            texto += f"        'descripcion': \"{g['descripcion']}\",\n"
            texto += f"        'mes': \"{g['mes']}\",\n"
            texto += f"        'anio': \"{g['anio']}\",\n"
            texto += f"        'abonado': \"{g['abonado']}\",\n"
            texto += f"        'fecha_pago': \"{g['fecha_pago']}\"\n"
            texto += f"    }},\n"
        texto += "}\n"
        with open(RUTA_DICT, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except:
        pass

def add_gastofijo(gastofijo):
    try:
        gastosfijos = cargar_gastosfijos()
        nuevo_id = 1
        if gastosfijos:
            nuevo_id = max(g["id_gasto_fijo"] for g in gastosfijos) + 1
        gastofijo["id_gasto_fijo"] = nuevo_id
        gastosfijos.append(gastofijo)
        return guardar_gastosfijos(gastosfijos)
    except:
        return False

def update_gastofijo(id_gastofijo, nuevo_gastofijo):
    try:
        gastosfijos = cargar_gastosfijos()
        for g in gastosfijos:
            if g["id_gasto_fijo"] == id_gastofijo:
                g.update(nuevo_gastofijo)
                return guardar_gastosfijos(gastosfijos)
        return False
    except:
        return False

def delete_gastofijo(id_gastofijo):
    try:
        gastosfijos = cargar_gastosfijos()
        nuevos = [g for g in gastosfijos if g["id_gasto_fijo"] != id_gastofijo]
        if len(nuevos) == len(gastosfijos):
            return False
        return guardar_gastosfijos(nuevos)
    except:
        return False
    
def exportar_gastos_fijos():
    messagebox.showinfo("Éxito", "En esta Función se exportan los Gastos Fijos")    

def validar_datos():
    return True         