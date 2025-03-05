CSV Processing with Django & Celery

Project Overview

This Django-based web application allows users to upload CSV files, process them asynchronously using Celery, and display computed metrics dynamically on the frontend. The system supports:

CSV file upload

Asynchronous processing with Celery

Calculation of sum, average, and count for numeric columns

Dynamic search functionality for filtering products

Setup Instructions

1. Clone the Repository

git clone <repository_url>
cd csv_project

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Database Migrations

python manage.py migrate

5. Run Django Development Server

python manage.py runserver

6. Start Celery Worker

celery -A app.celery worker --loglevel=info

7. Access the Application

Visit http://127.0.0.1:8000/ in your browser.

# Usage Guide

Upload CSV File: Navigate to the upload page and select a CSV file.

Processing in Background: The file is processed asynchronously using Celery.

View Computed Results: Sum, average, and count of numeric columns are displayed.

Search Feature: Filter products dynamically by name.


## Commands Recap

# To Start Everything

python manage.py runserver  # Start Django
celery -A app.celery worker --loglevel=info  # Start Celery Worker

# To Stop Services

pkill -f runserver  # Stop Django
pkill -f celery  # Stop Celery Worker

