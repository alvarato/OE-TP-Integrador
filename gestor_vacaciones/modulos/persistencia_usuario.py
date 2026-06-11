from constantes import TEXTO_ERROR_GENERICO, TEXTO_EXITO_GENERICO

import os

# --- 1. READ (Leer / Cargar) ---
def cargar_usuarios():
    """
    Lee 'usuarios.csv' y devuelve una lista de diccionarios con los datos de los empleados.
    """
    lista_usuarios = []
    if not os.path.exists("usuarios.csv"):
        # Si el archivo no existe, creamos la base con sus encabezados oficiales
        try:
            with open("usuarios.csv", "w", encoding="utf-8") as archivo:
                archivo.write("id_usuario,username,contrasena,nombre,perfil,dias_totales,dias_gastados\n")
        except Exception as e:
            print(f"{TEXTO_ERROR_GENERICO}No se pudo crear el archivo de usuarios: {e}")
        return lista_usuarios

    try:
        with open("usuarios.csv", "r", encoding="utf-8") as archivo:
            archivo.readline()  # Saltar encabezados
            for linea in archivo:
                datos = linea.strip().split(",")
                if not datos or datos == ['']:
                    continue
                
                usuario = {
                    "id_usuario": int(datos[0]),
                    "username": datos[1],
                    "contrasena": datos[2],
                    "nombre": datos[3],
                    "perfil": datos[4],
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
    Registra un nuevo usuario en el sistema. Autoincrementa el ID y pone
    por defecto los días gastados en 0.
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
        with open("usuarios.csv", "a", encoding="utf-8") as archivo:
            linea = f"{nuevo_id},{username},{contrasena},{nombre},{perfil},{dias_totales},{dias_gastados_inicial}\n"
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
    (por ejemplo: {'dias_gastados': 5} o {'contrasena': 'nueva123'}).
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
        with open("usuarios.csv", "w", encoding="utf-8") as archivo:
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
    Elimina un usuario del archivo CSV mediante su ID.
    """
    usuarios = cargar_usuarios()
    longitud_inicial = len(usuarios)
    
    usuarios_filtrados = [u for u in usuarios if u["id_usuario"] != id_usuario]

    if len(usuarios_filtrados) == longitud_inicial:
        print(f"{TEXTO_ERROR_GENERICO}No se encontró el usuario con ID #{id_usuario} para eliminar.")
        return False

    try:
        with open("usuarios.csv", "w", encoding="utf-8") as archivo:
            archivo.write("id_usuario,username,contrasena,nombre,perfil,dias_totales,dias_gastados\n")
            for u in usuarios_filtrados:
                linea = f"{u['id_usuario']},{u['username']},{u['contrasena']},{u['nombre']},{u['perfil']},{u['dias_totales']},{u['dias_gastados']}\n"
                archivo.write(linea)
        print(f"{TEXTO_EXITO_GENERICO}Usuario #{id_usuario} eliminado correctamente.")
        return True
    except Exception as e:
        print(f"{TEXTO_ERROR_GENERICO}No se pudo actualizar el archivo al eliminar usuario: {e}")
        return False