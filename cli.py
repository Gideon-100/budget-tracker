# cli.py
from database import create_table, get_connection

def add_expense(name, amount):
    """Add a new expense to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()
    print(f"✅ Added expense: {name} - {amount} KES")

def view_expenses():
    """View all expenses stored in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\n📋 Your Expenses:")
        for row in rows:
            print(f"{row[0]}. {row[1]} - {row[2]} KES")
    else:
        print("\n⚠️ No expenses recorded yet.")

def menu():
    """Display the CLI menu."""
    create_table()
    while True:
        print("\n=== Budget Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter expense name: ")
            try:
                amount = float(input("Enter amount: "))
                add_expense(name, amount)
            except ValueError:
                print("⚠️ Please enter a valid number for amount.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Goodbye! Your expenses are saved.")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

