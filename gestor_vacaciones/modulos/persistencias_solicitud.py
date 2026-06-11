from constantes import TEXTO_ERROR_GENERICO, TEXTO_EXITO_GENERICO, ESTADOS_SOLICITUD

import os

# --- 1. READ (Leer / Cargar) ---
def cargar_solicitudes():
    """
    Lee 'solicitudes.csv' y devuelve una lista de diccionarios.
    """
    lista_solicitudes = []
    if not os.path.exists("solicitudes.csv"):
        # Si el archivo no existe, lo creamos con sus encabezados
        try:
            with open("solicitudes.csv", "w", encoding="utf-8") as archivo:
                archivo.write("id_solicitud,id_usuario,mes_idx,dia_inicio_idx,dia_fin_idx,estado\n")
        except Exception as e:
            print(f"{TEXTO_ERROR_GENERICO}No se pudo crear el archivo base: {e}")
        return lista_solicitudes

    try:
        with open("solicitudes.csv", "r", encoding="utf-8") as archivo:
            archivo.readline()  # Saltar encabezados
            for linea in archivo:
                datos = linea.strip().split(",")
                if not datos or datos == ['']:
                    continue
                
                solicitud = {
                    "id_solicitud": int(datos[0]),
                    "id_usuario": int(datos[1]),
                    "mes_idx": int(datos[2]),
                    "dia_inicio_idx": int(datos[3]),
                    "dia_fin_idx": int(datos[4]),
                    "estado": datos[5]
                }
                lista_solicitudes.append(solicitud)
        return lista_solicitudes
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}Error al cargar solicitudes: {e}")
        return []


# --- 2. CREATE (Crear / Insertar) ---
def crear_solicitud(id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx):
    """
    Genera una nueva solicitud en estado PENDIENTE y la escribe en el CSV.
    Calcula el ID de forma autoincremental.
    """
    solicitudes_actuales = cargar_solicitudes()
    
    # Auto-incremento del ID
    if solicitudes_actuales:
        nuevo_id = max(s["id_solicitud"] for s in solicitudes_actuales) + 1
    else:
        nuevo_id = 1

    nuevo_estado = ESTADOS_SOLICITUD["PENDIENTE"]

    try:
        with open("solicitudes.csv", "a", encoding="utf-8") as archivo:
            linea = f"{nuevo_id},{id_usuario},{mes_idx},{dia_inicio_idx},{dia_fin_idx},{nuevo_estado}\n"
            archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Solicitud #{nuevo_id} creada correctamente.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo guardar la solicitud: {e}")
        return False


# --- 3. UPDATE (Actualizar Estado) ---
def actualizar_estado_solicitud(id_solicitud, nuevo_estado):
    """
    Busca una solicitud por su ID y cambia su estado (ej. APROBADA o RECHAZADA).
    Reescribe el archivo CSV con el cambio.
    """
    solicitudes = cargar_solicitudes()
    encontrado = False

    for s in solicitudes:
        if s["id_solicitud"] == id_solicitud:
            s["estado"] = nuevo_estado
            encontrado = False  # Usado para control
            encontrado = True
            break

    if not encontrado:
        print(f"{TEXTO_ERROR_GENERICO}No se encontró la solicitud #{id_solicitud}.")
        return False

    # Reescribir el archivo con el dato modificado
    try:
        with open("solicitudes.csv", "w", encoding="utf-8") as archivo:
            archivo.write("id_solicitud,id_usuario,mes_idx,dia_inicio_idx,dia_fin_idx,estado\n")
            for s in solicitudes:
                linea = f"{s['id_solicitud']},{s['id_usuario']},{s['mes_idx']},{s['dia_inicio_idx']},{s['dia_fin_idx']},{s['estado']}\n"
                archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Solicitud #{id_solicitud} actualizada a '{nuevo_estado}'.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo actualizar el archivo: {e}")
        return False


# --- 4. DELETE (Eliminar) ---
def eliminar_solicitud(id_solicitud):
    """
    Elimina una solicitud del archivo CSV mediante su ID.
    (Útil si un empleado cancela una solicitud antes de ser aprobada).
    """
    solicitudes = cargar_solicitudes()
    longitud_inicial = len(solicitudes)
    
    # Filtramos la lista dejando fuera la que queremos borrar
    solicitudes_filtradas = [s for s in solicitudes if s["id_solicitud"] != id_solicitud]

    if len(solicitudes_filtradas) == longitud_inicial:
        print(f"{TEXTO_ERROR_GENERICO}No se encontró la solicitud #{id_solicitud} para eliminar.")
        return False

    try:
        with open("solicitudes.csv", "w", encoding="utf-8") as archivo:
            archivo.write("id_solicitud,id_usuario,mes_idx,dia_inicio_idx,dia_fin_idx,estado\n")
            for s in solicitudes_filtradas:
                linea = f"{s['id_solicitud']},{s['id_usuario']},{s['mes_idx']},{s['dia_inicio_idx']},{s['dia_fin_idx']},{s['estado']}\n"
                archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Solicitud #{id_solicitud} eliminada correctamente.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo actualizar el archivo al eliminar: {e}")
        return False

