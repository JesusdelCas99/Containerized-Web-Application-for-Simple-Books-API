# REQUISITOS DEL SERVIDOR
# ---------------------------------------------------------------------------------------
# El servidor debe ser capaz de responder tres tipos de peticiones distintas del cliente:
#     Petición A: Responde con la información del tipo 1.
#     Petición B: Responde con información del tipo 2.
#     Petición C: Responde ambos tipos de información 1 y 2.

from flask import Flask, render_template
import requests
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')
    

@socketio.on('check_for_connection_request')
def handle_check_for_connection(data):
    print(f"Received 'check_for_connection' event with data: {data}")
    # Envía una respuesta al cliente
    socketio.emit('check_for_connection_response', 'Server processed your request')


# Ruta para la Petición A: Responder con información de la API 1
@app.route('/peticion_a')
def peticion_a():
    pass


if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo debug



