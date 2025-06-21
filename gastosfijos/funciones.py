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
            gastosfijos = json.load(archivo)
        return gastosfijos
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
            texto += f"    {g['id_gastos_fijos']}: {{\n"
            texto += f"        'id_categoria': {g['id_categoria']},\n"
            texto += f"        'nombre': \"{g['nombre']}\",\n"
            texto += f"        'monto': {g['monto']},\n"
            texto += f"        'descripcion': \"{g['descripción']}\",\n"
            texto += f"        'mes': {g['mes']},\n"
            texto += f"        'anio': {g['anio']},\n"
            texto += f"        'abonado': {g['abonado']},\n"
            texto += f"        'fecha_pago': \"{g['fecha_pago']}\"\n"
            texto += f"    }},\n"
        texto += "}\n"
        with open(RUTA_DICT, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except:
        pass  # Opcional: loguear error

def add_gastofijo(gastofijo):
    """
    gastofijo es un diccionario con keys: id_categoria, nombre, monto, descripción, mes, anio, abonado, fecha_pago
    """
    try:
        gastosfijos = cargar_gastosfijos()
        nuevo_id = 1
        if gastosfijos:
            nuevo_id = max(g["id_gastos_fijos"] for g in gastosfijos) + 1
        gastofijo["id_gastos_fijos"] = nuevo_id
        gastosfijos.append(gastofijo)
        return guardar_gastosfijos(gastosfijos)
    except:
        return False

def update_gastofijo(id_gastofijo, nuevo_gastofijo):
    """
    nuevo_gastofijo es un diccionario con keys: id_categoria, nombre, monto, descripción, mes, anio, abonado, fecha_pago
    """
    try:
        gastosfijos = cargar_gastosfijos()
        for gastofijo in gastosfijos:
            if gastofijo["id_gastos_fijos"] == id_gastofijo:
                gastofijo.update(nuevo_gastofijo)
                return guardar_gastosfijos(gastosfijos)
        return False
    except:
        return False

def delete_gastofijo(id_gastofijo):
    try:
        gastosfijos = cargar_gastosfijos()
        nuevos_gastosfijos = [g for g in gastosfijos if g["id_gastos_fijos"] != id_gastofijo]
        if len(nuevos_gastosfijos) == len(gastosfijos):
            return False
        return guardar_gastosfijos(nuevos_gastosfijos)
    except:
        return False
