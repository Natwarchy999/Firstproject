# FastAPI Practice Project

This project is a simple full-stack practice application with a FastAPI backend and a Vite React frontend. It includes user authentication, protected routes, account management, and file upload support.

## Features
- User registration and login
- JWT-based authentication
- Protected profile access
- Account deletion
- File upload endpoint
- React frontend under the client folder

## Project Structure
- app/main.py - FastAPI application entry point
- app/routes/auth.py - API routes for auth and user actions
- app/services/auth_service.py - Business logic for registration, login, profile, and uploads
- app/core/ - Configuration, database setup, and security helpers
- app/models/ - Database models
- app/schemas/ - Request and response schemas
- client/vite-project/ - Vite + React frontend

## Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic Settings
- JWT authentication with python-jose
- Passlib for password hashing
- Vite + React

## Setup Instructions
1. Activate the virtual environment:
   - Windows: `myenv\Scripts\activate`
2. Install the required Python packages if needed.
3. Create a `.env` file in the project root and define your database connection:
   - `DB_CONNECTION=your_database_url`
4. Start the backend:
   - `uvicorn app.main:app --reload`
5. Start the frontend:
   - `cd client/vite-project`
   - `npm install`
   - `npm run dev`

## API Endpoints
- GET `/` - Health check
- POST `/register` - Create a new user account
- POST `/login` - Log in and receive an access token
- POST `/logout` - Logout endpoint
- GET `/profile` - Access protected profile information
- DELETE `/delete_account` - Delete the authenticated user account
- POST `/upload_file` - Upload a file

## Notes
- Protected routes require a Bearer token received from the login endpoint.
- Uploaded files are saved in the uploads folder for this project.
- The backend is designed as a learning/demo project and can be extended with database models, validation, and frontend integration.
