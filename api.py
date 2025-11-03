"""
FastAPI application with CRUD endpoints for all Pydantic models.
Provides RESTful API for PersonModel, EmployeeModel, ClassroomModel, CustomerModel, and ItemModel.
"""

from fastapi import FastAPI, HTTPException
from typing import Dict, List
from models import (
    PersonModel,
    EmployeeModel,
    ClassroomModel,
    CustomerModel,
    ItemModel,
)

app = FastAPI(
    title="Pydantic Models API",
    description="FastAPI application exposing CRUD operations for all Pydantic models from the notebook",
    version="1.0.0",
)

# In-memory storage for each model type
persons: Dict[int, PersonModel] = {}
employees: Dict[int, EmployeeModel] = {}
classrooms: Dict[int, ClassroomModel] = {}
customers: Dict[int, CustomerModel] = {}
items: Dict[int, ItemModel] = {}

# Counter for generating IDs
person_id_counter = 1
classroom_id_counter = 1
item_id_counter = 1


@app.get("/")
def root():
    """Root endpoint providing API information."""
    return {
        "message": "Welcome to Pydantic Models API",
        "endpoints": {
            "persons": "/persons",
            "employees": "/employees",
            "classrooms": "/classrooms",
            "customers": "/customers",
            "items": "/items",
        },
        "docs": "/docs",
    }


# ==================== PersonModel CRUD ====================

@app.post("/persons", response_model=PersonModel, status_code=201)
def create_person(person: PersonModel):
    """Create a new person."""
    global person_id_counter
    persons[person_id_counter] = person
    person_id_counter += 1
    return person


@app.get("/persons", response_model=List[PersonModel])
def get_all_persons():
    """Get all persons."""
    return list(persons.values())


@app.get("/persons/{person_id}", response_model=PersonModel)
def get_person(person_id: int):
    """Get a specific person by ID."""
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons[person_id]


@app.put("/persons/{person_id}", response_model=PersonModel)
def update_person(person_id: int, person: PersonModel):
    """Update a person by ID."""
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    persons[person_id] = person
    return person


@app.delete("/persons/{person_id}")
def delete_person(person_id: int):
    """Delete a person by ID."""
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    del persons[person_id]
    return {"message": "Person deleted successfully"}


# ==================== EmployeeModel CRUD ====================

@app.post("/employees", response_model=EmployeeModel, status_code=201)
def create_employee(employee: EmployeeModel):
    """Create a new employee."""
    if employee.id in employees:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    employees[employee.id] = employee
    return employee


@app.get("/employees", response_model=List[EmployeeModel])
def get_all_employees():
    """Get all employees."""
    return list(employees.values())


@app.get("/employees/{employee_id}", response_model=EmployeeModel)
def get_employee(employee_id: int):
    """Get a specific employee by ID."""
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees[employee_id]


@app.put("/employees/{employee_id}", response_model=EmployeeModel)
def update_employee(employee_id: int, employee: EmployeeModel):
    """Update an employee by ID."""
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees[employee_id] = employee
    return employee


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    """Delete an employee by ID."""
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    del employees[employee_id]
    return {"message": "Employee deleted successfully"}


# ==================== ClassroomModel CRUD ====================

@app.post("/classrooms", response_model=ClassroomModel, status_code=201)
def create_classroom(classroom: ClassroomModel):
    """Create a new classroom."""
    global classroom_id_counter
    classrooms[classroom_id_counter] = classroom
    classroom_id_counter += 1
    return classroom


@app.get("/classrooms", response_model=List[ClassroomModel])
def get_all_classrooms():
    """Get all classrooms."""
    return list(classrooms.values())


@app.get("/classrooms/{classroom_id}", response_model=ClassroomModel)
def get_classroom(classroom_id: int):
    """Get a specific classroom by ID."""
    if classroom_id not in classrooms:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classrooms[classroom_id]


@app.put("/classrooms/{classroom_id}", response_model=ClassroomModel)
def update_classroom(classroom_id: int, classroom: ClassroomModel):
    """Update a classroom by ID."""
    if classroom_id not in classrooms:
        raise HTTPException(status_code=404, detail="Classroom not found")
    classrooms[classroom_id] = classroom
    return classroom


@app.delete("/classrooms/{classroom_id}")
def delete_classroom(classroom_id: int):
    """Delete a classroom by ID."""
    if classroom_id not in classrooms:
        raise HTTPException(status_code=404, detail="Classroom not found")
    del classrooms[classroom_id]
    return {"message": "Classroom deleted successfully"}


# ==================== CustomerModel CRUD ====================

@app.post("/customers", response_model=CustomerModel, status_code=201)
def create_customer(customer: CustomerModel):
    """Create a new customer."""
    if customer.id in customers:
        raise HTTPException(status_code=400, detail="Customer ID already exists")
    customers[customer.id] = customer
    return customer


@app.get("/customers", response_model=List[CustomerModel])
def get_all_customers():
    """Get all customers."""
    return list(customers.values())


@app.get("/customers/{customer_id}", response_model=CustomerModel)
def get_customer(customer_id: int):
    """Get a specific customer by ID."""
    if customer_id not in customers:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customers[customer_id]


@app.put("/customers/{customer_id}", response_model=CustomerModel)
def update_customer(customer_id: int, customer: CustomerModel):
    """Update a customer by ID."""
    if customer_id not in customers:
        raise HTTPException(status_code=404, detail="Customer not found")
    customers[customer_id] = customer
    return customer


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    """Delete a customer by ID."""
    if customer_id not in customers:
        raise HTTPException(status_code=404, detail="Customer not found")
    del customers[customer_id]
    return {"message": "Customer deleted successfully"}


# ==================== ItemModel CRUD ====================

@app.post("/items", response_model=ItemModel, status_code=201)
def create_item(item: ItemModel):
    """Create a new item."""
    global item_id_counter
    items[item_id_counter] = item
    item_id_counter += 1
    return item


@app.get("/items", response_model=List[ItemModel])
def get_all_items():
    """Get all items."""
    return list(items.values())


@app.get("/items/{item_id}", response_model=ItemModel)
def get_item(item_id: int):
    """Get a specific item by ID."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}", response_model=ItemModel)
def update_item(item_id: int, item: ItemModel):
    """Update an item by ID."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by ID."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}
