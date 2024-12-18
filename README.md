# Red Social de Viajes

Este es un sitio web donde los usuarios pueden compartir sus experiencias de viaje, ver publicaciones de otros usuarios, editar o eliminar sus propias publicaciones.  

---

## Funcionalidades

- **Usuarios comunes**:
  - Iniciar sesión o registrarse.
  - Ver publicaciones propias y de otros usuarios.
  - Editar y eliminar sus propias publicaciones.

- **Administrador**:
  - Ver todos los usuarios registrados.
  - Ver todas las publicaciones existentes.
  - Gestionar la información de ciudades.

---

## Instalación y configuración

Sigue estos pasos para configurar y ejecutar el proyecto localmente:


1. Clonar el repositorio

git clone https://github.com/tu-usuario/red-social-viajes.git
cd red-social-viajes


2. Instalar dependencias
Es necesario instalar las siguientes bibliotecas para ejecutar el proyecto:

- install django
- pip install djangorestframework
- pip install requests

3. Migraciones y servidor
Ejecuta los siguientes comandos en la terminal:

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

El servidor se iniciará en http://127.0.0.1:8000/.

El servidor se iniciará en http://127.0.0.1:8000/.

## Uso de la API

## Autenticación
Endpoint: /api/token/
Método: POST
Parámetros:
username: Nombre de usuario registrado.
password: Contraseña del usuario.
Descripción: Devuelve un token de autenticación que debe incluirse en las cabeceras de futuras solicitudes como:
Authorization: Token <tu_token>.
Destinos
Listar Destinos
Endpoint: /api/destinos/
Método: GET
Descripción: Devuelve una lista de todos los destinos disponibles en formato JSON.

    [
      {"id": 1, "nombre": "París", "ubicacion": "Francia"},
      {"id": 2, "nombre": "Tokio", "ubicacion": "Japón"}
    ]


## Publicaciones

Filtrar Publicaciones
Endpoint: /api/publicaciones/filtrar/
Método: GET
Parámetros Opcionales:
usuario: ID del usuario para filtrar publicaciones específicas.
destino: ID del destino para filtrar publicaciones relacionadas.
Descripción: Devuelve una lista paginada de publicaciones según los filtros proporcionados.

    {
      "count": 2,
      "next": null,
      "previous": null,
      "results": [
        {"id": 1, "titulo": "Viaje a París", "usuario": 1, "destino": 1, "contenido": "Hermoso viaje!"},
        {"id": 2, "titulo": "Aventura en Tokio", "usuario": 2, "destino": 2, "contenido": "Increíble experiencia!"}
      ]
    }


## Gestión de Usuarios

## Listar Usuarios

Endpoint: /usuarios/
Método: GET
Requiere: Ser superusuario autenticado.
Descripción: Devuelve una lista de todos los usuarios registrados.
Editar Usuario

Endpoint: /usuarios/<id>/editar/
Método: POST
Parámetros:
nombre: Nuevo nombre del usuario.
correo: Nuevo correo del usuario.
ubicacion: Nueva ubicación del usuario.
Descripción: Permite actualizar los datos de un usuario específico.
Eliminar Usuario

Endpoint: /usuarios/<id>/eliminar/
Método: POST
Descripción: Elimina a un usuario del sistema tras confirmar la operación.
Con esta API, puedes integrar la funcionalidad del proyecto en aplicaciones cliente o automatizar tareas mediante scripts.
Si necesitas más información o ejemplos, no dudes en consultarlo en los comentarios del código o la documentación del proyecto. """

