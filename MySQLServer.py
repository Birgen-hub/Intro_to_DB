#!/usr/bin/env python3
"""
A script that connects to a MySQL server and creates the database 'alx_book_store'
if it does not already exist, without using SELECT or SHOW statements.
Uses the pymysql library for a cleaner connection.
"""
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
        # Attempt connection using pymysql
        connection = pymysql.connect(**MYSQL_CONFIG)
        
        cursor = connection.cursor()
        
        # Required command
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        cursor.execute(create_db_query)
        
        # Required print message
        print("Database 'alx_book_store' created successfully!")

        cursor.close()

    except pymysql.Error as err:
        # Required error message
        print(f"Error: Failed to connect to MySQL or execute command. Details: {err}")

    finally:
        # Handle open and close of the DB connection
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
