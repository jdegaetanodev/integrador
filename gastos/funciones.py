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
        # Crear carpeta si no existe
        os.makedirs(os.path.dirname(RUTA_JSON), exist_ok=True)

        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(gastos, archivo, indent=4, ensure_ascii=False)
            archivo.flush()
            os.fsync(archivo.fileno())

        return True
    except Exception as e:
        print("Error en guardar_gastos:", e)
        return False

def guardar_diccionario(gastos):
    try:
        texto = "gastos = [\n"
        for g in gastos:
            texto += "    {\n"
            texto += f"        'id_gastos': {g['id_gastos']},\n"
            texto += f"        'id_categoria': {g['id_categoria']},\n"
            texto += f"        'nombre': \"{g['nombre']}\",\n"
            texto += f"        'monto': {g['monto']},\n"
            texto += f"        'detalle': \"{g['detalle']}\",\n"
            texto += f"        'fecha': \"{g['fecha']}\"\n"
            texto += "    },\n"
        texto += "]\n"
        with open(RUTA_DICT, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except:
        pass

def add_gasto(nombre, id_categoria, monto, fecha, descripcion, ventana_gastos, callback_actualizar=None):   

    if validar_datos(id_categoria, nombre, monto, fecha, descripcion):   

        try:
            gastos = cargar_gastos()
            nuevo_id = 1
            if gastos:
                nuevo_id = max(c["id_gastos"] for c in gastos) + 1

            nuevo_gasto = {
                "id_gastos": nuevo_id,
                "nombre": nombre,
                "id_categoria": id_categoria,
                "monto": monto,
                "fecha": fecha,
                "descripcion": descripcion
            }

            gastos.append(nuevo_gasto)
            guardado = guardar_gastos(gastos)

            if guardado:
                messagebox.showinfo("Éxito", "Gasto cargado correctamente.")
                if callback_actualizar:
                    callback_actualizar()
                ventana_gastos.destroy()
                return True
            else:
                messagebox.showerror("Error", "No se pudo guardar el gasto.")
                return False
        except Exception as e:
            print("Error en add_gasto:", e)
            messagebox.showerror("Error", "Ocurrió un error al añadir el gasto.")
            return False
    else:
        messagebox.showerror("Error", "Por favor complete todos los campos del formulario")


def update_gasto(id_gasto, id_categoria, nombre, categoria, monto, fecha, detalle, ventana_gasto, callback_actualizar):

    if validar_datos(id_categoria, nombre, monto, fecha, detalle):   

        try:
            nuevo_gasto = {
                "id_categoria": int(id_categoria),
                "nombre": nombre,
                "categoria": categoria,
                "monto": monto,
                "fecha": fecha,
                "detalle": detalle
            }

            gastos = cargar_gastos()
            for gasto in gastos:

                if gasto["id_gastos"] == int(id_gasto):
                    gasto.update(nuevo_gasto)
                    guardado = guardar_gastos(gastos)
                    if guardado:
                        messagebox.showinfo("Éxito", "Gasto actualizado correctamente.")
                        if callback_actualizar:
                            callback_actualizar()
                        ventana_gasto.destroy()
                        return True
                    else:
                        messagebox.showerror("Error", "No se pudo guardar el gasto.")
                        return False
            messagebox.showerror("Error", "No se encontró un Gasto con ese ID.")
            return False
        except Exception as e:
            print("Error en update_gasto:", e)
            messagebox.showerror("Error", "Ocurrió un error al actualizar el gasto.")
            return False
    else:
        messagebox.showerror("Error", "Por favor complete todos los campos del formulario")

def delete_gasto(id_gasto):
    try:
        gastos = cargar_gastos()
        nuevos_gastos = [g for g in gastos if g["id_gastos"] != id_gasto]
        if len(nuevos_gastos) == len(gastos):
            return False
        return guardar_gastos(nuevos_gastos)
    except:
        return False

def exportar_gastos():
    messagebox.showinfo("Éxito", "En esta Función se exportan los Gastos")

def validar_datos(id_categoria, nombre, monto, fecha, detalle):    
    return True      