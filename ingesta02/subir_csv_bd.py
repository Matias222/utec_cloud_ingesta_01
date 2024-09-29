import mysql.connector

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host='18.212.248.216',      # Replace with your MySQL host
        user='myuser',         # Replace with your MySQL username
        password='utecontra', # Replace with your MySQL password
        database='mydb'        # Replace with your MySQL database
    )

    if connection.is_connected():
        print("Successfully connected to the database")

    # Create a cursor object
    cursor = connection.cursor()

    # Drop the table if it already exists (optional)
    cursor.execute("DROP TABLE IF EXISTS cars")

    # Create the 'cars' table
    create_table_query = '''
    CREATE TABLE cars (
      brand VARCHAR(255),
      model VARCHAR(255),
      year INT
    )
    '''
    cursor.execute(create_table_query)
    print("Table 'cars' created successfully")

    # Insert two records into the 'cars' table
    insert_query = '''
    INSERT INTO cars (brand, model, year)
    VALUES (%s, %s, %s)
    '''
    records_to_insert = [
        ('Toyota', 'Camry', 2020),
        ('Honda', 'Civic', 2019)
    ]
    cursor.executemany(insert_query, records_to_insert)
    connection.commit()

    print("Two records inserted successfully")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
