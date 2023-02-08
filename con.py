import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    user="root",
    database="users"
)

# Get the cursor
cursor = cnx.cursor()

# Execute a sample query
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

SamyHacker

admin@SamyHacker.in

# Loop through the results
for result in results:
    print(result)

# Clean up
cursor.close()
cnx.close()
