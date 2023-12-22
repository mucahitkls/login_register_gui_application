# Login System with Tkinter and SQLAlchemy

## Project Overview
This project is a simple login system built with Python's Tkinter library for the GUI and SQLAlchemy for database interaction. It allows users to register and log in with a username and password. The password is securely hashed using bcrypt before being stored in a PostgreSQL database.

## Features
- User registration with hashed passwords
- User login with password verification
- GUI built with Tkinter
- Database interactions handled with SQLAlchemy

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6+
- PostgreSQL server running and accessible
- Required Python packages: `Tkinter`, `SQLAlchemy`, `bcrypt`, `psycopg2` (or `psycopg2-binary`)

## Installation and Setup
1. Clone the repository:
git clone [Your Repository URL Here]

2. Navigate to the project directory:
cd login_gui_with_tkinter


3. Install the required packages:
pip install -r requirements.txt


4. Configure your database connection:
- Update the `app.config` file with your PostgreSQL database URL.

## Usage
To run the application, execute the following command in your terminal:
python main.py

## Contributing
Contributions to this project are welcome! Here's how you can help:
- Report a bug
- Submit a feature request
- Propose improvements to the code or documentation


## Contact
For any questions or comments, please contact Mucahit Keles at kelessmucahit@gmail.com.

## Acknowledgements
bcrypt documentation: https://pypi.org/project/bcrypt/
sqlalchemy documentation: https://docs.sqlalchemy.org/en/20/
postgresql documentation: https://www.postgresql.org/docs/current/
