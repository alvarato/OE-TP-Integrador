from modulos import interfaz
from modulos import imprimir
from modulos import control_entradas
from modulos import constantes

#eliminar luego
from modulos import funciones

# # del usuario vamos a necesitar el ID Y si el perfil es administrador
# USUARIO = interfaz.iniciar_sesion()
# print(USUARIO)
# interfaz.solicitudes_crear(USUARIO["id_usuario"])

# #interfaz.solicitudes_crear(USUARIO["id_usuario"])
# #solicitudes_visualizar_por_user_id(USUARIO["id_usuario"])

# """
# if USUARIO['perfil' == 'admin']
# desplegas tambien las funciones de admin
# """


# #todos los expedientes :interfaz.solicitudes_visualizar()
# # mas adelante aceptar/denegar solicitud
# # interfaz.obtener_solicitudes_por_estado(constantes.ESTADOS_SOLICITUD["PENDIENTE"])


def log_in():
    return interfaz.iniciar_sesion()


def menu_empleado(usuario_actual):
    """
    Controla el flujo de opciones para un perfil de empleado regular.
    Recibe el diccionario del 'usuario_actual' autenticado.
    """
    ejecutando = True
    
    while ejecutando:
        
        # 2. Renderizado de la interfaz
        print("\n=== MENÚ DE EMPLEADO ===")
        print("1. Solicitar vacaciones")
        print("2. Consultar días disponibles")
        print("3. Cancelar de solicitud")
        print("4. Mis Solicitudes")
        print("5. Salir")
        print("-----------------------")
        
        # Validación de entrada usando tu módulo especializado
        opcion = control_entradas.pedir_entero_en_rango("Seleccione una opción: ", 1, 5)
        
        match opcion:
            case 1:
                print("\n--- SOLICITAR VACACIONES ---")
                # 1. Cálculo de variables de negocio
                dias_disponibles = interfaz.usuario_dias_disponibles(usuario_actual["id_usuario"])
                if dias_disponibles <= 0:
                    print("❌ Error: No le quedan días de vacaciones disponibles.")
                else:
                    interfaz.solicitudes_crear(usuario_actual["id_usuario"])

            case 2:
                print("\n--- CONSULTA DE SALDO ---")
                dias_disponibles = interfaz.usuario_dias_disponibles(usuario_actual["id_usuario"])
                print(f"Usted tiene {dias_disponibles} días disponibles para usufructuar.")

            case 3:
                print("\n--- CANCELAR DE SOLICITUD ---")
                interfaz.solicitudes_obtener_por_estado(constantes.ESTADOS_SOLICITUD["PENDIENTE"],usuario_actual["id_usuario"],usuario_actual["nombre"])
                interfaz.solicitudes_cancelar_solicitud(usuario_actual["id_usuario"])
                
            case 4:
                interfaz.solicitudes_visualizar_por_user_id(usuario_actual["id_usuario"],usuario_actual["nombre"])
            case 5:
                print("Cerrando sesión administrativa. ¡Hasta luego!")
                ejecutando = False


def menu_admin(usuario_actual):
    ejecutando = True
    
    while ejecutando:
        
        print("\n=== MENÚ DE ADMIN ===")
        print("1. Aceptar/Rechazar solicitudes")
        print("2. Ver Solicitudes")
        print("3. Salir")
        print("-----------------------")
        
        # Validación de entrada usando tu módulo especializado
        opcion = control_entradas.pedir_entero_en_rango("Seleccione una opción", 1, 3)
        
        match opcion:
            case 1:
                print("\n--- Aceptar/Rechazar solicitudes ---")
                print("1. Aceptar solicitud")
                print("2. Rechazar solicitud")
                accion = control_entradas.pedir_entero_en_rango("Seleccione una opción",1,2)
                interfaz.solicitudes_obtener_por_estado(constantes.ESTADOS_SOLICITUD["PENDIENTE"],None,None)
                if accion == 1:
                    interfaz.solicitudes_aprobar_solicitud()
                elif accion == 2:
                    interfaz.solicitudes_rechazar_solicitud()
            case 2:
               interfaz.solicitudes_visualizar()
            case 3:
                print("Cerrando sesión administrativa. ¡Hasta luego!")
                ejecutando = False



def ejecutor_sistema():
    usuario_actual = None
    print("\n--- INICIO DE SESIÓN ---")
    for i in range(3):
        print(f"Intento de inicio de sesión {i + 1}/3")
        usuario_actual = log_in()
        if usuario_actual != None:
            break

    if usuario_actual != None:   
        if usuario_actual["perfil"] == constantes.PERFILES["ADMIN"]:
            menu_admin(usuario_actual)
        else:
            menu_empleado(usuario_actual)
    else:
        print(f"{constantes.TEXTO_ERROR_GENERICO}no se puedo iniciar sesión")

ejecutor_sistema()         