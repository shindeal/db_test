import streamlit as st
import pyodbc
import pandas as pd

# Database connection details
connection_string = r"Driver={SQL Server};Server=L1SQLS1601P\SpeedyDWAnalytic;Database=Speedy_Models;Trusted_Connection=yes;"

# Function to establish a database connection
def get_connection():
    conn = pyodbc.connect(connection_string)
    return conn

# Function to query data from the database
def get_data(query):
    conn = get_connection()
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Streamlit app
def main():
    st.title("SQL Server Data Viewer")

    # SQL query to execute
    query = "SELECT TOP 10 * FROM YourTableName"  # Adjust the query as needed

    # Retrieve data from the database
    data = get_data(query)

    # Display the data in Streamlit
    st.write(data)

if __name__ == "__main__":
    main()
