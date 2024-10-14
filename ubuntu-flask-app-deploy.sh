#!/bin/bash

sudo -i

# 1. Install Flask and the MySQL connector for Python
sudo apt-get update
sudo apt-get install python3-pip
pip3 install Flask mysql-connector-python

# 2. Connect to MySQL (Obs: After installing MySQL)
mysql -u root -p

# To create a new user and database, enter the following. Replace 'your_password' with a strong password
# CREATE DATABASE flask_app_db;
# CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'your_password';
# GRANT ALL PRIVILEGES ON flask_app_db.* TO 'flask_user'@'localhost';
# FLUSH PRIVILEGES;
# # Grant access to zoneminder database (Optional)
# GRANT ALL PRIVILEGES ON zm.* TO 'flask_user'@'localhost';
# FLUSH PRIVILEGES;
# EXIT;

# 3. Configure Firewall and Network Settings:
# Make sure that your Flask application is accessible from the network. You may need to configure firewall rules in Google Compute Engine to allow incoming traffic on the port your Flask application is running on (usually port TCP 5000 for development).

# 3.1 Adjust app permision
sudo chown -R root:root /usr/local/zm-flask-app

# 4. Connect Flask Application to MySQL:
# In your Flask application code, you can use Flask-MySQLdb to connect to the MySQL database:

# Put the code below in your_flask_app.py file

    # from flask import Flask
    # import mysql.connector
    
    # app = Flask(__name__)
    
    # # Database Configuration
    # db_config = {
    #     "host": "localhost",
    #     "user": "flask_user",
    #     "password": "your_password",
    #     "database": "flask_app_db"
    # }
    
    # @app.route('/hello', methods=['GET'])
    # def say_hello():
    #     return "Hello, world!"
    
    # @app.route('/')
    # def index():
    #     try:
    #         # Establish a connection to the database
    #         connection = mysql.connector.connect(**db_config)
    
    #         # Create a cursor object to execute SQL queries
    #         cursor = connection.cursor()
    
    #         # Example Query: Select all rows from a table
    #         query = "SELECT * FROM your_table;"  # Replace 'your_table' with your specific table name or replace the entire query
    #         cursor.execute(query)
    
    #         # Fetch all rows from the result set
    #         data = cursor.fetchall()
    
    #         # Close the cursor and connection
    #         cursor.close()
    #         connection.close()
    
    #         return str(data)
    
    #     except Exception as e:
    #         return str(e)
    
    # if __name__ == '__main__':
    #     app.run(debug=True)

# Note: Replace 'your_table' with the name of the table you want to query.

# 5. Run Flask Application:
# Run your Flask application. You can run it in the background using tools like nohup to keep it running even when you log out:

# nohup python3 your_flask_app.py &
# Replace 'your_flask_app.py' with the name of your Flask application file.
