from .constantes import TEXTO_ERROR_GENERICO,NOMBRES_MESES, TEXTO_EXITO_GENERICO, ESTADOS_SOLICITUD

def lineas():
    print("---------------------------------")


def espacio():
    print("\n")



def solicitudes(lista_solicitudes,mapa_usuarios):
    """
    Recibe una lista de diccionarios de solicitudes y las imprime 
    de forma legible y tabulada en la consola.
    """
    if not lista_solicitudes:
        print("\n--- No hay solicitudes registradas para mostrar ---")
        return

    
    _cabezera_solicitudes()

    for sol in lista_solicitudes:
        try:
            # Obtenemos el nombre del mes usando el índice
            nombre_mes = NOMBRES_MESES[sol["mes_idx"]]
            nombre_empleado = ""
            
            if isinstance(mapa_usuarios, str):
                nombre_empleado = mapa_usuarios
            else:
                nombre_empleado = mapa_usuarios[sol["id_usuario"]]
            # Sumamos 1 a los índices de los días para mostrárselos al usuario de forma natural (1 al 31)
            dia_inicio = sol["dia_inicio_idx"] + 1
            dia_fin = sol["dia_fin_idx"] + 1
            
            # Imprimimos la fila alineando los textos a la izquierda (<) con sus anchos correspondientes
            _imprimir_fila_solicitud(sol, nombre_empleado, nombre_mes, dia_inicio, dia_fin)
            
                  
        except IndexError:
            print(f"{TEXTO_ERROR_GENERICO}Índice de mes fuera de rango en la solicitud #{sol.get('id_solicitud')}")
        except KeyError as e:
            print(f"{TEXTO_ERROR_GENERICO}Falta el campo {e} en la estructura de la solicitud.")

    print("=" * 75 + "\n")

def _cabezera_solicitudes():
    # 1. Cabecera corregida con "Empleado" y los separadores '|' alineados
    print("\n" + "=" * 75)
    print("=====================================================================================")
    print(f"{'ID Sol.':<10} | {'Empleado':<22} | {'Mes':<12} | {'Día Inicio':<12} | {'Día Fin':<10} | {'Estado':<10}")
    print("-------------------------------------------------------------------------------------")

def _imprimir_fila_solicitud(sol, nombre_empleado, nombre_mes, dia_inicio, dia_fin):
    """
    Imprime una única fila de solicitud con un formato tabulado y alineado.
    """
    print(
        f"{sol['id_solicitud']:<10} | "
        f"{nombre_empleado:<22} | "
        f"{nombre_mes:<12} | "
        f"{dia_inicio:<12} | "
        f"{dia_fin:<10} | "
        f"{sol['estado']:<10}"
    )