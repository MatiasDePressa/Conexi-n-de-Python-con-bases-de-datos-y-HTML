#pip install flask
#pip install flask flask-mysql
#pip install mysql-connector-python


from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "tu_user",
    password = "tu_password",
    database = "escuela"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingresar_alumnos')
def ingresar_alumnos():
    return render_template('ingresar_alumnos.html')

@app.route('/ingresar', methods=['POST'])
def ingresar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    carrera = request.form['carrera']
    nota = float(request.form['nota'])

    query = "INSERT INTO alumnos (nombre, apellido, edad, carrera, nota) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, apellido, edad, carrera, nota))
    db.commit()

    return redirect('/')

@app.route('/mostrar')
def mostrar():
    cursor.execute("SELECT id ,nombre, apellido, edad, carrera, nota FROM alumnos")
    alumno = cursor.fetchall()
    return render_template('mostrar_alumnos.html', alumnos=alumno)

@app.route('/actualizar_alumno', methods=['GET'])
def actualizar_alumno_form():
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()

    return render_template('actualizar_alumnos.html', alumnos=alumnos, alumnos_json=jsonify(alumnos).json)

@app.route('/actualizar', methods=['POST'])
def actualizar_alumno():
    idA = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    carrera = request.form['carrera']
    nota = float(request.form['nota'])

    query = "UPDATE alumnos SET nombre = %s, apellido = %s, edad = %s, carrera = %s, nota = %s WHERE id = %s"

    cursor.execute(query, (nombre, apellido, edad, carrera, nota, idA))
    
    return redirect('/mostrar')

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_alumno(id):
    cursor.execute("DELETE FROM alumnos WHERE id=%s", (id,))
    db.commit()

    return redirect('/mostrar')


if __name__ == '__main__':
    app.run(debug=True)