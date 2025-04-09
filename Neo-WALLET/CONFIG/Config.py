import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()

# Set your database connection parameters
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT"))
}

try:
    # Create a connection pool
    connection_pool = pooling.MySQLConnectionPool(pool_name="pool",
                                                  pool_size=10,
                                                  **db_config)
except mysql.connector.Error as err:
    print(f"Error: {err}")

def get_connection():
    # Get a connection from the pool
    return connection_pool.get_connection()

def close_connection(conn, cursor):
    # Close the cursor and return the connection to the pool
    cursor.close()
    conn.close()











# import mysql.connector
# # import main 

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Vivek@123",
#         database="transaction_wallet",
#         port=3306
#     )
#     if conn.is_connected():
#         print("Connected to the MySQL database.")
#     else:
#         print("Failed to connect to the MySQL database.")

#     cursor1 = conn.cursor()
#     cursor2 = conn.cursor()
#     cursor3 = conn.cursor()
#     cursor4 = conn.cursor()

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

