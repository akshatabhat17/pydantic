import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="User Management API")


class User(BaseModel):
    id: int
    name: str
    email: str


class HelloResponse(BaseModel):
    message: str


def load_users():
    """Load users from the JSON file."""
    json_path = os.path.join(os.path.dirname(__file__), "users.json")
    with open(json_path, "r") as f:
        return json.load(f)


@app.get("/hello", response_model=HelloResponse)
async def hello():
    """Simple hello world endpoint."""
    return {"message": "Hello World"}


@app.get("/user/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Fetch user details by user_id from JSON file."""
    users = load_users()
    user_key = str(user_id)
    
    if user_key not in users:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
    return users[user_key]


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
