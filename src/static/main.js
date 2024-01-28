/* Client "main.js" JavaScript file */

/* (Client-Server connections) Establish WebSocket connection to the server */
const socket = io.connect('http://127.0.0.1:5000');

/* (Client event) Client 'onclick' event "Clear response"*/
function ClientClearResponse() {
    document.getElementById('result').innerHTML = '';
}


/* (Client event) Client 'onclick' WebSocket event 'check_status_request' */
function WebSocketsStatusRequest() {
    socket.emit('check_status_request', "dummy text");
}

/* (Client event) Client 'onclick' WebSocket event 'bookList_request' */
function WebSocketsbookListRequest() {
    var typeValue = document.getElementById("typeInput").value;
    var limitValue = document.getElementById("limitInput").value;

    // Check for input typeValue content
    if (typeValue !== "") {
        if (typeValue.toLowerCase() !== "fiction" && typeValue.toLowerCase() !== "non-fiction"){
            alert("Please enter a correct value for Type.");
            return;
        }
    }

    // Check if the limit value is a valid integer
    if (limitValue !== "") {
        if (!(/^\d+$/.test(limitValue))) {
            alert("Please enter a correct value for Type.");
            return;
        }
        else if (parseInt(limitValue) < 1 || parseInt(limitValue) > 20 ){
            alert("Please enter an integer value for Limit.");
            return;
        }
    }

    socket.emit('bookList_request', typeValue, limitValue);
}


/* Server Events */
document.addEventListener('DOMContentLoaded', function () {
    /* (Server event) Server WebSockets event 'check_status_response' */
    handleServerStatusEvent();
    handleServerBookListEvent();
});


/* Server WebSockets event 'check_status_response' */
function handleServerStatusEvent() {
    socket.on('check_status_response', (data) => {
        let now = new Date();
        let year = now.getFullYear();
        let month = now.getMonth() + 1;
        let day = now.getDate();
        let hour = now.getHours();
        let minute = now.getMinutes();
        let second = now.getSeconds();

        document.getElementById('result').innerHTML = `(${day}/${month}/${year}) - ${hour*3600 + 60*minute + second}'' - (simple-books-api) Status: ${data}<br>`;
    });
}

function handleServerBookListEvent() {
    socket.on('bookList_response', (data) => {
        // Parse the JSON data
        var books = data

        // Initialize an empty string to store the HTML markup
        var html = '';

        // Iterate over each book object
        books.forEach(function(book) {
            // Generate HTML markup for each book
            html += '<div>';
            html += '<hr>'
            html += '<p><strong>ID:</strong> ' + book.id + '</p>';
            html += '<p><strong>Name:</strong> ' + book.name + '</p>';
            html += '<p><strong>Type:</strong> ' + book.type + '</p>';
            html += '<p><strong>Available:</strong> ' + (book.available ? 'Yes' : 'No') + '</p>';
            html += '</div>';
        });

        // Set the HTML content of the 'result' element to display the generated HTML
        document.getElementById('result').innerHTML = html;
    });
}

// JavaScript function to redirect to a specific page
function redirectToPage(url) {
    window.location.href = url;
}