# RSS Reader Backend

This repository contains the backend for an RSS Reader application, providing APIs to manage users, feeds, and blog entries.

## Project Description

The backend is built using FastAPI and interacts with a PostgreSQL database to store user information, RSS feed subscriptions, and parsed blog entries. It handles fetching, parsing, and sanitizing RSS feed content.

## Technology Stack

*   **Framework:** FastAPI
*   **Database:** PostgreSQL
*   **ORM:** SQLAlchemy
*   **Dependencies:**
    *   `fastapi`
    *   `uvicorn[standard]`
    *   `psycopg2-binary`
    *   `SQLAlchemy`
    *   `python-dotenv`
    *   `firebase-admin` (for authentication)
    *   `feedparser` (for parsing RSS/Atom feeds)
    *   `bleach` (for sanitizing HTML content)
*   **Containerization:** Docker

## Setup Instructions

1.  **Clone the repository:**
```
bash
    git clone https://github.com/your-username/rss-reader-backend.git
    cd rss-reader-backend
    
```
2.  **Create and activate a virtual environment:**
```
bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    
```
3.  **Install dependencies:**
```
bash
    pip install -r requirements.txt
    
```
4.  **Copy `.env.example` to `.env` and fill in details:**
```
bash
    cp .env.example .env
    
```
Edit the `.env` file and update the placeholder values with your actual database credentials, Firebase service account key path, and a strong secret key.
```
dotenv
    DATABASE_URL=postgresql://user:password@host:port/database_name
    FIREBASE_SERVICE_ACCOUNT_KEY_PATH=/path/to/your/firebase-service-account.json
    APP_SECRET_KEY=your_very_secret_key
    
```
5.  **Database Setup:**

    Ensure you have a PostgreSQL database running. Update the `DATABASE_URL` in your `.env` file to point to your database instance. You will need to run database migrations (not yet implemented in the basic setup) to create the necessary tables based on the models defined in `models.py`.

## Running the Application

To start the FastAPI development server using uvicorn:
```
bash
uvicorn main:app --reload
```
The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints Overview

API endpoints are defined in the `routes/` directory. You will find modules for different functionalities like user management, feed subscriptions, and retrieving blog entries. Refer to the files within `routes/` for specific endpoint details and request/response schemas (defined in `schemas/`).

## Docker Instructions

To build the Docker image:
```
bash
docker build -t rss-reader-backend .
```
To run the Docker container:
```
bash
docker run -p 8000:8000 --env-file .env rss-reader-backend
```
This will run the application in a container, mapping port 8000 on your host to port 8000 in the container. The `--env-file .env` flag passes your environment variables from the `.env` file into the container.