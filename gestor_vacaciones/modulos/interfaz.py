from . import funciones
from . import constantes
from . import control_entradas
from . import imprimir



def solicitudes_visualizar_por_user_id(id:int):
    solicitudes = funciones.obtener_solicitudes_por_usuario(1)
    imprimir.solicitudes(solicitudes)

def solicitudes_visualizar():
    solicitudes = funciones.obtener_solicitudes()
    mapa_usuarios = funciones.obtener_mapa_usuarios()
    imprimir.solicitudes(solicitudes,mapa_usuarios)

def solicitudes_obtener_por_estado(estado:str):
    solicitudes = funciones.obtener_solicitudes_por_estado(estado)
    mapa_usuarios = funciones.obtener_mapa_usuarios()
    imprimir.solicitudes(solicitudes,mapa_usuarios)


def solicitudes_crear(id_usuario_logueado):
    """
    Pide al usuario por consola el mes, día de inicio y día de fin usando
    las funciones de control de entradas, y ejecuta la función CRUD.
    
    :param id_usuario_logueado: int -> ID del usuario de la sesión activa.
    :param crear_solicitud_crud: function -> La función CRUD 'crear_solicitud' para guardarlo.
    """
    print("\n--- 📝 NUEVA SOLICITUD DE VACACIONES ---")
    
    # 1. Mostrar los meses disponibles para que el usuario elija
    print("\nMeses disponibles:")
    for i, mes in enumerate(constantes.NOMBRES_MESES):
        print(f"  {i + 1}. {mes}")
    print("----------------------------------------")
    
    # 2. Pedir el mes usando tu validador de rango (1 al 12)
    opcion_mes = control_entradas.pedir_entero_en_rango("Seleccione el número del mes", 1, 12)
    mes_idx = opcion_mes - 1  # Pasamos a índice base 0
    
    # Obtener el límite real de días de ese mes usando la constante MATRIZ_MESES
    max_dias_mes = len(constantes.MATRIZ_MESES[mes_idx])
    print(f"\n📌 El mes de {constantes.NOMBRES_MESES[mes_idx]} tiene {max_dias_mes} días.")
    
    # 3. Pedir el día de inicio y el día de fin con un bucle solo para la coherencia lógica (inicio <= fin)
    while True:
        dia_inicio = control_entradas.pedir_entero_en_rango(f"Ingrese el día de INICIO (1-{max_dias_mes})", 1, max_dias_mes)
        dia_fin = control_entradas.pedir_entero_en_rango(f"Ingrese el día de FIN (1-{max_dias_mes})", 1, max_dias_mes)
        
        if dia_inicio <= dia_fin:
            break
        
        print(f"{constantes.TEXTO_ERROR_GENERICO}El día de inicio no puede ser mayor que el día de fin. Reintente.\n")
    
    # Transformamos los días elegidos a índices (Día 1 -> Índice 0)
    dia_inicio_idx = dia_inicio - 1
    dia_fin_idx = dia_fin - 1
    
    funciones.solicitudes_crear(id_usuario_logueado, mes_idx, dia_inicio_idx, dia_fin_idx)
    