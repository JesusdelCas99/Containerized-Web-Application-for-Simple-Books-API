// Client-Server connections
// ---------------------------------------------------------
// Establish WebSocket connection to 'Flask' server on 127.0.0.1:5000
const socket = io.connect('http://127.0.0.1:5000');


// Client Events
// ---------------------------------------------------------
// Client 'onclick' WebSocket event 'check_status_request'
function WebSocketsSendRequest() {
    const mensaje = document.getElementById('requestType').value;
    socket.emit('check_status_request', mensaje);
}


// Server Events
// ---------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
    // Server WebSockets event 'check_status_response'
    handleServerStatusEvent();
});


// Server WebSockets event 'check_status_response'
function handleServerStatusEvent() {
    const timestamp = new Date().toLocaleTimeString();
    socket.on('check_status_response', (data) => {
        document.getElementById('result').innerHTML += `${timestamp} - (simple-books-api) Status: ${data}<br>`;
    });
}