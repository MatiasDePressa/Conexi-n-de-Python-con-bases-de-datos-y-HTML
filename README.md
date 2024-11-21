# Proyecto Flask: Gestión de Alumnos

Este proyecto consiste en una aplicación web sencilla para gestionar alumnos utilizando Flask y MySQL. La aplicación permite ingresar, mostrar, actualizar y eliminar alumnos.

## Requisitos

- Python 3
- Flask
- MySQL
- Un servidor MySQL como XAMPP para ejecutar la base de datos

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/MatiasDePressa/python-proyecto-flask.git
   cd proyecto-flask
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install flask flask-mysql mysql-connector-python
   ```

4. Configura el servidor MySQL:
   - Descarga e instala XAMPP desde [apachefriends.org](https://www.apachefriends.org/index.html).
   - Inicia el servidor MySQL desde el panel de control de XAMPP.
   - Crea una base de datos llamada `escuela`.
   - Crea la tabla `alumnos` con la siguiente estructura:
     ```sql
     CREATE DATABASE IF NOT EXISTS escuela

     USE escuela;

     CREATE TABLE alumnos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255) NOT NULL,
       apellido VARCHAR(255) NOT NULL,
       edad INT NOT NULL,
       carrera VARCHAR(255) NOT NULL,
       nota DECIMAL(4,2) NOT NULL
     );
     ```

5. Configura las credenciales de la base de datos en `script.py`:
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="tu_user",
       password="tu_password",
       database="escuela"
   )
   ```

## Uso

1. Inicia la aplicación Flask:
   ```bash
   python script.py
   ```

2. Abre tu navegador y ve a `http://localhost:5000`.

3. Usa las siguientes rutas para gestionar alumnos:
   - `/` : Página principal con opciones para ingresar y mostrar alumnos.
   - `/ingresar_alumnos` : Formulario para ingresar nuevos alumnos.
   - `/mostrar` : Lista de todos los alumnos con opciones para actualizar o eliminar.

## Estructura del Proyecto

- `script.py` : Archivo principal con la lógica del backend en Flask.
- `templates/index.html` : Página principal.
- `templates/ingresar_alumnos.html` : Formulario para ingresar nuevos alumnos.
- `templates/mostrar_alumnos.html` : Página para mostrar y eliminar alumnos.
- `templates/actualizar_alumnos.html` : Formulario para actualizar información de los alumnos.
- `static/css/style.css` : Archivo CSS para estilos.
