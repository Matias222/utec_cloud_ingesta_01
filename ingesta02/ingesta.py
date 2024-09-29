import mysql.connector
import csv
import boto3
import os

# MySQL connection setup
try:
    connection = mysql.connector.connect(
        host='18.212.248.216',    
        user='myuser',         
        password='utecontra', 
        database='mydb'       
    )

    if connection.is_connected():
        print("Successfully connected to the database")

    # Create a cursor object
    cursor = connection.cursor()

    # Execute SELECT * FROM cars
    select_query = "SELECT * FROM cars"
    cursor.execute(select_query)

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Column names for the CSV file
    column_names = [i[0] for i in cursor.description]

    # Write the results to a CSV file
    csv_file = "data.csv"
    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(column_names)  # Write the header (column names)
        csv_writer.writerows(rows)         # Write the data rows

    print(f"Data written to {csv_file} successfully")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# S3 Upload Setup
ficheroUpload = csv_file  # File to upload
nombreBucket = "matias-balde"  # Replace with your S3 bucket name

# Initialize the S3 client
s3 = boto3.client('s3')

# Upload the CSV file to the specified S3 bucket
try:
    s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
    print(f"Ingesta completada, file uploaded to S3 bucket: {nombreBucket}")
except Exception as e:
    print(f"Error uploading file to S3: {e}")
