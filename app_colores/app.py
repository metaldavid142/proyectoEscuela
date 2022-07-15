import os
from flask import Flask, render_template
from pymongo import MongoClient

app=Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")
# Definimos la uri de conexión a mongodb local
MONGO_URI = "mongodb://localhost"
# Creamos la conexión
client = MongoClient(MONGO_URI)

# Creamos la base de datos
db = client["escuela"]
estudiantes = db["estudiantes"] # Creamos la colección
docentes = db["docentes"] # Creamos la colección

@app.route("/")
def index():
    return render_template("layouts/index.html")

@app.route("/docente")
def teacher():
    return render_template("layouts/login_docente.html")

@app.route("/estudiante")
def student():
    return render_template("layouts/login_estudiante.html")

@app.route("/colores")
def colors():
    return render_template("layouts/colores.html")

@app.route("/test")
def test():
    return render_template("layouts/test.html")

if __name__=='__main__':
    app.run(debug=True, port=5000)
