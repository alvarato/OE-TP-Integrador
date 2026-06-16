from modulos import interfaz
from modulos import imprimir
from modulos import control_entradas
from modulos import constantes

# del usuario vamos a necesitar el ID Y si el perfil es administrador
USUARIO = interfaz.iniciar_sesion()
print(USUARIO)
interfaz.solicitudes_crear(USUARIO["id_usuario"])

#interfaz.solicitudes_crear(USUARIO["id_usuario"])
#solicitudes_visualizar_por_user_id(USUARIO["id_usuario"])

"""
if USUARIO['perfil' == 'admin']
desplegas tambien las funciones de admin
"""


#todos los expedientes :interfaz.solicitudes_visualizar()
# mas adelante aceptar/denegar solicitud
# interfaz.obtener_solicitudes_por_estado(constantes.ESTADOS_SOLICITUD["PENDIENTE"])