from modulos import interfaz
from modulos import imprimir
from modulos import control_entradas
from modulos import constantes

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


opcion = control_entradas.pedir_entero_positivo()
dias_disponibles = "dias_totales - dias_gastados"
print(
    "1. Solicitar vacaciones.\n"
    "2. Consultar dias disponibles.\n"
    "3. Solicitar cancelacion. \n"
)
match opcion:
    case 1:
        print("Soicitar vacaciones.")
        print("Consultar base de datos--->")
        if dias_disponibles == 0:
            print("avisar que no quedan dias disponibles")
            print("fin.")#en el diagrama terminaaca esta opcion pero pede volver al menu principal y preguntar si el usuario quiere ahcer otra cosa
        else:
            print(f"tiene {"numero"} dias disponibles")
            fechas = input("fechas de vacaciones")
            persistencia_solicitud.crear_solicitud(fechas)
            print("usted pidio vacaciones desde {"fecha"} hasta {"fecha"}")
            print("solicitud aprobada")
    case 2:
        print("Consultar dias disponibles.")
        dias_disponibles = "dias_totales - dias_gastados"
        print(f"usted tiene {dias_disponibles} dias disponibles")
        #volver al menu

    case 3:
        print("Solicitar cancelacion.")
        persistencia_solicitud.eliminar_solicitud()