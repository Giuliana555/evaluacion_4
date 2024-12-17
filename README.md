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
