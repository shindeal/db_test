import streamlit as st
import pyodbc
import pandas as pd

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=" + st.secrets["server"] + ";"
        "DATABASE=" + st.secrets["database"] + ";"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(connection_string)

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        columns = [column[0] for column in cur.description]
        data = cur.fetchall()
        return columns, data

query = "SELECT TOP 10 * FROM dim_depot with (nolock);"

# Retrieve data from the database
columns, rows = run_query(query)

# Print results.
st.write("### Query Results")
df = pd.DataFrame(rows, columns=columns)
st.write(df)
