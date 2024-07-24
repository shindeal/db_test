import streamlit as st
import pyodbc

# Function to initialize the connection
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["db"]["server"]
        + ";DATABASE="
        + st.secrets["db"]["database"]
        + ";UID="
        + st.secrets["db"]["username"]
        + ";PWD="
        + st.secrets["db"]["password"]
    )

# Function to test the connection
def test_connection():
    try:
        conn = init_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        if result:
            st.write("Connection to SQL Server successful!")
        else:
            st.write("Connection successful but no result fetched.")
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit app
def main():
    st.title("SQL Server Connection Test")
    test_connection()

if __name__ == "__main__":
    main()
