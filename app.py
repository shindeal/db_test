import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import urllib

# Database connection details
server = "L1SQLS1601P\\SpeedyDWAnalytic"
database = "Speedy_Models"
driver = "ODBC Driver 17 for SQL Server"

# Create a connection string
params = urllib.parse.quote_plus(f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;")
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

# Function to establish a database connection and retrieve data
@st.cache_data
def get_data(query):
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        data = pd.read_sql(query, conn)
    return data

# Streamlit app
def main():
    st.title("SQL Server Data Viewer")

    # SQL query to execute
    query = "SELECT TOP 10 * FROM dim_depot with (nolock)"  # Adjust the query as needed

    # Retrieve data from the database
    data = get_data(query)

    # Display the data in Streamlit
    st.write(data)

if __name__ == "__main__":
    main()
