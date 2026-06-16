from .constantes import TEXTO_ERROR_GENERICO, TEXTO_EXITO_GENERICO

import os

# Definimos la ruta hacia el archivo de usuarios en la carpeta data
RUTA_USUARIOS_CSV = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "usuarios.csv"))

def obtener_mapa_usuarios_nombres():
    """
    Lee 'usuarios.csv' y devuelve un diccionario (mapa)
    donde la Key es el 'id_usuario' (int) y el Value es el 'nombre' (str).
    """
    mapa_usuarios = {}

    if not os.path.exists(RUTA_USUARIOS_CSV):
        print(f"{TEXTO_ERROR_GENERICO}No se encontró el archivo de usuarios en {RUTA_USUARIOS_CSV}")
        return mapa_usuarios

    try:
        with open(RUTA_USUARIOS_CSV, "r", encoding="utf-8") as archivo:
            archivo.readline()  # Saltar la línea de encabezados si existe
            for linea in archivo:
                datos = linea.strip().split(",")
                if not datos or datos == ['']:
                    continue
                
                # Basado en tu estructura: datos[0] es id_usuario, datos[3] es nombre
                id_usuario = int(datos[0])
                nombre_completo = datos[3].strip()
                
                # Asignamos al mapa: { id: "Nombre Apellido" }
                mapa_usuarios[id_usuario] = nombre_completo
                
        return mapa_usuarios
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}Error al generar el mapa de usuarios: {e}")
        return {}

# --- 1. READ (Leer / Cargar) ---
def cargar_usuarios():
    """
    Lee 'usuarios.csv' usando RUTA_USUARIOS_CSV y devuelve una lista de diccionarios con los datos de los empleados.
    """
    lista_usuarios = []
    if not os.path.exists(RUTA_USUARIOS_CSV):
        # Si el archivo no existe, creamos la carpeta base y el archivo con sus encabezados oficiales
        try:
            os.makedirs(os.path.dirname(RUTA_USUARIOS_CSV), exist_ok=True)
            with open(RUTA_USUARIOS_CSV, "w", encoding="utf-8") as archivo:
                archivo.write("id_usuario,username,contrasena,nombre,perfil,dias_totales,dias_gastados\n")
        except Exception as e:
            print(f"{TEXTO_ERROR_GENERICO}No se pudo crear el archivo de usuarios: {e}")
        return lista_usuarios

    try:
        with open(RUTA_USUARIOS_CSV, "r", encoding="utf-8") as archivo:
            archivo.readline()  # Saltar encabezados
            for linea in archivo:
                datos = linea.strip().split(",")
                if not datos or datos == ['']:
                    continue
                
                usuario = {
                    "id_usuario": int(datos[0]),
                    "username": datos[1].strip(),
                    "contrasena": datos[2].strip(),
                    "nombre": datos[3].strip(),
                    "perfil": datos[4].strip(),
                    "dias_totales": int(datos[5]),
                    "dias_gastados": int(datos[6])
                }
                lista_usuarios.append(usuario)
        return lista_usuarios
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}Error al cargar usuarios: {e}")
        return []


# --- 2. CREATE (Crear / Registrar Usuario) ---
def crear_usuario(username, contrasena, nombre, perfil="empleado", dias_totales=30):
    """
    Registra un nuevo usuario en el sistema usando RUTA_USUARIOS_CSV. 
    Autoincrementa el ID y pone por defecto los días gastados en 0.
    """
    usuarios_actuales = cargar_usuarios()
    
    # Validar que el username no esté repetido
    for u in usuarios_actuales:
        if u["username"].lower() == username.lower():
            print(f"{TEXTO_ERROR_GENERICO}El nombre de usuario '{username}' ya existe.")
            return False

    # Auto-incremento del ID de usuario
    nuevo_id = max([u["id_usuario"] for u in usuarios_actuales], default=0) + 1
    dias_gastados_inicial = 0

    try:
        with open(RUTA_USUARIOS_CSV, "a", encoding="utf-8") as archivo:
            linea = f"{nuevo_id},{username.strip()},{contrasena.strip()},{nombre.strip()},{perfil.strip()},{dias_totales},{dias_gastados_inicial}\n"
            archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Usuario '{username}' registrado con ID #{nuevo_id}.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo guardar el usuario: {e}")
        return False


# --- 3. UPDATE (Actualizar Datos / Días Gastados) ---
def actualizar_usuario(id_usuario, datos_nuevos):
    """
    Recibe el ID del usuario y un diccionario con los campos que se quieren cambiar
    utilizando RUTA_USUARIOS_CSV para reescribir los datos modificados.
    """
    usuarios = cargar_usuarios()
    encontrado = False

    for u in usuarios:
        if u["id_usuario"] == id_usuario:
            # Reemplazamos solo los datos que vengan en el diccionario 'datos_nuevos'
            for clave, valor in datos_nuevos.items():
                if clave in u:
                    u[clave] = valor
            encontrado = True
            break

    if not encontrado:
        print(f"{TEXTO_ERROR_GENERICO}No se encontró el usuario con ID #{id_usuario}.")
        return False

    # Reescribir el archivo con las modificaciones
    try:
        with open(RUTA_USUARIOS_CSV, "w", encoding="utf-8") as archivo:
            archivo.write("id_usuario,username,contrasena,nombre,perfil,dias_totales,dias_gastados\n")
            for u in usuarios:
                linea = f"{u['id_usuario']},{u['username']},{u['contrasena']},{u['nombre']},{u['perfil']},{u['dias_totales']},{u['dias_gastados']}\n"
                archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Datos del usuario #{id_usuario} actualizados.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo actualizar el archivo de usuarios: {e}")
        return False


# --- 4. DELETE (Eliminar Usuario) ---
def eliminar_usuario(id_usuario):
    """
    Elimina un usuario de RUTA_USUARIOS_CSV localizándolo mediante su ID.
    """
    usuarios = cargar_usuarios()
    longitud_inicial = len(usuarios)
    
    # Filtramos para excluir al usuario que se desea eliminar
    usuarios_filtrados = [u for u in usuarios if u["id_usuario"] != id_usuario]

    if len(usuarios_filtrados) == longitud_inicial:
        print(f"{TEXTO_ERROR_GENERICO}No se encontró el usuario con ID #{id_usuario} para eliminar.")
        return False

    # Volver a escribir en el archivo RUTA_USUARIOS_CSV sin el registro eliminado
    try:
        with open(RUTA_USUARIOS_CSV, "w", encoding="utf-8") as archivo:
            archivo.write("id_usuario,username,contrasena,nombre,perfil,dias_totales,dias_gastados\n")
            for u in usuarios_filtrados:
                linea = f"{u['id_usuario']},{u['username']},{u['contrasena']},{u['nombre']},{u['perfil']},{u['dias_totales']},{u['dias_gastados']}\n"
                archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Usuario #{id_usuario} eliminado correctamente.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo actualizar el archivo al eliminar el usuario: {e}")
        return False