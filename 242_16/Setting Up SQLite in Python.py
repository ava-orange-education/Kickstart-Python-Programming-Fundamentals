import sqlite3

# Create a connection to the database
connection = sqlite3.connect('example.db')
# Create a cursor object
cursor = connection.cursor()
print("Database created and connected successfully")
# Close the connection
connection.close()
print("Connection closed")
