import psycopg2

DB_NAME = "calculator_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id SERIAL PRIMARY KEY,
            expression TEXT NOT NULL,
            result TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    connection.commit()
    cursor.close()
    connection.close()


def save_operation(expression, result):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO operations (expression, result) VALUES (%s, %s)",
        (expression, str(result))
    )

    connection.commit()
    cursor.close()
    connection.close()


def get_history():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, expression, result, created_at FROM operations ORDER BY id DESC"
    )

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


def clear_history():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM operations")

    connection.commit()
    cursor.close()
    connection.close()
