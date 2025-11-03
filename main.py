"""
Main entry point for the FastAPI application.
Run with: python main.py
"""

import uvicorn


def main():
    """Start the FastAPI server."""
    print("Starting Pydantic Models API server...")
    print("API Documentation available at: http://127.0.0.1:8000/docs")
    print("API Root endpoint: http://127.0.0.1:8000/")
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
