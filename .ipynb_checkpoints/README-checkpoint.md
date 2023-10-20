# Flask MySQL CRUD API

Flask MySQL CRUD API provides a simple RESTful interface for basic database operations on MySQL tables. It supports creating, updating, deleting tables, inserting, retrieving, updating, and deleting records.

## Features

- **Create Table:**
  - **Endpoint:** `POST /sql`
  - **Payload:**
    ```json
    {
      "name": "table_name",
      "columns": ["column1 datatype", "column2 datatype"]
    }
    ```

- **Add Columns to Table:**
  - **Endpoint:** `PUT /sql/<table_name>`
  - **Payload:**
    ```json
    {
      "columns": ["new_column1 datatype", "new_column2 datatype"]
    }
    ```

- **Insert Record:**
  - **Endpoint:** `POST /sql/<table_name>`
  - **Payload:**
    ```json
    {
      "column1": "value1",
      "column2": "value2"
    }
    ```

- **Get All Records:**
  - **Endpoint:** `GET /sql/<table_name>`

- **Update Record:**
  - **Endpoint:** `PUT /sql/<table_name>/<record_id>`
  - **Payload:**
    ```json
    {
      "column1": "new_value1",
      "column2": "new_value2"
    }
    ```

- **Delete Record:**
  - **Endpoint:** `DELETE /sql/<table_name>/<record_id>`

## Technologies Used

- Flask
- MySQL
- Flask-CORS

## How to Run

1. Clone the repository.
2. Install required packages: `pip install -r requirements.txt`.
3. Set up MySQL database configuration in `app.py`.
4. Run the Flask app: `python app.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
