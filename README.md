# Simple-Post-Comments Service

A simple backend-only service for creating posts and comments using FastAPI, SQLAlchemy, and Alembic.

## Features

- Create posts
- Add comments to posts
- Retrieve posts and their comments

## Requirements

- pip install -r requirements.txt

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/post-comments-service.git
    cd Simple-post-comments-service
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    Generate an Alembic migration:

    ```sh
    alembic revision --autogenerate -m "Initial migration"
    ```

    Apply the migration to create the database tables:

    ```sh
    alembic upgrade head
    ```

## Running the Application

1. **Start the FastAPI server:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation:**

    Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by Swagger UI.
