Gestor de Vacaciones - Proyecto Integrador
🏫 Institución y Cátedra
Universidad Tecnológica Nacional (UTN)

Materia: Organización Empresarial

Trabajo: Proyecto Integrador Final

Integrantes:

Estudiante 1: [Nombre y Apellido] - Legajo: [Número]

Estudiante 2: [Nombre y Apellido] - Legajo: [Número]

📝 Descripción del Proyecto
El Gestor de Vacaciones es una aplicación de consola desarrollada en Python que simula el flujo organizacional para la solicitud, revisión y control de las vacaciones del personal dentro de una empresa. El sistema permite automatizar un proceso administrativo clave, garantizando la consistencia de los datos, el control de los días disponibles por empleado y la jerarquía de estados en las solicitudes.

El diseño del software se alinea con los conceptos de procesos de negocio, control de gestión y flujos de información estudiados en la cátedra de Organización Empresarial.

🏗️ Arquitectura y Estructura de Archivos
El proyecto sigue un diseño modular para separar las responsabilidades de persistencia, lógica de negocio, validación y presentación:

persistencias.py: Módulo encargado del manejo y lectura/escritura de la base de datos basada en archivos CSV.

funciones.py: Contiene la lógica de negocio central (mediador entre la interfaz y la persistencia).

interfaz.py: Gestiona los menús de navegación y el flujo de pantallas del sistema.

imprimir.py: Módulo especializado de visualización. Recibe listas de datos y las formatea de manera limpia en la consola.

control_entragas.py: Componente de soporte encargado de la captura segura de datos mediante funciones de validación de entradas:

pedir_texto_no_vacio(mensaje)

pedir_entero(mensaje)

pedir_entero_en_rango(mensaje, minimo, maximo)

pedir_entero_positivo(mensaje)

pedir_texto(mensaje)

pedir_opcion_booleana(mensaje)

🗂️ Modelo de Datos (DB basada en CSV)
El sistema persiste la información en dos archivos planos con codificación relacional mediante identificadores:

1. usuarios.csv
   Almacena el perfil del personal, credenciales y saldo de días.

Estructura en archivo: id_usuario, username, contrasena, nombre, perfil, dias_totales, dias_gastados

Estructura de Objeto (Diccionario):
usuario = {
"id_usuario": int(datos[0]),
"username": datos[1],
"contrasena": datos[2],
"nombre": datos[3],
"perfil": datos[4],
"dias_totales": int(datos[5]),
"dias_gastados": int(datos[6])
}

2. solicitudes.csv
   Registra cada una de las peticiones temporales de vacaciones de los empleados.

Estructura en archivo: id_solicitud, id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx, estado

Estructura de Objeto (Diccionario):
solicitud = {
"id_solicitud": int(datos[0]),
"id_usuario": int(datos[1]),
"mes_idx": int(datos[2]),
"dia_inicio_idx": int(datos[3]),
"dia_fin_idx": int(datos[4]),
"estado": datos[5]
}

⚙️ Reglas de Negocio y Constantes
MATRIZ_MESES: Representación interna anual estructurada en matrices por mes (de 28 a 31 días, indexados desde 0) para el control preciso del calendario.

ESTADOS_SOLICITUD: Los estados permitidos y validados son "Pendiente", "Aprobada" y "Rechazada".

NOMBRES_MESES: Mapeo amigable para el usuario de "Enero" a "Diciembre".

Feedback unificado: El sistema responde de manera estandarizada utilizando los prefijos ❌ Error: para fallos de validación o lógica, y ✅ Éxito: para operaciones correctas.

🤖 Contexto de Desarrollo (Prompt de Base para IA)
Para el desarrollo, soporte y mantenimiento de este código, se utilizó el asistente de Inteligencia Artificial Gemini. A continuación se detalla el prompt estricto de contexto que se utilizó para alinear el diseño del software:

Actúa como un desarrollador experto y mi asistente de programación. A partir de ahora, ten en cuenta las bases del proyecto "Gestor de Vacaciones" que te detallo a continuación para el código que desarrollemos:

🌐 Lenguaje
Python

🗂️ Modelo de Datos (DB basada en CSV)
solicitudes.csv: id_solicitud, id_usuario, mes_idx, dia_inicio_idx, dia_fin_idx, estado

usuarios.csv: id_usuario, username, contrasena, nombre, perfil, dias_totales, dias_gastados

Estructura de Objetos (Diccionarios)
usuario = {
"id_usuario": int(datos[0]),
"username": datos[1],
"contrasena": datos[2],
"nombre": datos[3],
"perfil": datos[4],
"dias_totales": int(datos[5]),
"dias_gastados": int(datos[6])
}

solicitud = {
"id_solicitud": int(datos[0]),
"id_usuario": int(datos[1]),
"mes_idx": int(datos[2]),
"dia_inicio_idx": int(datos[3]),
"dia_fin_idx": int(datos[4]),
"estado": datos[5]
}

🧱 Prompt para trabajar con IA
imprimir: Archivo/módulo auxiliar que se encarga exclusivamente de recibir listas de datos (usuarios, solicitudes, etc.) y formatearlas para mostrarlas en pantalla de manera limpia.

interfaz: Archivo/módulo auxiliar que se encarga de mediar entre funciones y menu

funciones: Archivo/módulo auxiliar que se encarga de mediar entre interfaz y persistencias

persistencias: Archivo/módulo auxiliar que se encarga de manejar los csv

control_entragas: contiene funciones para solicitar datos al usuario:
[pedir_texto_no_vacio(mensaje),pedir_entero(mensaje),pedir_entero_en_rango(mensaje, minimo, maximo),pedir_entero_positivo(mensaje),pedir_entero_positivo(mensaje),pedir_texto(mensaje),pedir_opcion_booleana(mensaje)]

⚙️ Constantes y Estructuras del Sistema
MATRIZ_MESES: Representación anual en matrices por mes (de 28 a 31 días, indexados desde 0).

ESTADOS_SOLICITUD: "Pendiente", "Aprobada", "Rechazada".

NOMBRES_MESES: Mapeo amigable para el usuario de "Enero" a "Diciembre".

Mensajes de feedback con prefijos específicos ("❌ Error: ", "✅ Éxito: ").
