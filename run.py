from flask import Flask, render_template, request
#Crear app medante instancia
app = Flask(__name__)
#Crear rutas con sus correspondientes funciones
@app.route('/', methods=['GET', 'POST'])
def index():
 if request.method == 'POST':
        nombre = request.form['Nombre']
        return render_template('/index.html', nombre = nombre)
 else:
        return render_template('/index.html')
 
@app.route('/mis-proyectos')
def mostrarproyectos():
    return 'Aquí se mostrarán mis proyectos'
#Ejecutar nuestra app cuando ejecutemos este archivo run.py
if __name__ == '__main__':
    app.run(debug=True)