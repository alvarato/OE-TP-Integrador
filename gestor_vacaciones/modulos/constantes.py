# Matriz anual: 12 meses con sus respectivos días (0 = libre, 1 = ocupado)
# Enero es el índice 0, Febrero el índice 1, etc.
MATRIZ_MESES = [
    [0] * 31,  # Enero (Índice 0)
    [0] * 28,  # Febrero (Índice 1 - año estándar)
    [0] * 31,  # Marzo (Índice 2)
    [0] * 30,  # Abril (Índice 3)
    [0] * 31,  # Mayo (Índice 4)
    [0] * 30,  # Junio (Índice 5)
    [0] * 31,  # Julio (Índice 6)
    [0] * 31,  # Agosto (Índice 7)
    [0] * 30,  # Septiembre (Índice 8)
    [0] * 31,  # Octubre (Índice 9)
    [0] * 30,  # Noviembre (Índice 10)
    [0] * 31   # Diciembre (Índice 11)
]

ESTADOS_SOLICITUD = {
    "PENDIENTE": "Pendiente",
    "APROBADA": "Aprobada",
    "RECHAZADA": "Rechazada",
    "CANCELADA": "Cancelado"
}

TEXTO_ERROR_GENERICO = "❌ Error: "
TEXTO_EXITO_GENERICO = "✅ Éxito: "

    # Mapeo de índices a nombres de meses para que sea amigable al usuario
NOMBRES_MESES = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]