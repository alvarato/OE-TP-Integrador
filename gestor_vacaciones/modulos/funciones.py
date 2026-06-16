from . import persistencias_solicitud
from . import persistencias_usuario
from .constantes import NOMBRES_MESES, ESTADOS_SOLICITUD

def formatear_nombre_compuesto(texto):
    return texto.strip().title()

def obtener_mapa_usuarios():
    return persistencias_usuario.obtener_mapa_usuarios_nombres()

def obtener_solicitudes_por_usuario(id_usuario: int):
    """
    Filtra y retorna las solicitudes de un usuario específico a partir 
    de la lista completa obtenida por el Read del CRUD.
    """
    todas_las_solicitudes = persistencias_solicitud.cargar_solicitudes()
    
    # Filtrar utilizando una lista de comprensión
    solicitudes_usuario = [
        solicitud for solicitud in todas_las_solicitudes 
        if solicitud["id_usuario"] == id_usuario
    ]
    return solicitudes_usuario

def obtener_solicitudes():
    return persistencias_solicitud.cargar_solicitudes()

def obtener_solicitudes_por_estado(estado:str):
    lista_solicitudes = persistencias_solicitud.cargar_solicitudes()

    # List comprehension para filtrar de forma eficiente y limpia
    pendientes = [s for s in lista_solicitudes if s["estado"] == estado]
    
    return pendientes

def solicitudes_crear(id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx):
    persistencias_solicitud.crear_solicitud(id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx)

    