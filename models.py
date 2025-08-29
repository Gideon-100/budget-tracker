# models.py
import sqlite3
from database import get_connection, create_table

create_table()

def add_expense(name, amount):
    """Insert a new expense into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()

def view_expenses():
    """Retrieve all expenses from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    """Delete an expense by its ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
