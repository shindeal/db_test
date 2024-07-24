import streamlit as st
import pyodbc

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
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

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Sample SQL query, replace with your actual query.
query = """
SELECT TOP 10 * FROM dim_depot with (nolock)
"""

rows = run_query(query)

# Print results.
for row in rows:
    st.write(row)
