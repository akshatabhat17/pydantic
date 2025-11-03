# Pydantic Models FastAPI Application

A FastAPI application that exposes CRUD operations for all Pydantic models from the `pydantic.ipynb` notebook.

**Note:** This is a demonstration application using in-memory storage. For production use, consider implementing:
- Persistent database storage (PostgreSQL, MongoDB, etc.)
- Thread-safe data structures or proper locking mechanisms
- Authentication and authorization
- Rate limiting and input sanitization

## Features

This API provides full CRUD (Create, Read, Update, Delete) operations for the following models:

1. **PersonModel** - Basic person information (name, age, city)
2. **EmployeeModel** - Employee data with optional salary and active status
3. **ClassroomModel** - Classroom with list of students and capacity
4. **CustomerModel** - Customer with nested address information
5. **ItemModel** - Items with field constraints (name, price, description)

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
python main.py
```

The server will start on `http://0.0.0.0:8000`

## API Documentation

Once the server is running, access the interactive API documentation at:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Root
- `GET /` - API information and available endpoints

### PersonModel
- `POST /persons` - Create a new person
- `GET /persons` - Get all persons
- `GET /persons/{person_id}` - Get a specific person
- `PUT /persons/{person_id}` - Update a person
- `DELETE /persons/{person_id}` - Delete a person

### EmployeeModel
- `POST /employees` - Create a new employee
- `GET /employees` - Get all employees
- `GET /employees/{employee_id}` - Get a specific employee
- `PUT /employees/{employee_id}` - Update an employee
- `DELETE /employees/{employee_id}` - Delete an employee

### ClassroomModel
- `POST /classrooms` - Create a new classroom
- `GET /classrooms` - Get all classrooms
- `GET /classrooms/{classroom_id}` - Get a specific classroom
- `PUT /classrooms/{classroom_id}` - Update a classroom
- `DELETE /classrooms/{classroom_id}` - Delete a classroom

### CustomerModel
- `POST /customers` - Create a new customer
- `GET /customers` - Get all customers
- `GET /customers/{customer_id}` - Get a specific customer
- `PUT /customers/{customer_id}` - Update a customer
- `DELETE /customers/{customer_id}` - Delete a customer

### ItemModel
- `POST /items` - Create a new item
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a specific item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item

## Example Usage

### Create a Person
```bash
curl -X POST http://127.0.0.1:8000/persons \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","age":30,"city":"New York"}'
```

### Create an Employee
```bash
curl -X POST http://127.0.0.1:8000/employees \
  -H "Content-Type: application/json" \
  -d '{"id":1,"name":"John Doe","department":"Engineering","salary":75000.0}'
```

### Create a Classroom
```bash
curl -X POST http://127.0.0.1:8000/classrooms \
  -H "Content-Type: application/json" \
  -d '{"class_name":"Math 101","students":["Alice","Bob","Charlie"],"capacity":30}'
```

### Create a Customer with Nested Address
```bash
curl -X POST http://127.0.0.1:8000/customers \
  -H "Content-Type: application/json" \
  -d '{"id":1,"name":"Emily Davis","address":{"street":"123 Main St","city":"Springfield","zip_code":"12345"}}'
```

### Create an Item with Validation
```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Laptop","price":999.99,"description":"A high-end gaming laptop"}'
```

## Data Validation

All models include Pydantic validation:
- **PersonModel**: Validates name (str), age (int), city (str)
- **EmployeeModel**: Validates id (int), optional salary (float), optional is_active (bool)
- **ClassroomModel**: Validates students as a list of strings, optional capacity (int)
- **CustomerModel**: Validates nested AddressModel structure
- **ItemModel**: Enforces field constraints (name max 50 chars, price > 0, description max 300 chars)

## Project Structure

```
.
├── main.py           # Entry point to start the FastAPI server
├── api.py            # FastAPI application with all CRUD endpoints
├── models.py         # Pydantic model definitions
├── requirements.txt  # Python dependencies
└── pydantic.ipynb   # Original notebook with model examples
```

## Technologies Used

- **Python 3.12+**
- **FastAPI** - Modern web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server for running FastAPI
