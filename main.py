from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Default Database Configuration
default_db_config = {
    "host": "localhost",
    "user": "flask_user",
    "password": "your_password",
    "database": "flask_app_db"
}

# Function to establish database connection based on request parameters
def get_db_config():
    # Get the database parameter from the request URL, default to None if not provided
    database = request.args.get('db', None)
    
    # If database parameter is provided, use it in the connection configuration
    if database:
        db_config = default_db_config.copy()  # Create a copy of the default configuration
        db_config["database"] = database  # Update the database name
        return db_config
    else:
        return default_db_config  # Use the default configuration if database parameter is not provided

@app.route('/hello', methods=['GET'])
def say_hello():
    return "Hello, world!"

@app.route('/sql', methods=['POST'])
def create_table():
    try:
        # Parse JSON data from the request
        table_data = request.get_json()
        
        # Extract column details from JSON data
        table_name = table_data.get('name')
        columns = table_data.get('columns')

        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example Query: Create a new table based on provided columns
        # Note: This is a basic example and might need additional validation and error handling
        query = f"CREATE TABLE {table_name} ({', '.join(columns)});"
        cursor.execute(query)

        # Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": f"Table '{table_name}' created successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/sql/<string:table_name>', methods=['DELETE'])
def delete_table(table_name):
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example Query: Drop the specified table
        query = f"DROP TABLE {table_name};"
        cursor.execute(query)

        # Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": f"Table '{table_name}' deleted successfully."})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/sql/<string:table_name>', methods=['PUT'])
def update_table(table_name):
    try:
        # Parse JSON data from the request
        table_data = request.get_json()

        # Extract column details from JSON data
        columns = table_data.get('columns')

        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example Query: Add new columns to the specified table
        for column in columns:
            query = f"ALTER TABLE {table_name} ADD {column};"
            cursor.execute(query)

        # Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": f"Columns added to '{table_name}' successfully."})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/sql/<string:table_name>', methods=['POST'])
def create_record(table_name):
    try:
        # Parse JSON data from the request
        record_data = request.get_json()

        # Check if the incoming data is a list or a dictionary
        if isinstance(record_data, dict):
            record_data = [record_data]
        
        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        
        # Handle a list of records
        for record in record_data:
            columns = ', '.join(record.keys())
            placeholders = ', '.join('%s' for _ in record.values())
            values = tuple(record.values())


            # Example Query: Insert a new record into the specified table using parameterized query
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
            cursor.execute(query, values)  # Pass the values as a parameter to execute

        # Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
        
        return jsonify({"message": f"Record(s) created successfully in '{table_name}'."}), 201

    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/sql/<string:table_name>', methods=['GET'])
def get_records(table_name):
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example Query: Select all records from the specified table
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)

        # Get column names from the description attribute
        column_names = [column[0] for column in cursor.description]

        # Fetch all rows from the result set
        records = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Convert the result to a list of dictionaries for JSON response
        record_list = []
        for record in records:
            record_dict = dict(zip(column_names, record))  # Assuming the first column is an ID
            record_list.append(record_dict)

        return jsonify(record_list)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/sql/<string:table_name>/<int:record_id>', methods=['PUT'])
def update_record(table_name, record_id):
    try:
        # Parse JSON data from the request
        record_data = request.get_json()

        # Construct update values from JSON data using placeholders
        update_values = ', '.join(f"{key} = %s" for key in record_data.keys())
        values = tuple(record_data.values())  # Convert values to a tuple

        # Add record_id to the values tuple
        values += (record_id,)

        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example Query: Update the record in the specified table using parameterized query
        query = f"UPDATE {table_name} SET {update_values} WHERE id = %s;"
        cursor.execute(query, values)  # Pass the values as a parameter to execute

        # Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": f"Record with ID {record_id} updated successfully in '{table_name}'."})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/sql/<string:table_name>/<int:record_id>', methods=['DELETE'])
def delete_record(table_name, record_id):
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**get_db_config())

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example Query: Delete the record from the specified table
        query = f"DELETE FROM {table_name} WHERE id = {record_id};"
        cursor.execute(query)

        # Commit the transaction and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": f"Record with ID {record_id} deleted successfully from '{table_name}'."})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
