import funciones
import os

def listar_presupuestos():
    presupuestos = funciones.cargar_presupuestos()
    if not presupuestos:
        print("📂 No hay presupuestos cargados.")
    else:
        print("\n📋 Listado de presupuestos:")
        for p in presupuestos:
            print(f"🆔 ID: {p['id_presupuesto']} - 📚 Categoría: {p['id_categoria']} - 💰 Monto: {p['monto_presupuesto']} - 🗒️ Descripción: {p['descripcion']} - 📅 Mes: {p['mes']} - 📆 Año: {p['anio']}")

def agregar_presupuesto():
    try:
        id_categoria = int(input("📝 Ingrese el ID de la categoría: ").strip())
        monto_presupuesto = float(input("💰 Ingrese el monto del presupuesto: ").strip())
        descripcion = input("🗒️ Ingrese la descripción del presupuesto: ").strip()
        mes = int(input("📅 Ingrese el mes (número): ").strip())
        anio = int(input("📅 Ingrese el año: ").strip())
    except ValueError:
        print("❌ Dato inválido ingresado.")
        return

    presupuesto = {
        "id_categoria": id_categoria,
        "monto_presupuesto": monto_presupuesto,
        "descripcion": descripcion,
        "mes": mes,
        "anio": anio
    }
    if funciones.add_presupuesto(presupuesto):
        print("✅ Presupuesto agregado correctamente.")
    else:
        print("❌ Error al agregar el presupuesto.")

def modificar_presupuesto():
    try:
        id_presupuesto = int(input("🔧 Ingrese el ID del presupuesto a modificar: ").strip())
        id_categoria = int(input("📝 Ingrese el nuevo ID de la categoría: ").strip())
        monto_presupuesto = float(input("💰 Ingrese el nuevo monto del presupuesto: ").strip())
        descripcion = input("🗒️ Ingrese la nueva descripción: ").strip()
        mes = int(input("📅 Ingrese el nuevo mes (número): ").strip())
        anio = int(input("📅 Ingrese el nuevo año: ").strip())
    except ValueError:
        print("❌ Dato inválido ingresado.")
        return

    nuevo_presupuesto = {
        "id_categoria": id_categoria,
        "monto_presupuesto": monto_presupuesto,
        "descripcion": descripcion,
        "mes": mes,
        "anio": anio
    }
    if funciones.update_presupuesto(id_presupuesto, nuevo_presupuesto):
        print("✅ Presupuesto modificado correctamente.")
    else:
        print("❌ No se pudo modificar el presupuesto (ID no encontrado).")

def eliminar_presupuesto():
    try:
        id_presupuesto = int(input("🗑️ Ingrese el ID del presupuesto a eliminar: ").strip())
    except ValueError:
        print("❌ ID inválido.")
        return
    confirmacion = input(f"❓ ¿Está seguro que desea eliminar el presupuesto con ID {id_presupuesto}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("ℹ️ Operación cancelada.")
        return
    if funciones.delete_presupuesto(id_presupuesto):
        print("✅ Presupuesto eliminado correctamente.")
    else:
        print("❌ No se pudo eliminar el presupuesto (ID no encontrado).")

def exportar_presupuestos_a_excel():
    try:
        if funciones.exportar_presupuesto():
            print("✅ Presupuestos exportados a Excel correctamente.")
        else:
            print("❌ Error al exportar los presupuestos a Excel.")
    except Exception as e:
        print(f"❌ Error en la exportación: {e}")

def mostrar_menu():
    print("\n📌 --- Menú Presupuestos ---")
    print("1. 📋 Listar presupuestos")
    print("2. ➕ Agregar presupuesto")
    print("3. ✏️ Modificar presupuesto")
    print("4. 🗑️ Eliminar presupuesto")
    print("5. 📤 Exportar presupuestos a Excel")
    print("6. 🚪 Salir")

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
            exportar_presupuestos_a_excel()
        elif opcion == "6":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
