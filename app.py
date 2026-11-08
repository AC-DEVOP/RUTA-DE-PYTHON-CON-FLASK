from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

@app.route("/")
def HolaFlask():
    return "HOLA FLASK"

## Ejercicio 1)  Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de
## 30%, 30%, y 40% respectivamente. 

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas (nota1=0,nota2=0,nota3=0):
    resultado=(nota1*0.3) + (nota2*0.3) +(nota3*0.4)
    return f"El resultado es: {resultado} <hr>"

## Ejercicio 2) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades/")
@app.route("/edades/<int:edad>")
def edades(edad = 0):
   if edad < 18:
       R = "Menor de edad"
   elif edad >= 18 and edad < 60: 
       R = "Adulto"
   elif edad >= 60:
       R = "Adulto Mayor"
   return f"La persona es: {R} <hr>" 

## Ejercicio 3) Programa que crea arreglos con valores aleatorios
## Importamos la libreria sino tenemos que instalarla
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas == 0:
        arreglo= np.random.randint(valores, size=columnas)
    else:
        arreglo = np.random.randint(valores, size=(filas,columnas))
    return f" El arreglo aleatorio es: {arreglo} <hr>"

if __name__ == "__main__":
    app.run(debug=True)