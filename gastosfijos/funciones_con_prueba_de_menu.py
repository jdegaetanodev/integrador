import funciones
import importlib.util
import os

RUTA_DICT = os.path.join("datos", "gastosfijos.py")

def mostrar_diccionario_actual():
    try:
        spec = importlib.util.spec_from_file_location("gastosfijos_dict", RUTA_DICT)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        print("\n📁 Diccionario actual en datos/gastosfijos.py:")
        for k, v in modulo.gastosfijos_dict.items():
            print(f"ID: {k} - Categoria: {v['id_categoria']} - Nombre: {v['nombre']} - Monto: {v['monto']} - Descripcion: {v['descripcion']} - Mes: {v['mes']} - Anio: {v['anio']} - Abonado: {v['abonado']} - Fecha Pago: {v['fecha_pago']}")
    except Exception as e:
        print(f"Error al cargar el diccionario: {e}")

def listar_gastosfijos():
    gastosfijos = funciones.cargar_gastosfijos()
    if not gastosfijos:
        print("No hay gastos fijos cargados.")
    else:
        print("\nListado de gastos fijos:")
        for g in gastosfijos:
            print(f"ID: {g['id_gastos_fijos']} - Categoria: {g['id_categoria']} - Nombre: {g['nombre']} - Monto: {g['monto']} - Descripcion: {g['descripción']} - Mes: {g['mes']} - Anio: {g['anio']} - Abonado: {g['abonado']} - Fecha Pago: {g['fecha_pago']}")

def agregar_gastofijo():
    try:
        id_categoria = int(input("Ingrese el ID de la categoría: ").strip())
    except ValueError:
        print("ID de categoría inválido.")
        return
    nombre = input("Ingrese el nombre del gasto fijo: ").strip()
    if not nombre:
        print("Nombre vacío, operación cancelada.")
        return
    try:
        monto = float(input("Ingrese el monto: ").strip())
    except ValueError:
        print("Monto inválido.")
        return
    descripcion = input("Ingrese la descripción: ").strip()
    try:
        mes = int(input("Ingrese el mes (número): ").strip())
        anio = int(input("Ingrese el año: ").strip())
    except ValueError:
        print("Mes o año inválido.")
        return
    abonado_str = input("¿Está abonado? (s/n): ").strip().lower()
    abonado = abonado_str == 's'
    fecha_pago = input("Ingrese la fecha de pago (AAAA-MM-DD): ").strip()

    gastofijo = {
        "id_categoria": id_categoria,
        "nombre": nombre,
        "monto": monto,
        "descripción": descripcion,
        "mes": mes,
        "anio": anio,
        "abonado": abonado,
        "fecha_pago": fecha_pago
    }
    resultado = funciones.add_gastofijo(gastofijo)
    if resultado:
        print("Gasto fijo agregado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("Error al agregar el gasto fijo.")

def modificar_gastofijo():
    try:
        id_gastofijo = int(input("Ingrese el ID del gasto fijo a modificar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    try:
        id_categoria = int(input("Ingrese el nuevo ID de la categoría: ").strip())
    except ValueError:
        print("ID de categoría inválido.")
        return
    nombre = input("Ingrese el nuevo nombre del gasto fijo: ").strip()
    if not nombre:
        print("Nombre vacío, operación cancelada.")
        return
    try:
        monto = float(input("Ingrese el nuevo monto: ").strip())
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
    abonado_str = input("¿Está abonado? (s/n): ").strip().lower()
    abonado = abonado_str == 's'
    fecha_pago = input("Ingrese la nueva fecha de pago (AAAA-MM-DD): ").strip()

    nuevo_gastofijo = {
        "id_categoria": id_categoria,
        "nombre": nombre,
        "monto": monto,
        "descripción": descripcion,
        "mes": mes,
        "anio": anio,
        "abonado": abonado,
        "fecha_pago": fecha_pago
    }
    resultado = funciones.update_gastofijo(id_gastofijo, nuevo_gastofijo)
    if resultado:
        print("Gasto fijo modificado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("No se pudo modificar el gasto fijo (ID no encontrado).")

def eliminar_gastofijo():
    try:
        id_gastofijo = int(input("Ingrese el ID del gasto fijo a eliminar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    confirmacion = input(f"¿Está seguro que desea eliminar el gasto fijo con ID {id_gastofijo}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("Operación cancelada.")
        return
    resultado = funciones.delete_gastofijo(id_gastofijo)
    if resultado:
        print("Gasto fijo eliminado correctamente.")
        mostrar_diccionario_actual()
    else:
        print("No se pudo eliminar el gasto fijo (ID no encontrado).")

def mostrar_menu():
    print("\n--- Menú Gastos Fijos ---")
    print("1. Listar gastos fijos")
    print("2. Agregar gasto fijo")
    print("3. Modificar gasto fijo")
    print("4. Eliminar gasto fijo")
    print("5. Ver diccionario actual")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_gastosfijos()
        elif opcion == "2":
            agregar_gastofijo()
        elif opcion == "3":
            modificar_gastofijo()
        elif opcion == "4":
            eliminar_gastofijo()
        elif opcion == "5":
            mostrar_diccionario_actual()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
