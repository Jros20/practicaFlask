#BLOQUE IMPORT
import os
import json
#BLOQUE APERTURA ARCHIVO JSON
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) #-> Detectamos el directorio de este archivo ".py" que contiene este código.
my_file = os.path.join(THIS_FOLDER + '/DB/' 'bbdd.json') #-> A ese directorio le sumamos el del archivo. La ruta total se almacena en my_file
#Aquí "os" detecta el directorio donde se ejecuta nuestro archivo python es decir en este caso "models.py" y a partir de allí almacena esta ruta en THIS_FOLDER. Luego ya sabiendo que la ruta es donde está "models.py" bastará agregarle el directorio DB y finalmente indicar el nombre de archivo.
# --> Cargar archivo JSON   
with open (my_file, "r") as f: #->Abrimos pasando como arg la variable my_file que contiene ruta completa Y ALMACENAMOS EN "f"
    datos = json.load(f) #-> Almacenamos en la variable "datos" la interpreteación de nuestro JSON que está almacenado en "f"
#Ahora datos es un diccionario.
#Almacenamos los diccionarios en una sola variable:
datos_personas = datos['Personas']
#Ahora "datos_personas" almacena los diccionarios.
#Así que nos basta con indicar el index de la lista correspondiente y el nombre de CLAVE PARA IMPRIMIR UN VALOR
print(datos_personas[0]['test'])

class Persona(object):
    def __init__(self, id, nombre, apellido, apodo, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.direccion = direccion
persona_test = Persona(0, "Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net").__dict__
print(persona_test)