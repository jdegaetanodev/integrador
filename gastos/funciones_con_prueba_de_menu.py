import funciones
import importlib.util
import os

RUTA_DICT = os.path.join("datos", "gastos.py")

def mostrar_diccionario_actual():
    try:
        spec = importlib.util.spec_from_file_location("gastos_dict", RUTA_DICT)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        print("\n📁 Diccionario actual en datos/gastos.py:")
        for k, v in modulo.gastos_dict.items():
            print(f"ID: {k} - Categoria: {v['id_categoria']} - Nombre: {v['nombre']} - Monto: {v['monto']} - Detalle: {v['detalle']} - Fecha: {v['fecha']}")
    except Exception as e:
        print(f"Error al cargar el diccionario: {e}")

def listar_gastos():
    gastos = funciones.cargar_gastos()
    if not gastos:
        print("No hay gastos cargados.")
    else:
        print("\nListado de gastos:")
        for g in gastos:
            print(f"ID: {g['id_gastos']} - Categoria: {g['id_categoria']} - Nombre: {g['nombre']} - Monto: {g['monto']} - Detalle: {g['detalle']} - Fecha: {g['fecha']}")

def agregar_gasto():
    try:
        id_categoria = int(input("Ingrese el ID de la categoría: ").strip())
    except ValueError:
        print("ID de categoría inválido.")
        return
    nombre = input("Ingrese el nombre del gasto: ").strip()
    if not nombre:
        print("Nombre vacío, operación cancelada.")
        return
    try:
        monto = float(input("Ingrese el monto: ").strip())
    except ValueError:
        print("Monto inválido.")
        return
    detalle = input("Ingrese detalle: ").strip()
    fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
    gasto = {
        "id_categoria": id_categoria,
        "nombre": nombre,
        "monto": monto,
        "detalle": detalle,
        "fecha": fecha
    }
    resultado = funciones.add_gasto(gasto)
    if resultado:
        print("Gasto agregado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("Error al agregar el gasto.")

def modificar_gasto():
    try:
        id_gasto = int(input("Ingrese el ID del gasto a modificar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    try:
        id_categoria = int(input("Ingrese el nuevo ID de la categoría: ").strip())
    except ValueError:
        print("ID de categoría inválido.")
        return
    nombre = input("Ingrese el nuevo nombre del gasto: ").strip()
    if not nombre:
        print("Nombre vacío, operación cancelada.")
        return
    try:
        monto = float(input("Ingrese el nuevo monto: ").strip())
    except ValueError:
        print("Monto inválido.")
        return
    detalle = input("Ingrese el nuevo detalle: ").strip()
    fecha = input("Ingrese la nueva fecha (AAAA-MM-DD): ").strip()
    nuevo_gasto = {
        "id_categoria": id_categoria,
        "nombre": nombre,
        "monto": monto,
        "detalle": detalle,
        "fecha": fecha
    }
    resultado = funciones.update_gasto(id_gasto, nuevo_gasto)
    if resultado:
        print("Gasto modificado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("No se pudo modificar el gasto (ID no encontrado).")

def eliminar_gasto():
    try:
        id_gasto = int(input("Ingrese el ID del gasto a eliminar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    confirmacion = input(f"¿Está seguro que desea eliminar el gasto con ID {id_gasto}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("Operación cancelada.")
        return
    resultado = funciones.delete_gasto(id_gasto)
    if resultado:
        print("Gasto eliminado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("No se pudo eliminar el gasto (ID no encontrado).")

def mostrar_menu():
    print("\n--- Menú Gastos ---")
    print("1. Listar gastos")
    print("2. Agregar gasto")
    print("3. Modificar gasto")
    print("4. Eliminar gasto")
    print("5. Ver diccionario actual")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_gastos()
        elif opcion == "2":
            agregar_gasto()
        elif opcion == "3":
            modificar_gasto()
        elif opcion == "4":
            eliminar_gasto()
        elif opcion == "5":
            mostrar_diccionario_actual()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
