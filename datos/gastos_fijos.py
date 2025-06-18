# Cargar los datos desde el json

gastos_fijos = [
    {
        'id_gasto_fijo': 1,     # ID único del gasto fijo
        'id_categoria': 2,       # ID de la categoría (eje. Servicios)
        'nombre': 'Internet Hogar',
        'monto': 12500.00,
        'descripcion': 'Servicio de fibra óptica 300 MB',
        'mes': 6,                       # Mes al que corresponde el gasto fijo
        'anio': 2025,                   # Año al que corresponde el gasto fijo
        'abonado': True,                # Booleano: True si ya fue pagado este mes
        'fecha_pago': '2025-06-03'      # Fecha en que se  pago (None si no se pago)
    },
    {
        'id_gasto_fijo': 2,
        'id_categoria': 2,
        'nombre': 'Alquiler',
        'monto': 180000.00,
        'descripcion': 'Alquiler de departamento mensual',
        'mes': 6,
        'anio': 2025,
        'abonado': False,
        'fecha_pago': None
    }
]