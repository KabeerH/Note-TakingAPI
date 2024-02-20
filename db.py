import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()


def get_database_connection():
    """
    This function will connect to the mysql database (display confirmation message if connected to each request)
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
        print("Connection to database successful!")
    except Error as err:
        print(f"Error: {err}")
    return connection
