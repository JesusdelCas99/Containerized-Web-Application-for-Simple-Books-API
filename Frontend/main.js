function sendRequest() {
    // Obtener el tipo de petición del usuario desde la interfaz
    var requestType = document.getElementById("requestType").value;

    // Configurar la URL del servidor Flask
    var serverUrl = "http://127.0.0.1:5000/api/" + requestType;

    // Datos de ejemplo para la solicitud POST
    var data = {'parametro': 'valor'};

    // Realizar la solicitud al servidor Flask
    fetch(serverUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        // Mostrar el resultado al usuario
        document.getElementById("result").innerText = JSON.stringify(result);
    })
    .catch(error => {
        // Manejar errores
        console.error('Error:', error);
    });
}