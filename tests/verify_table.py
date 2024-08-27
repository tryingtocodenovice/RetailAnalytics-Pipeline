import sqlite3

def verify_table(table_name):
    # Connect to the SQLite database
    db_path = '../retailanalytics.db'
    conn = sqlite3.connect(db_path)
    
    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query to fetch data from the table
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 10")

        # Fetch the column names
        column_names = [description[0] for description in cursor.description]

        # Fetch the data rows
        rows = cursor.fetchall()

        # Print the column names
        print(f"Table: {table_name}")
        print(" | ".join(column_names))

        # Print each row of data
        for row in rows:
            print(" | ".join(str(value) for value in row))
        
        print("\n" + "="*50 + "\n")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()

# List of tables to verify
tables_to_verify = ["table_1", "table_2", "joined_table", "hourly_trend", "event_type_counts"]

# Verify each table
for table in tables_to_verify:
    verify_table(table)
