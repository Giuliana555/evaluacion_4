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
    
  Para acceder a la vista de administrador, es necesario crear un superusuario.
  Ejecuta el siguiente comando para crear uno:
  -py manage.py createsuperuser
  Se te pedirá que ingreses un nombre de usuario, correo electrónico y contraseña

---

## Instalación y configuración

Sigue estos pasos para configurar y ejecutar el proyecto localmente:


1. Clonar el repositorio

git clone https://github.com/tu-usuario/red-social-viajes.git
cd red-social-viajes

2. Entorno virtual
   Si necesitas un entorno virtual  para aislar las dependenciasm debes crearlo antes de instalar las dependencias con el siguiente comando:
   -py -m venv venv
   luego para activarlo debes ingresar:
   -source venv/bin/activate  # Para Linux
   -venv\Scripts\activate # para Windows
   
   
3. Instalar dependencias

Antes de proceder, asegúrate de que tienes instalados Python y pip en tu sistema ejecutando los siguientes comandos en la terminal:
- python --version
- pip --version
  
Nota: Si usas Windows, también puedes probar con py --version para verificar Python.

Una vez confirmada la instalación de Python y pip, instala las dependencias necesarias para ejecutar el proyecto utilizando el archivo requirements.txt:
- pip install -r requirements.txt
  
Debes confirmar que  las dependencias se instalaron correctamente con el siguiente comando:
-pip list

4. Migraciones y servidor
Ejecuta los siguientes comandos en la terminal:

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

El servidor se iniciará en http://127.0.0.1:8000/.
