# REQUISITOS DEL SERVIDOR
# ---------------------------------------------------------------------------------------
# El servidor debe ser capaz de responder tres tipos de peticiones distintas del cliente:
#     Petición A: Responde con la información del tipo 1.
#     Petición B: Responde con información del tipo 2.
#     Petición C: Responde ambos tipos de información 1 y 2.

from flask import Flask, render_template
import requests
# import requests_cache

app = Flask(__name__)


# Cache para las solicitudes HTTP con duración de 300 segundos (5 minutos)
# requests_cache.install_cache('api_cache', expire_after=300)


# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Función para obtener datos de la API 1
def obtener_datos_api1():
    # Encabezados para la solicitud
    headers = {"Accept": "application/json"}
    # Realizar la solicitud GET con los encabezados
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    # Imprimir la respuesta
    return response.json()


# Función para obtener datos de la API 2
def obtener_datos_api2():
    # Aquí se realiza la solicitud a la API 2
    response = requests.get('https://randomuser.me/api/')
    # Imprimir la respuesta
    return response.json()


# Ruta para la Petición A: Responder con información de la API 1
@app.route('/peticion_a')
def peticion_a():
    data_api1 = obtener_datos_api1()
    return f'<p>Broma: {data_api1["joke"]}</p>'


# Ruta para la Petición B: Responder con información de la API 2
@app.route('/peticion_b')
def peticion_b():
    data_api2 = obtener_datos_api2()
    first = data_api2["results"][0]["name"]["first"]
    last = data_api2["results"][0]["name"]["last"]
    return f'<p>Name: {first}, Last: {last}</p>'


# Ruta para la Petición C: Responder con información de ambas APIs
@app.route('/peticion_c')
def peticion_c():
    data_api1 = obtener_datos_api1()
    joke = data_api1["joke"]

    data_api2 = obtener_datos_api2()
    first = data_api2["results"][0]["name"]["first"]
    last = data_api2["results"][0]["name"]["last"]

    return f'<p>{joke}, ({first},{last})</p>'


if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo debug



