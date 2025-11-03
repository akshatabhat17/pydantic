# User Management API

A simple FastAPI application with user management endpoints.

## Features

- `/hello` - Returns a Hello World message
- `/user/{user_id}` - Fetches user details from a JSON file

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the FastAPI server:
```bash
python main.py
```

The server will start on `http://localhost:8000`

Alternatively, you can use uvicorn directly:
```bash
uvicorn main:app --reload
```

## Testing the Endpoints

Once the server is running, you can test the endpoints:

### Hello World Endpoint
```bash
curl http://localhost:8000/hello
```

Expected response:
```json
{
  "message": "Hello World"
}
```

### Get User Details
```bash
curl http://localhost:8000/user/1
```

Expected response:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Error Handling
If you request a non-existent user:
```bash
curl http://localhost:8000/user/999
```

Expected response (404):
```json
{
  "detail": "User with id 999 not found"
}
```

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
