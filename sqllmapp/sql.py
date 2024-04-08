import sqlite3
import pandas as pd

# Function to create a connection to SQLite database
def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        print("Connection to SQLite database successful!")
        return conn
    except sqlite3.Error as e:
        print("Error: ", e)
        return None

# Function to create a table in SQLite database based on Excel file contents
def create_table_from_excel(conn, excel_file):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file)
        
        # Generate table schema based on column names and data types
        table_schema = ", ".join([f'"{col}" TEXT' for col in df.columns])
        
        # Create table in SQLite database
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS STUDENT ({table_schema})")
        conn.commit()
        print("Table created successfully!")
    except Exception as e:
        print("Error: ", e)

# Function to insert data from Excel file into SQLite database
def insert_data_from_excel(conn, excel_file):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file)
        
        # Insert DataFrame records into SQLite database
        df.to_sql('STUDENT', conn, if_exists='append', index=False)
        
        print("Data inserted successfully!")
    except Exception as e:
        print("Error: ", e)

# Main function
def main():
    # Connect to SQLite database
    database = "justpay.db"
    conn = create_connection(database)
    if conn is None:
        return
    
    # Create table in the database based on Excel file contents
    excel_file = "justpaydata.xlsx"  # Replace 'your_file.xlsx' with your actual file path
    create_table_from_excel(conn, excel_file)
    
    # Insert data from Excel file into the database
    insert_data_from_excel(conn, excel_file)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
