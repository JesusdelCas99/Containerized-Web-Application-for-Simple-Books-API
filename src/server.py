from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
import json


app = Flask(__name__)
socketio = SocketIO(app)


'''
Default route ('/'): 
This route directs users to 'index.html' page                        
'''
@app.route('/')
def index():
    return render_template('index.html')
    

"""
Server-side event handler for a Socket.IO connection:
* Server listens for 'check_status_request' WebSocket event
* Server emits 'check_status_response' WebSocket event               
"""
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


# Run application in debug mode
if __name__ == '__main__':
    app.run(debug=True) 



