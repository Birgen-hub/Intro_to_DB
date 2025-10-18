import mysql.connector
import sys

# --- IMPORTANT: CONNECTION DETAILS ---
HOST_NAME = "localhost"
USER_NAME = "root"
# FIX THIS LINE: Use the actual password you set for the root user.
USER_PASSWORD = "Birgen@99"  
DATABASE_NAME = "hr_db"

def connect_to_database():
    """
    Establishes a connection to the MySQL database and prints the server info.
    """
    try:
        print(f"Attempting to connect to '{DATABASE_NAME}' as user '{USER_NAME}'...")
        
        # 1. Connect to the database
        mydb = mysql.connector.connect(
            host=HOST_NAME,
            user=USER_NAME,
            password=USER_PASSWORD,
            database=DATABASE_NAME
        )

        # 2. Check and print server information if successful
        if mydb.is_connected():
            print("\nConnection Successful!")
            print("-" * 30)
            print(f"Server Information: {mydb.get_server_info()}")
            print(f"Connection ID: {mydb.connection_id}")
            print("-" * 30)
            
            # Close the connection
            mydb.close()
            print("Connection closed.")
        
    except mysql.connector.Error as err:
        # 3. Handle common connection errors
        if err.errno == 1045:
            print(f"\nConnection Failed (Error 1045): Access denied for user '{USER_NAME}'.")
            print("Please double-check the 'USER_PASSWORD' in the script.")
        elif err.errno == 2003:
            print(f"\nConnection Failed (Error 2003): Cannot connect to MySQL server on '{HOST_NAME}'.")
            print("Ensure your MySQL server is running.")
        else:
            print(f"An error occurred: {err}")
            sys.exit(1)

if __name__ == "__main__":
    connect_to_database()
