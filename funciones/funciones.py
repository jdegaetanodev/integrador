def centrar_ventana(ventana, ancho=400, alto=300):
    # obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    # calcular las coordenadas x e y
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2

    # establecer tamaño y posición de la ventana
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


