import funciones
import os

RUTA_JSON = os.path.join("categorias", "categorias.json")

def listar_categorias():
    categorias = funciones.cargar_categorias()
    if not categorias:
        print("📂 No hay categorías cargadas.")
    else:
        print("\n📋 Listado de categorías:")
        for c in categorias:
            print(f"🆔 ID: {c['id_categoria']} - 📚 Nombre: {c['nombre_categoria']}")

def agregar_categoria():
    nombre = input("📝 Ingrese el nombre de la nueva categoría: ").strip()
    if not nombre:
        print("⚠️ Nombre vacío, operación cancelada.")
        return
    resultado = funciones.add_categoria(nombre, ventana_categoria=None)
    if resultado:
        print("✅ Categoría agregada correctamente.")
        listar_categorias()
    else:
        print("❌ Error al agregar la categoría.")

def modificar_categoria():
    try:
        id_str = input("🔧 Ingrese el ID de la categoría a modificar: ").strip()
        id_categoria = int(id_str)
    except ValueError:
        print("❌ ID inválido.")
        return
    nombre = input("📝 Ingrese el nuevo nombre de la categoría: ").strip()
    if not nombre:
        print("⚠️ Nombre vacío, operación cancelada.")
        return
    resultado = funciones.update_categoria(id_categoria, nombre, ventana_categoria=None)
    if resultado:
        print("✅ Categoría modificada correctamente.")
        listar_categorias()
    else:
        print("❌ No se pudo modificar la categoría (ID no encontrado).")

def eliminar_categoria():
    try:
        id_str = input("🗑️ Ingrese el ID de la categoría a eliminar: ").strip()
        id_categoria = int(id_str)
    except ValueError:
        print("❌ ID inválido.")
        return
    confirmacion = input(f"❓ ¿Está seguro que desea eliminar la categoría con ID {id_categoria}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("ℹ️ Operación cancelada.")
        return
    resultado = funciones.delete_categoria(id_categoria)
    if resultado:
        print("✅ Categoría eliminada correctamente.")
        listar_categorias()
    else:
        print("❌ No se pudo eliminar la categoría (ID no encontrado).")

def exportar_categorias():
    try:
        resultado = funciones.exportar_categorias()
        if resultado:
            print("✅ Categorías exportadas a Excel correctamente.")
        else:
            print("❌ Error al exportar las categorías a Excel.")
    except Exception as e:
        print(f"❌ Error en la exportación: {e}")

def mostrar_menu():
    print("\n📌 --- Menú Categorías ---")
    print("1. 📋 Listar categorías")
    print("2. ➕ Agregar categoría")
    print("3. ✏️ Modificar categoría")
    print("4. 🗑️ Eliminar categoría")
    print("5. 📤 Exportar categorías a Excel")
    print("6. 🚪 Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_categorias()
        elif opcion == "2":
            agregar_categoria()
        elif opcion == "3":
            modificar_categoria()
        elif opcion == "4":
            eliminar_categoria()
        elif opcion == "5":
            exportar_categorias()
        elif opcion == "6":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
