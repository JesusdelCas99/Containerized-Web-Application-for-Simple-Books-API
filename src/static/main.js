// CONEXIONES CLIENTE-SERVIDOR
// ---------------------------------------------------------
// Conexión WebSockets al servidor 'Flask' (127.0.0.1:5000)
const socket = io.connect('http://127.0.0.1:5000');


// EVENTOS DEL CLIENTE
// ---------------------------------------------------------
// Evento 'onclick' del cliente 'check_status_request' (conexión WebSockets al servidor 'Flask')
function WebSocketsSendRequest() {
    const mensaje = document.getElementById('requestType').value;
    socket.emit('check_status_request', mensaje);
}


// EVENTOS DEL SERVIDOR
// ---------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
    // Eventos del servidor 'Flask'
    handleServerFlaskEvents();
});


// Eventos del servidor 'Flask'
function handleServerFlaskEvents(){
    // Lista de eventos del servidor 'Flask'
    handleServerStatusEvent()
}

// (Servidor 'Flask') Evento del servidor 'check_status_response' (conexión WebSockets)
function handleServerStatusEvent() {
    const timestamp = new Date().toLocaleTimeString();
    socket.on('check_status_response', (data) => {
    document.getElementById('result').innerHTML += `${timestamp} - (simple-books-api) Status: ${data}<br>`;
    });
}