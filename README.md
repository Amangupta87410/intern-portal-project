Intern Portal Project
This is a full-stack intern portal application built with Django for the backend and HTML/CSS/JavaScript for the frontend, as per the provided task requirements.

Features
Dummy Login Page: A simple, non-functional login interface.

Intern Dashboard: Displays key information for the logged-in intern:

Intern's Name

A unique Referral Code

Total Donations Raised

Live Data Fetching: All dashboard data is fetched dynamically from the Django backend API.

Static Rewards Section: Shows a list of unlockable rewards based on performance.

Bonus: Leaderboard Page: A separate page that ranks all interns based on their total donations, highlighting the current user's position.

How to Run This Project Locally
Follow these steps to set up and run the project on your local machine.

Prerequisites
Python 3.x

pip (Python package installer)

1. Backend Setup (Django)
First, set up and run the backend server.

Clone the repository:

git clone https://amangupta87410.github.io/intern-portal-project/
cd your-repo-name

Navigate to the backend directory:

cd intern_portal

Install dependencies:

pip install -r requirements.txt

Apply migrations to create the database tables:

python manage.py migrate

Run the server:

python manage.py runserver

The backend API will now be running at http://127.0.0.1:8000/api/. Keep this terminal window open.

2. Frontend Setup (HTML)
Make sure the backend server from the previous step is still running.

Navigate to the root directory of the project in your file explorer.

Open the index.html file in your web browser (like Chrome, Firefox, etc.).

The portal should now be fully functional on your local machine.
