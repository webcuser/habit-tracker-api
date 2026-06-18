# Habit Tracker API

This is a simple API for tracking daily habits to help you improve your personal growth. You can create, read, update, and delete habits, as well as mark them as completed for each day. This project is built using Python with FastAPI for the backend and Vue.js for the frontend.

## Features
- Create, Read, Update, Delete habits
- Mark habits as completed on a daily basis
- Simple user authentication

## Setup
### Backend (Python)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/habit-tracker-api.git
   cd habit-tracker-api/backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend (Vue.js)
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the Vue.js development server:
   ```bash
   npm run dev
   ```

## How it Works
1. The backend is built using FastAPI, providing a RESTful API to manage habits.
2. The frontend is a Vue.js application that communicates with the API to display and manage habits.
3. You can interact with the API using POST, GET, PUT, and DELETE requests from the Vue.js application.

## Learn More
For documentation on FastAPI, visit [FastAPI Docs](https://fastapi.tiangolo.com/).
For more advanced Vue.js concepts, check out [Vue.js Docs](https://vuejs.org/v2/guide/).