import streamlit as st
import pyperclip


# Define a function to copy the code snippet to the clipboard
def copy_to_clipboard(code):
    pyperclip.copy(code)
    st.success("Copied to clipboard!")


# App title
st.title("Comprehensive SQL & Python Code Snippets")

# SQL Snippets Dictionary
sql_snippets = {
    # DDL Commands
    "DDL - CREATE TABLE": """CREATE TABLE table_name (
    column_name1 data_type(size), 
    column_name2 data_type(size), 
    ...
);""",
    "DDL - CREATE DATABASE": "CREATE DATABASE database_name;",
    "DDL - CREATE INDEX": "CREATE INDEX index_name ON table_name (column_name);",
    "DDL - CREATE VIEW": """CREATE VIEW view_name AS 
SELECT columns 
FROM table_name 
WHERE conditions;""",
    "DDL - ALTER TABLE ADD COLUMN": "ALTER TABLE table_name ADD column_name data_type;",
    "DDL - ALTER TABLE DROP COLUMN": "ALTER TABLE table_name DROP COLUMN column_name;",
    "DDL - ALTER TABLE MODIFY COLUMN": "ALTER TABLE table_name MODIFY COLUMN column_name data_type;",
    "DDL - DROP TABLE": "DROP TABLE table_name;",
    "DDL - DROP DATABASE": "DROP DATABASE database_name;",
    "DDL - DROP INDEX": "DROP INDEX index_name;",
    "DDL - DROP VIEW": "DROP VIEW view_name;",
    "DDL - TRUNCATE TABLE": "TRUNCATE TABLE table_name;",
    "DDL - RENAME TABLE": "RENAME TABLE old_table_name TO new_table_name;",

    # DML Commands
    "DML - SELECT": "SELECT column1, column2 FROM table_name WHERE condition;",
    "DML - INSERT": "INSERT INTO table_name (column1, column2) VALUES (value1, value2);",
    "DML - UPDATE": "UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;",
    "DML - DELETE": "DELETE FROM table_name WHERE condition;",

    # DCL Commands
    "DCL - GRANT": "GRANT SELECT, INSERT ON table_name TO 'username';",
    "DCL - REVOKE": "REVOKE SELECT, INSERT ON table_name FROM 'username';",

    # TCL Commands
    "TCL - COMMIT": "COMMIT;",
    "TCL - ROLLBACK": "ROLLBACK;",
    "TCL - SAVEPOINT": "SAVEPOINT savepoint_name;",
    "TCL - RELEASE SAVEPOINT": "RELEASE SAVEPOINT savepoint_name;",
    "TCL - SET TRANSACTION": "SET TRANSACTION;",

    # DQL Commands
    "DQL - SELECT": "SELECT column1, column2 FROM table_name WHERE condition;",

    # Additional SQL Commands
    "JOIN": """SELECT columns 
FROM table1 
INNER JOIN table2 ON table1.column = table2.column;""",
    "UNION": """SELECT column1, column2 
FROM table1 
UNION 
SELECT column1, column2 
FROM table2;""",
    "INDEX": "CREATE INDEX index_name ON table_name (column_name);",
    "VIEW": """CREATE VIEW view_name AS 
SELECT column1, column2 
FROM table_name 
WHERE condition;""",
    "ORDER BY": """SELECT column1, column2 
FROM table_name 
ORDER BY column1 [ASC|DESC];""",
    "GROUP BY": """SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1;""",
    "HAVING": """SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1 
HAVING COUNT(*) > value;""",
    "DISTINCT": "SELECT DISTINCT column1 FROM table_name;",

    # Common SQL Queries
    "Basic Select": """SELECT * FROM table_name;""",
    "Select with Condition": """SELECT * FROM table_name WHERE condition;""",
    "Select Specific Columns": """SELECT column1, column2 FROM table_name;""",
    "Select with Order By": """SELECT * FROM table_name ORDER BY column1 [ASC|DESC];""",
    "Select with Group By": """SELECT column1, COUNT(*) FROM table_name GROUP BY column1;""",
    "Select with Having": """SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > value;""",
    "Select with Join": """SELECT table1.column1, table2.column2 
FROM table1 
INNER JOIN table2 ON table1.common_column = table2.common_column;""",
    "Select with Subquery": """SELECT column1 
FROM table_name 
WHERE column2 IN (SELECT column2 FROM another_table WHERE condition);""",

    # Advanced SQL Queries
    "Select Top N Records": """SELECT * FROM table_name ORDER BY column_name LIMIT N;""",
    "Select Distinct Records": """SELECT DISTINCT column1 FROM table_name;""",
    "Count Records": """SELECT COUNT(*) FROM table_name;""",
    "Sum Records": """SELECT SUM(column_name) FROM table_name;""",
    "Average Records": """SELECT AVG(column_name) FROM table_name;""",
    "Min/Max Records": """SELECT MIN(column_name), MAX(column_name) FROM table_name;""",
    "Update with Condition": """UPDATE table_name SET column1 = value1 WHERE condition;""",
    "Delete with Condition": """DELETE FROM table_name WHERE condition;""",

    # Python Database Connectors
    "Python - SQLite3": """import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM table_name;")
rows = cursor.fetchall()

# Close the connection
conn.close()""",

    "Python - MySQL Connector": """import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM table_name;")
rows = cursor.fetchall()

# Close the connection
conn.close()""",

    "Python - PostgreSQL Connector": """import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname='database_name',
    user='username',
    password='password',
    host='localhost'
)
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM table_name;")
rows = cursor.fetchall()

# Close the connection
conn.close()""",

    # Python Streamlit Application Example
    "Python - Streamlit with SQLite": """import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Streamlit app
st.title("Streamlit and SQLite")

# Query data
cursor.execute("SELECT * FROM table_name;")
data = cursor.fetchall()

# Display data
st.write(data)

# Close the connection
conn.close()""",

    # Python Tkinter Application Example
    "Python - Tkinter with MySQL": """import tkinter as tk
import mysql.connector

def fetch_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='username',
        password='password',
        database='database_name'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name;")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Tkinter app
root = tk.Tk()
root.title("Tkinter and MySQL")

data = fetch_data()

for row in data:
    tk.Label(root, text=row).pack()

root.mainloop()""",

    # Python CustomTkinter Application Example
    "Python - CustomTkinter with PostgreSQL": """import customtkinter as ctk
import psycopg2

def fetch_data():
    conn = psycopg2.connect(
        dbname='database_name',
        user='username',
        password='password',
        host='localhost'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name;")
    rows = cursor.fetchall()
    conn.close()
    return rows

# CustomTkinter app
app = ctk.CTk()
app.title("CustomTkinter and PostgreSQL")

data = fetch_data()

for row in data:
    ctk.CTkLabel(app, text=row).pack()

app.mainloop()"""
}

# Sidebar selection
st.sidebar.title("Select a Category")
categories = list(sql_snippets.keys())
selected_category = st.sidebar.selectbox("Select a category", categories)

# Display selected SQL snippet or Python code
st.subheader(selected_category)
st.code(sql_snippets[selected_category])

# Copy button
if st.button("Copy to Clipboard"):
    copy_to_clipboard(sql_snippets[selected_category])
