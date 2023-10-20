Flask CRUD API for MySQL Database
This Flask application provides a simple CRUD (Create, Read, Update, Delete) API for interacting with a MySQL database. It allows you to create tables, manage records, and perform basic operations on specified tables.

Prerequisites
Python 3.x
Flask
Flask-CORS
MySQL Database Server
MySQL Connector/Python
Setup
Clone this repository to your local machine:

git clone https://github.com/username/flask-mysql-crud-api.git

Install the required Python packages:

pip install Flask Flask-CORS mysql-connector-python

Configure the MySQL database connection details in the app.py file:

python
Copy code
default_db_config = {
    "host": "localhost",
    "user": "flask_user",
    "password": "your_password",
    "database": "flask_app_db"
}
Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate

Run the Flask application:

python app.py

The API will be accessible at http://localhost:5000.

API Endpoints
Create Table
Create a new table in the database.

URL: POST /sql

Request Body:

{"name": "table_name", "columns": ["column1_name column1_data_type", "column2_name column2_data_type"]}

Delete Table
Delete the specified table from the database.

URL: DELETE /sql/<string:table_name>
Update Table
Add new columns to the specified table.

URL: PUT /sql/<string:table_name>

Request Body:

{"columns": ["new_column_name new_column_data_type", "another_column_name another_column_data_type"]}

Create Record
Insert a new record into the specified table.

URL: POST /sql/<string:table_name>

Request Body:

{"column1_name": "value1", "column2_name": "value2", ...}

Get Records
Retrieve all records from the specified table.

URL: GET /sql/<string:table_name>
Get Single Record
Retrieve a single record by ID from the specified table.

URL: GET /sql/<string:table_name>/<int:record_id>
Update Record
Update the specified record by ID in the specified table.

URL: PUT /sql/<string:table_name>/<int:record_id>

Request Body:

{"column1_name": "new_value1", "column2_name": "new_value2", ...}

Delete Record
Delete the specified record by ID from the specified table.

URL: DELETE /sql/<string:table_name>/<int:record_id>