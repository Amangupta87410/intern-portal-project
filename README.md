# Intern Portal Project

This is a full-stack intern portal application built with Django for the backend and HTML/CSS/JavaScript for the frontend.

## Features

-   Dummy Login Page
-   Intern Dashboard showing name, referral code, and total donations.
-   Data is fetched from a live Django API.
-   Static Rewards Section.
-   Bonus: Leaderboard page to show rankings of all interns.

## How to Run This Project

### Prerequisites

-   Python
-   Pip
-   Django

### 1. Backend Setup (Django)

First, set up and run the backend server.

1.  **Clone the repository and navigate into the `intern_portal` directory.**
2.  **Install dependencies:**
    ```bash
    pip install django djangorestframework django-cors-headers
    ```
3.  **Apply migrations to create the database tables:**
    ```bash
    python manage.py migrate
    ```
4.  **Run the server:**
    ```bash
    python manage.py runserver
    ```
    The backend API will now be running at `http://127.0.0.1:8000/api/`.

### 2. Frontend Setup (HTML)

1.  Make sure the backend server is running.
2.  Open the `intern_portal.html` file in your web browser (like Chrome or Firefox).
3.  The portal should now be fully functional.
