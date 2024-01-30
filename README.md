[![test_server](https://github.com/JesusdelCas99/Flask-Web-Client-Server-Application/actions/workflows/test_server.yml/badge.svg)](https://github.com/JesusdelCas99/Flask-Web-Client-Server-Application/actions/workflows/test_server.yml)
## Simple Books API Web Client

This project is a web application built with Flask, providing a simple interface to interact with a book database. It allows users to view a list of books, get detailed information about a specific book, and check the status of an external API serving the book data.

The application is designed to interact with the **Simple Books API** hosted at [simple-books-api.glitch.me](https://simple-books-api.glitch.me). This API provides endpoints for retrieving information about books, including their titles, authors, ISBNs, types, prices, and availability status.

For detailed documentation on the API endpoints and how to use them, please refer to the [API documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md).

### How to run the Server

1. **Install Dependencies**

   You can install the required dependencies using either `requirements.txt` or `environment.yml`. Choose one of the following methods:

   - Using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

   - Using `environment.yml`:
     ```
     conda env create -f environment.yml
     conda activate dapt
     ```

    
2. **Launch the Server**

   Run the Flask server by executing the following command:

        python server.py
    
3. **Access the Web Application**

    Once the server is running, you can access the web application by navigating to http://127.0.0.1:5000 in your web browser.

### Unit Testing

The project includes unit tests for the server functionality. These tests ensure that the server routes return the expected responses and handle various scenarios correctly. You can find the unit tests in the `tests/unittest/` directory. To run the unit tests, execute the following command:

   ```
   python test/unittest/test_server.py
   ```

### Additional Information

- **Server Architecture**:
        The server is built using Flask, a lightweight web framework for Python.
        It utilizes Socket.IO for real-time communication between the client and server.

- **External API Integration**:
        The server interacts with an external API (https://simple-books-api.glitch.me) to fetch book data.
        It handles requests to endpoints such as /status, /bookList, and /bookInfo.

- **Client-Side Interaction**:
        The client-side functionality is implemented using JavaScript.
        It establishes WebSocket connections with the server to fetch data asynchronously.

- **Folder Structure**:
        - `src/`: Contains the server code (`server.py`) and static files (e.g., JavaScript).
        - `tests/unittest/`: Contains unit tests for the server.

Feel free to explore the codebase and contribute to further enhancements or bug fixes!
