# Expense Tracker App

A simple web application built with Flask and Bootstrap to log, categorize, and view daily expenses.

## Features

* Log expenses with amount, category, date, and notes.
* View a complete list of all expenses.
* See a running total of all spending.
* Filter expenses by category.
* Client-side form validation to ensure data integrity.

## Tech Stack

* **Backend**: Python (Flask)
* **Database**: SQLite (with Flask-SQLAlchemy)
* **Frontend**: HTML, Bootstrap 5
* **JavaScript**: jQuery for form validation

## Setup and Run

1. **Clone the repository**
    ```bash
    git clone https://github.com/RaghuRam2005/expenses_tracker.git
    cd expenses_tracker
    ```

2. **Install Python package manager [uv](https://docs.astral.sh/uv/getting-started/installation/)**
    - Follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

3.  **Run the application:**
    ```bash
    python run app.py
    ```
    
The app will be available at `http://127.0.0.1:5000`.
