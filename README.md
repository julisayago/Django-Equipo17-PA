# Photogram 

Este es un proyecto de una aplicación de intercambio de fotos diseñada para conectar a las personas a través de imágenes.

# Links importantes:
-Link a la presentación en Google Slides: https://docs.google.com/presentation/d/1apePV5AOeZxayK8LSAsnASqIiOD_Jm51QBIrHbanles/edit#slide=id.g21541b24c8c_0_0
-Link al video: https://drive.google.com/file/d/1tRAscbLIZYFnDteMYRIhYSR-gB7ZDtK9/view?usp=sharing

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior

## Instalación

1. Clona el repositorio:
    ```
    git clone https://github.com/julisayago/Django-Equipo17-PA.git
    cd red_social
    ```

2. Crea un entorno virtual:
    ```
    python -m venv env
    source env/bin/activate   # En Windows: env\Scripts\activate
    ```

3. Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:
    ```
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración (opcional):
    ```
    python manage.py createsuperuser
    ```

6. Ejecuta el servidor de desarrollo:
    ```
    python manage.py runserver
    ```

## Uso

1. Accede a la página de inicio de sesión en `http://127.0.0.1:8000/`.
2. Inicia sesión con tus credenciales.
3. Navega a la página de inicio.
4. Desde la página de inicio, accede a tu perfil.

## Solución de errores
- 'pip' is not recognized as an internal or external command, operable program or batch file.
Solución:
Instalar pip desde la terminal: https://pip.pypa.io/en/stable/installation/
Además de instalar pip en el entorno, pip está disponible como una aplicación zip independiente. Se puede descargar desde: https://bootstrap.pypa.io/pip/pip.pyz

## Acceso al Panel de Administración

1. Accede al panel de administración en `http://127.0.0.1:8000/admin/`.
2. Inicia sesión con las credenciales de superusuario que creaste previamente durante la instalación.


