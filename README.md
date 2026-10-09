
# Hackathon Practice App

## Overview
A simple task management application built to practise Python, Streamlit, and SQLite before a software development hackathon.

## Features
- Add tasks through a simple user interface.
- Store tasks in an SQLite database.
- Display saved tasks in a table.
- Preserve tasks after restarting the application.
- Validate empty task submissions.

## Tech Stack
- Python
- Streamlit
- SQLite
- Git and GitHub

## Project Structure
- `app.py` — Main Streamlit application.
- `check_db.py` — Script to verify saved database records.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Files excluded from Git.

## Setup Instructions

1. Install Python 3.
2. Create and activate a virtual environment.
3. Install dependencies:

   `python -m pip install -r requirements.txt`

4. Run the application:

   `python -m streamlit run app.py`

## Database
The application creates `practice.db` locally when it runs. The database file is excluded from Git.

## Testing
- Added multiple tasks.
- Verified tasks appear in the application.
- Restarted the application and confirmed saved tasks remained available.
