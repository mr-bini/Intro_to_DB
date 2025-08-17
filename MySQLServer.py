import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",       # Change if needed
            user="root",            # Your MySQL username
            password="your_password"  # Your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database (won't fail if it exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")  # optional log


if __name__ == "__main__":
    create_database()
