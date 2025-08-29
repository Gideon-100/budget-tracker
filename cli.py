# cli.py
from models import add_expense, view_expenses, delete_expense

def run_cli():
    """Run the command-line interface for the budget tracker."""
    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter amount: "))
            add_expense(name, amount)
            print("Expense added successfully!")

        elif choice == "2":
            expenses = view_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                print("\nExpenses:")
                for expense in expenses:
                    print(f"{expense[0]}. {expense[1]} - ${expense[2]}")

        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted successfully!")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


