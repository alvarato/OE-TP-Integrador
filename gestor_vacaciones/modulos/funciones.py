from . import persistencias_solicitud
from . import persistencias_usuario
from .constantes import NOMBRES_MESES, ESTADOS_SOLICITUD,TEXTO_ERROR_GENERICO

def formatear_nombre_compuesto(texto):
    return texto.strip().title()

def verificar_login(username, contrasena):
    lista_usuarios = persistencias_usuario.cargar_usuarios()
    
    for usuario in lista_usuarios:
        if usuario["username"] == username and usuario["contrasena"] == contrasena:
            return usuario
            
    return None 

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
        if int(solicitud["id_usuario"]) == int(id_usuario)
    ]
    return solicitudes_usuario

def obtener_usuario_por_id(id_usuario: int):
    usuarios = persistencias_usuario.cargar_usuarios()
    
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            return usuario

def obtener_solicitudes():
    return persistencias_solicitud.cargar_solicitudes()

def obtener_solicitudes_por_estado(estado:str,id:int):
    #si recibe id busca por persona, si no trae todas
    lista_solicitudes = []
    if id == None:
        lista_solicitudes = persistencias_solicitud.cargar_solicitudes()
    else:
        lista_solicitudes = obtener_solicitudes_por_usuario(id)
    
    pendientes = [s for s in lista_solicitudes if s["estado"] == estado]
    
    return pendientes

def solicitudes_crear(id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx):
    try:
        dias_solicitados =  dia_fin_idx - dia_inicio_idx
        dias_disponibles = usuario_dias_disponibles(id_usuario)

        if dias_solicitados > dias_disponibles:
            raise ValueError("Los dias solicitados no pueden superar los dias disponibles")
        
        id_solicitud = persistencias_solicitud.crear_solicitud(id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx)
    
        if id_solicitud == None:
            raise ValueError("Solicitud no encontrada")
        
        usuario_actualizar_dias_gastados_por_user_id(id_usuario,dias_solicitados,1)

    except ValueError as e:
        print(f"{TEXTO_ERROR_GENERICO} {str(e)}")
    
def cancelar_solicitud_por_id(id_solicitud: int, id_usuario: int):
    try:
        # 1. Cargar la lista actual de diccionarios de solicitudes
        solicitudes = persistencias_solicitud.cargar_solicitudes()
        
        # 2. Buscar la solicitud con el ID indicado
        flag = True
        for solicitud in solicitudes:
            if int(solicitud["id_solicitud"]) == int(id_solicitud):
                flag = False
                if id_usuario != solicitud["id_usuario"]:
                    raise ValueError("Esta solicitud no pertenece al usuario actual.")
                elif solicitud["estado"] != ESTADOS_SOLICITUD["PENDIENTE"]:
                    raise ValueError("Solo se pueden cancelar solicitudes pendientes.")
                
                usuario_actualizar_dias_gastados(solicitud,2)
                break  # ID único, podemos salir del bucle

        if flag: raise ValueError(f"No existe la solicitud con el id: {id_solicitud}")
        
        
        persistencias_solicitud.actualizar_estado_solicitud(id_solicitud, ESTADOS_SOLICITUD["CANCELADA"])
    except ValueError as e:
        print(f"{TEXTO_ERROR_GENERICO} {str(e)}")
    
def rechazar_solicitud_por_id(id_solicitud: int):
    try:
        # 1. Cargar la lista actual de diccionarios de solicitudes
        solicitudes = persistencias_solicitud.cargar_solicitudes()
        
        flag = True
        for solicitud in solicitudes:
            if int(solicitud["id_solicitud"]) == int(id_solicitud):
                flag = False
                if solicitud["estado"] != ESTADOS_SOLICITUD["PENDIENTE"]:
                    raise ValueError("Solo se pueden rechazar solicitudes en estado pendiente.")
                usuario_actualizar_dias_gastados(solicitud,2)
                break  # ID único, podemos salir del bucle

        if flag: raise ValueError(f"No existe la solicitud con el id: {id_solicitud}")

        
        persistencias_solicitud.actualizar_estado_solicitud(id_solicitud, ESTADOS_SOLICITUD["RECHAZADA"])
    except ValueError as e:
        print(f"{TEXTO_ERROR_GENERICO} {str(e)}")   

def aprobar_solicitud_por_id(id_solicitud: int):
    try:
        # 1. Cargar la lista actual de diccionarios de solicitudes
        solicitudes = persistencias_solicitud.cargar_solicitudes()
        
        flag = True
        for solicitud in solicitudes:
            if int(solicitud["id_solicitud"]) == int(id_solicitud):
                flag = False
                if solicitud["estado"] != ESTADOS_SOLICITUD["PENDIENTE"]:
                    raise ValueError("Solo se pueden Aprobar solicitudes en estado pendiente.")
                break  # ID único, podemos salir del bucle

        if flag: raise ValueError(f"No existe la solicitud con el id: {id_solicitud}")        
        persistencias_solicitud.actualizar_estado_solicitud(id_solicitud, ESTADOS_SOLICITUD["APROBADA"])
    except ValueError as e:
        print(f"{TEXTO_ERROR_GENERICO} {str(e)}")

def usuario_actualizar_dias_gastados(solicitud,operacion):
    # 1 añade dias utilizados, 2 resta dias utilizados
    usuario = None
    dias_solicitados = solicitud["dia_fin_idx"] - solicitud["dia_inicio_idx"]
    if(operacion == 1):
        usuario = obtener_usuario_por_id(solicitud["id_usuario"])
        usuario["dias_gastados"] = usuario["dias_gastados"] + dias_solicitados
           
    elif operacion == 2:
        usuario = obtener_usuario_por_id(solicitud["id_usuario"])
        usuario["dias_gastados"] = usuario["dias_gastados"] - dias_solicitados

    if usuario!= None:
        persistencias_usuario.actualizar_usuario(solicitud["id_usuario"],usuario)

def usuario_actualizar_dias_gastados_por_user_id(usuario_id,dias_solicitados,operacion):
    # 1 añade dias utilizados, 2 resta dias utilizados
    usuario = None
    if(operacion == 1):
        usuario = obtener_usuario_por_id(usuario_id)
        usuario["dias_gastados"] = usuario["dias_gastados"] + dias_solicitados
            
    elif operacion == 2:
        usuario = obtener_usuario_por_id(usuario_id)
        usuario["dias_gastados"] = usuario["dias_gastados"] - dias_solicitados

    if usuario!= None:
        persistencias_usuario.actualizar_usuario(usuario_id,usuario)

def usuario_dias_disponibles(usuario_id):
    usuario = obtener_usuario_por_id(usuario_id)
    return usuario["dias_totales"] - usuario ["dias_gastados"]
