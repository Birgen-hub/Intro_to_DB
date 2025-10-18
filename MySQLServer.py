#!/usr/bin/env python3
"""
A script that connects to a MySQL server and creates the database 'alx_book_store'
if it does not already exist, without using SELECT or SHOW statements.
"""
import mysql.connector

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Birgen@99" 
}

def create_database():
    """
    Connects to MySQL and executes the CREATE DATABASE IF NOT EXISTS command.
    """
    connection = None
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")
            cursor.close()

    except mysql.connector.Error as err:
        print(f"Error: Failed to connect to MySQL or execute command. Details: {err}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
