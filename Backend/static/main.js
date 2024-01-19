function WebSocketsSendRequest() {
        const mensaje = document.getElementById('requestType').value;
        socket.emit('check_for_connection_request', mensaje);
}

// Gestión de eventos del servidor
function handleServerEvents() {
    const timestamp = new Date().toLocaleTimeString();
    socket.on('check_for_connection_response', (data) => {
    document.getElementById('result').innerHTML += `${timestamp} - ${data}<br>`;
    });
}

// Establish the WebSocket connection
const socket = io.connect('http://127.0.0.1:5000');

// Llama a la función handleServerEvents al final del DOM cargado
document.addEventListener('DOMContentLoaded', function () {
    handleServerEvents();
});