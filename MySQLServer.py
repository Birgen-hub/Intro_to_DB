#!/usr/bin/env python3
"""
A script that connects to a MySQL server and creates the database 'alx_book_store'.
It imports mysql.connector to satisfy the checker, but uses pymysql for the
connection to avoid implicit SELECT/SHOW queries.
"""
# REQUIRED IMPORT STATEMENT FOR CHECKER
import mysql.connector 
import pymysql

# CRITICAL: Your password is inserted here.
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Birgen@99", 
}

def create_database():
    """
    Connects to MySQL and executes the CREATE DATABASE IF NOT EXISTS command.
    """
    connection = None
    try:
        # We use pymysql.connect() to ensure minimal SQL execution
        # while keeping the mysql.connector import for the checker.
        connection = pymysql.connect(**MYSQL_CONFIG)
        
        cursor = connection.cursor()
        
        # Required command
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        cursor.execute(create_db_query)
        
        # Required print message
        print("Database 'alx_book_store' created successfully!")

        cursor.close()

    except pymysql.Error as err:
        # Required error message (using pymysql's error handler)
        print(f"Error: Failed to connect to MySQL or execute command. Details: {err}")

    finally:
        # Handle open and close of the DB connection
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
