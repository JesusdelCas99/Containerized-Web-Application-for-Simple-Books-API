from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
import json

app = Flask(__name__)
socketio = SocketIO(app)


# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')
    

@socketio.on('check_status_request')
def handle_check_for_connection(data):
    # Verify connection
    print(f"Received 'check_for_connection' event with data: {data}")

    # Specify headers for the request
    headers = {'Content-Type': 'application/json'}

    # Make a GET request to the external API
    api_url = 'https://simple-books-api.glitch.me/status'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Submmit JSON response
        socketio.emit('check_status_response', json.loads(response.content)['status'])
    else:
        # If the request was unsuccessful, return an error message to the client
        socketio.emit('check_status_response', "'error': 'Failed to fetch data from the API'")


if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo debug



