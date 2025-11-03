import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="User Management API")

# Cache for user data - loaded once at startup
_users_cache = None


class User(BaseModel):
    id: int
    name: str
    email: str


class HelloResponse(BaseModel):
    message: str


def load_users():
    """Load users from the JSON file with error handling and caching."""
    global _users_cache
    
    if _users_cache is not None:
        return _users_cache
    
    json_path = os.path.join(os.path.dirname(__file__), "users.json")
    
    try:
        with open(json_path, "r") as f:
            _users_cache = json.load(f)
            return _users_cache
    except FileNotFoundError:
        raise HTTPException(
            status_code=500, 
            detail="User data file not found. Please contact the administrator."
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail="User data file is corrupted. Please contact the administrator."
        )


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
