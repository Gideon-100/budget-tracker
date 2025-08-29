import sqlite3

DB_NAME = "budget.db"

def get_connection():
    """Create a database connection and return the connection object."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    """Create expenses table if it does not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
