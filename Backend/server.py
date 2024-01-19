from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')
    

@socketio.on('check_status_request')
def handle_check_for_connection(data):
    print(f"Received 'check_for_connection' event with data: {data}")
    # Envía una respuesta al cliente
    socketio.emit('check_status_response', 'Server processed your request')


# Ruta para la Petición A: Responder con información de la API 1
@app.route('/peticion_a')
def peticion_a():
    pass


if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo debug



