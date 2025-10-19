import mysql.connector

from mysql.connector import Error


try: 
  mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Rahbode25"
  )

  if mydb.is_connected():
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("DATABASE 'alx_book_store' created successfully")

except Error as e:
  print(f"Error while connecting to mySQL: {e}")

finally:
  if "cursor" in locals():
    cursor.close()
  if "mydb" in locals() and mydb.is_connected():
    mydb.close()