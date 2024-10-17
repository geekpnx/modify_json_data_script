import psycopg2
import json

# Connect to your PostgreSQL database
conn = psycopg2.connect(
# Connection parameters
    dbname = "prosffer_db",
    user = "prosffer_user",
    password = "password123",
    host = "localhost"  # Or your remote server address
)

# Create a cursor
cur = conn.cursor()

# Execute the SQL query to get data from the table
cur.execute("SELECT store, name, price, currency, category, description, image, link, id_tag FROM product_product")

# Fetch all rows
rows = cur.fetchall()

# Get the column names
colnames = [desc[0] for desc in cur.description]

# Convert rows into a list of dictionaries
data = [dict(zip(colnames, row)) for row in rows]

# Write data to JSON file
with open('/Users/t.r.n.c/Documents/DCI/PythonClass/FINAL_PROJECT/Projects/testing_project_2/product_data/prosffer_product_data_backup.json', 'w') as f:
    json.dump(data, f, indent=4)

# Close the cursor and connection
cur.close()
conn.close()