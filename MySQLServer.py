import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "GaWiMu-09!",
)

mycursor = mydb.cursor()

if mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store"):
    print("Database 'alx_book_store' created successfully!")
else:
    raise Exception (f"Failed to Connect to Database.")
    print("Error Trying to Connect to Database.")

mycursor.close()
mydb.close()

