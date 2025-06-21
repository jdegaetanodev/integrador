import funciones
import importlib.util
import os

RUTA_DICT = os.path.join("datos", "presupuesto.py")

def mostrar_diccionario_actual():
    try:
        spec = importlib.util.spec_from_file_location("presupuesto_dict", RUTA_DICT)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        print("\n📁 Diccionario actual en datos/presupuesto.py:")
        for k, v in modulo.presupuesto_dict.items():
            print(f"ID: {k} - Categoria: {v['id_categoria']} - Monto: {v['monto_presupuesto']} - Descripcion: {v['descripcion']} - Mes: {v['mes']} - Año: {v['anio']}")
    except Exception as e:
        print(f"Error al cargar el diccionario: {e}")

def listar_presupuestos():
    presupuestos = funciones.cargar_presupuestos()
    if not presupuestos:
        print("No hay presupuestos cargados.")
    else:
        print("\nListado de presupuestos:")
        for p in presupuestos:
            print(f"ID: {p['id_presupuesto']} - Categoria: {p['id_categoria']} - Monto: {p['monto_presupuesto']} - Descripcion: {p['descripcion']} - Mes: {p['mes']} - Año: {p['anio']}")

def agregar_presupuesto():
    try:
        id_categoria = int(input("Ingrese el ID de la categoría: ").strip())
    except ValueError:
        print("ID de categoría inválido.")
        return
    try:
        monto_presupuesto = float(input("Ingrese el monto del presupuesto: ").strip())
    except ValueError:
        print("Monto inválido.")
        return
    descripcion = input("Ingrese la descripción del presupuesto: ").strip()
    try:
        mes = int(input("Ingrese el mes (número): ").strip())
        anio = int(input("Ingrese el año: ").strip())
    except ValueError:
        print("Mes o año inválido.")
        return

    presupuesto = {
        "id_categoria": id_categoria,
        "monto_presupuesto": monto_presupuesto,
        "descripcion": descripcion,
        "mes": mes,
        "anio": anio
    }
    resultado = funciones.add_presupuesto(presupuesto)
    if resultado:
        print("Presupuesto agregado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("Error al agregar el presupuesto.")

def modificar_presupuesto():
    try:
        id_presupuesto = int(input("Ingrese el ID del presupuesto a modificar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    try:
        id_categoria = int(input("Ingrese el nuevo ID de la categoría: ").strip())
    except ValueError:
        print("ID de categoría inválido.")
        return
    try:
        monto_presupuesto = float(input("Ingrese el nuevo monto del presupuesto: ").strip())
    except ValueError:
        print("Monto inválido.")
        return
    descripcion = input("Ingrese la nueva descripción: ").strip()
    try:
        mes = int(input("Ingrese el nuevo mes (número): ").strip())
        anio = int(input("Ingrese el nuevo año: ").strip())
    except ValueError:
        print("Mes o año inválido.")
        return

    nuevo_presupuesto = {
        "id_categoria": id_categoria,
        "monto_presupuesto": monto_presupuesto,
        "descripcion": descripcion,
        "mes": mes,
        "anio": anio
    }
    resultado = funciones.update_presupuesto(id_presupuesto, nuevo_presupuesto)
    if resultado:
        print("Presupuesto modificado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("No se pudo modificar el presupuesto (ID no encontrado).")

def eliminar_presupuesto():
    try:
        id_presupuesto = int(input("Ingrese el ID del presupuesto a eliminar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    confirmacion = input(f"¿Está seguro que desea eliminar el presupuesto con ID {id_presupuesto}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("Operación cancelada.")
        return
    resultado = funciones.delete_presupuesto(id_presupuesto)
    if resultado:
        print("Presupuesto eliminado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("No se pudo eliminar el presupuesto (ID no encontrado).")

def mostrar_menu():
    print("\n--- Menú Presupuestos ---")
    print("1. Listar presupuestos")
    print("2. Agregar presupuesto")
    print("3. Modificar presupuesto")
    print("4. Eliminar presupuesto")
    print("5. Ver diccionario actual")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_presupuestos()
        elif opcion == "2":
            agregar_presupuesto()
        elif opcion == "3":
            modificar_presupuesto()
        elif opcion == "4":
            eliminar_presupuesto()
        elif opcion == "5":
            mostrar_diccionario_actual()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
