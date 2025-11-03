"""
Pydantic models for the FastAPI application.
All models are extracted from the pydantic.ipynb notebook.
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class PersonModel(BaseModel):
    """Basic person model with name, age, and city."""
    name: str
    age: int
    city: str


class EmployeeModel(BaseModel):
    """Employee model with optional salary and active status fields."""
    id: int
    name: str
    department: str
    salary: Optional[float] = None
    is_active: Optional[bool] = True


class ClassroomModel(BaseModel):
    """Classroom model with list of students and optional capacity."""
    class_name: str
    students: List[str]
    capacity: Optional[int] = None


class AddressModel(BaseModel):
    """Address model for nested use in CustomerModel."""
    street: str
    city: str
    zip_code: str


class CustomerModel(BaseModel):
    """Customer model with nested address."""
    id: int
    name: str
    address: AddressModel


class ItemModel(BaseModel):
    """Item model with field constraints."""
    name: str = Field(..., title="Item Name", max_length=50)
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    description: Optional[str] = Field(None, max_length=300)
