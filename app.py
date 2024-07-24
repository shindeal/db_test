import streamlit as st
import pyodbc
import pandas as pd


# Function to establish a database connection
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
        + ";Connection Timeout=30;"  # Increase timeout to 30 seconds
    )


# Function to query data from the database
@st.cache_data(ttl=600)
def get_data(query):
    conn = get_connection()
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Streamlit app
def main():
    st.title("SQL Server Data Viewer")

    # SQL query to execute
    query = "SELECT TOP 10 * FROM dim_depot WITH (NOLOCK)"  # Adjust the query as needed

    # Retrieve data from the database
    data = get_data(query)

    # Display the data in Streamlit
    #st.write("### Query Results")
    st.table(data)



if __name__ == "__main__":
    main()
