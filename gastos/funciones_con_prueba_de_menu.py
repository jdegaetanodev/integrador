import funciones
import os

def listar_gastos():
    gastos = funciones.cargar_gastos()
    if not gastos:
        print("No hay gastos cargados.")
    else:
        print("\nListado de gastos:")
        for g in gastos:
            print(f"ID: {g['id_gastos']} - Categoria: {g['id_categoria']} - Nombre: {g['nombre']} - Monto: {g['monto']} - Detalle: {g.get('detalle','')} - Fecha: {g.get('fecha','')}")

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

    # Aquí se llaman los parámetros individuales
    resultado = funciones.add_gasto(nombre, id_categoria, monto, fecha, detalle, ventana_gastos=None)
    if resultado:
        print("Gasto agregado correctamente.")
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

    # La función update_gasto requiere id_gasto, id_categoria, nombre, categoria (?), monto, fecha, detalle, ventana_gasto, callback_actualizar
    # Aquí el parámetro 'categoria' no tiene sentido, pasamos '' y ventana None, callback None para evitar errores
    resultado = funciones.update_gasto(id_gasto, id_categoria, nombre, '', monto, fecha, detalle, ventana_gasto=None, callback_actualizar=None)
    if resultado:
        print("Gasto modificado correctamente.")
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
    else:
        print("No se pudo eliminar el gasto (ID no encontrado).")

def exportar_gastos_a_excel():
    try:
        funciones.exportar_gastos()
    except Exception as e:
        print(f"Error en la exportación: {e}")

def mostrar_menu():
    print("\n--- Menú Gastos ---")
    print("1. Listar gastos")
    print("2. Agregar gasto")
    print("3. Modificar gasto")
    print("4. Eliminar gasto")
    print("5. Exportar gastos a Excel")
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
            exportar_gastos_a_excel()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
