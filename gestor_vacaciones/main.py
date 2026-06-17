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

#usuario_actual = log_in()
usuario_actual = funciones.verificar_login("admin", "admin")

def menu_empleado(usuario_actual):
    """
    Controla el flujo de opciones para un perfil de empleado regular.
    Recibe el diccionario del 'usuario_actual' autenticado.
    """
    ejecutando = True
    
    while ejecutando:
        # 1. Cálculo de variables de negocio
        dias_disponibles = usuario_actual["dias_totales"] - usuario_actual["dias_gastados"]
        
        # 2. Renderizado de la interfaz
        print("\n=== MENÚ DE EMPLEADO ===")
        print("1. Solicitar vacaciones")
        print("2. Consultar días disponibles")
        print("3. Solicitar cancelación de solicitud")
        print("4. Mis Solicitudes")
        print("5. Salir")
        print("-----------------------")
        
        # Validación de entrada usando tu módulo especializado
        opcion = control_entradas.pedir_entero_en_rango("Seleccione una opción: ", 1, 4)
        
        match opcion:
            case 1:
                print("\n--- SOLICITAR VACACIONES ---")
                
                if dias_disponibles <= 0:
                    print("❌ Error: No le quedan días de vacaciones disponibles.")
                else:
                    interfaz.solicitudes_crear(usuario_actual["id_usuario"])

            case 2:
                print("\n--- CONSULTA DE SALDO ---")
                print(f"Usted tiene {dias_disponibles} días disponibles para usufructuar.")
                print(f"(Totales asignados: {usuario_actual['dias_totales']} | Consumidos: {usuario_actual['dias_gastados']})")

            case 3:
                print("\n--- CANCELACIÓN DE SOLICITUDES ---")
                interfaz.solicitudes_obtener_por_estado(constantes.ESTADOS_SOLICITUD["PENDIENTE"],usuario_actual["id_usuario"],usuario_actual["nombre"])
                interfaz.solicitudes_cancelar_solicitud(usuario_actual["id_usuario"])
                
            case 4:
                interfaz.solicitudes_visualizar_por_user_id(usuario_actual["id_usuario"],usuario_actual["nombre"])
            case 5:
                print("Cerrando sesión administrativa. ¡Hasta luego!")
                ejecutando = False

menu_empleado(usuario_actual)