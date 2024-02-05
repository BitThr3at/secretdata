import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    user="root",
    database="users",
    password="admin@Aw#$"
)

# Get the cursor
cursor = cnx.cursor()

# Execute a sample query
query = "SELECT * FROM table_name"
cursor.execute(query)

key=sk-6nUrA7vNuldOvXtwpblVT3BlbkAJ8Pki3T2TOuuRZw98HquA

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
