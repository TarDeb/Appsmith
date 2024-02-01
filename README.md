# login
# Flask Login API

This Flask application provides a simple API endpoint for user authentication. It uses Werkzeug's security features for password hashing and verification.

## Features

- Simple user authentication
- Password hashing with Werkzeug
- Basic Flask route setup

## Installation

To get this application running on your local machine, follow these steps:

1. **Clone the Repository**

The API will be available at `http://127.0.0.1:5000/`.

## API Usage

### `/login` Endpoint

- **Method**: POST
- **Body**:
  - `username`: String
  - `password`: String

### Successful Response

- **Code**: 200 OK
- **Content**: `{ "message": "success" }`

### Failed Response

- **Code**: 200 OK
- **Content**: `{ "message": "Invalid credentials" }`

## Notes

- This application is a demonstration and not suitable for production use.
- The user data is hardcoded for demonstration purposes. For production, integrate with a database.

