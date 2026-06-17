from modulos import interfaz
from modulos import imprimir
from modulos import control_entradas
from modulos import constantes
from modulos import funciones
from modulos import persistencias_usuario
from modulos import persistencias_solicitud

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
        print("4. Salir")
        print("-----------------------")
        
        # Validación de entrada usando tu módulo especializado
        opcion = control_entradas.pedir_entero_en_rango("Seleccione una opción: ", 1, 4)
        
        match opcion:
            case 1:
                print("\n--- SOLICITAR VACACIONES ---")
                
                if dias_disponibles <= 0:
                    print("❌ Error: No le quedan días de vacaciones disponibles.")
                else:
                    print(f"Usted cuenta con {dias_disponibles} días disponibles.")
                    
                    # Solicitar datos temporales indexados según las constantes del sistema
                    # NOMBRES_MESES ayuda a validar de 0 a 11, y los días según el mes
                    mes_idx = control_entradas.pedir_entero_en_rango("Ingrese el número de mes (1-12): ", 1, 12) - 1
                    dia_inicio = control_entradas.pedir_entero_en_rango("Día de inicio: ", 1, 31)
                    dia_fin = control_entradas.pedir_entero_en_rango("Día de fin: ", 1, 31)
                    
                    # Validar consistencia de fechas (regla de negocio en capa 'funciones')
                    if dia_fin < dia_inicio:
                        print("❌ Error: El día de fin no puede ser menor al día de inicio.")
                        continue
                        
                    # Calcular días solicitados
                    dias_solicitados = (dia_fin - dia_inicio) + 1
                    
                    if dias_solicitados > dias_disponibles:
                        print(f"❌ Error: No puede solicitar {dias_solicitados} días. Solo le restan {dias_disponibles}.")
                    else:
                        # Enviar a la capa de lógica/funciones para procesar y persistir en el CSV
                        exito = funciones.registrar_nueva_solicitud(
                            id_usuario=usuario_actual["id_usuario"],
                            mes=mes_idx,
                            inicio=dia_inicio,
                            fin=dia_fin
                        )
                        
                        if exito:
                            print(f"✅ Éxito: Solicitud registrada desde el día {dia_inicio} al {dia_fin}.")
                            # Se asume que entra en estado "Pendiente" hasta aprobación de un Admin
                        else:
                            print("❌ Error: No se pudo procesar la solicitud en este momento.")

            case 2:
                print("\n--- CONSULTA DE SALDO ---")
                # Muestra limpia delegada a la lógica empresarial
                print(f"Usted tiene {dias_disponibles} días disponibles para usufructuar.")
                print(f"(Totales asignados: {usuario_actual['dias_totales']} | Consumidos: {usuario_actual['dias_gastados']})")

            case 3:
                print("\n--- CANCELACIÓN DE SOLICITUDES ---")
                # Primero listamos las solicitudes pendientes del usuario para que elija cuál borrar
                solicitudes_usuario = funciones.obtener_solicitudes_por_usuario(usuario_actual["id_usuario"])
                
                if not solicitudes_usuario:
                    print("❌ Error: Usted no posee solicitudes activas para cancelar.")
                else:
                    # El módulo 'imprimir' se encarga de mostrar la lista formateada
                    imprimir.mostrar_tabla_solicitudes(solicitudes_usuario)
                    
                    id_cancelar = control_entradas.pedir_entero_positivo("Ingrese el ID de la solicitud que desea cancelar: ")
                    
                    # Validar y procesar la eliminación física o lógica en la capa de negocio
                    if funciones.cancelar_solicitud_empleado(id_cancelar, usuario_actual["id_usuario"]):
                        print("✅ Éxito: La solicitud ha sido cancelada y removida del sistema.")
                    else:
                        print("❌ Error: No se encontró la solicitud o no pertenece a su usuario.")

            case 4:
                print("Cerrando sesión administrativa. ¡Hasta luego!")
                ejecutando = False