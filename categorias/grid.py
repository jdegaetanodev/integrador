from tkinter import ttk
from categorias.funciones import listar_categorias

def crear_grid(parent):
    tree = ttk.Treeview(parent, columns=("ID", "Nombre"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.pack(fill="both", expand=True)
    return tree

def cargar_datos(tree):
    for row in tree.get_children():
        tree.delete(row)
    for cat in listar_categorias():
        tree.insert("", "end", values=(cat["id"], cat["nombre"]))