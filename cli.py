# cli.py  
from datetime import datetime
from database import SessionLocal
from models import User, Category, Expense

def _prompt_nonempty(msg):
    while True:
        v = input(msg).strip()
        if v:
            return v
        print("Please enter a value.")

def _prompt_float(msg):
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("Enter a valid number (e.g., 250 or 1200.50).")

def add_user():
    name = _prompt_nonempty("User name: ")
    with SessionLocal() as s:
        u = User(name=name)
        s.add(u)
        s.commit()
        s.refresh(u)
        print(f"Added user: {u.id} - {u.name}")

def add_category():
    name = _prompt_nonempty("Category name: ")
    with SessionLocal() as s:
        
        existing = s.query(Category).filter(Category.name == name).first()
        if existing:
            print("Category already exists.")
            return
        c = Category(name=name)
        s.add(c)
        s.commit()
        s.refresh(c)
        print(f"Added category: {c.id} - {c.name}")

def add_expense():
    desc = _prompt_nonempty("Description: ")
    amt = _prompt_float("Amount: ")
    # list categories
    with SessionLocal() as s:
        cats = s.query(Category).order_by(Category.id).all()
        if cats:
            print("Categories:")
            for c in cats:
                print(f"  {c.id}. {c.name}")
            cat_in = input("Category id (blank = none): ").strip()
            cat_id = int(cat_in) if cat_in else None
        else:
            print("No categories yet.")
            cat_id = None

        users = s.query(User).order_by(User.id).all()
        if users:
            print("Users:")
            for u in users:
                print(f"  {u.id}. {u.name}")
            user_in = input("User id (blank = none): ").strip()
            user_id = int(user_in) if user_in else None
        else:
            print("No users yet.")
            user_id = None

        date_in = input("Date YYYY-MM-DD (blank = today): ").strip()
        if date_in:
            try:
                exp_date = datetime.strptime(date_in, "%Y-%m-%d").date()
            except ValueError:
                print("Bad date — using today.")
                exp_date = None
        else:
            exp_date = None

        e = Expense(description=desc, amount=amt, category_id=cat_id, user_id=user_id)
        if exp_date:
            e.date = exp_date
        s.add(e)
        s.commit()
        s.refresh(e)
        print(f"Added expense: {e.id} | {e.description} | {e.amount}")

def view_expenses():
    with SessionLocal() as s:
        rows = s.query(Expense).order_by(Expense.date.desc()).all()
        if not rows:
            print("No expenses yet.")
            return
        print("\nID | Date       | Amount   | Category   | User   | Description")
        print("---+------------+----------+------------+--------+----------------")
        for r in rows:
            cat = r.category.name if r.category else ""
            usr = r.user.name if r.user else ""
            print(f"{r.id:2} | {str(r.date)} | {r.amount:8} | {cat[:10]:10} | {usr[:6]:6} | {r.description[:30]}")

def delete_expense():
    view_expenses()
    id_in = input("Expense id to delete (or blank to cancel): ").strip()
    if not id_in:
        return
    try:
        eid = int(id_in)
    except ValueError:
        print("Invalid id.")
        return
    with SessionLocal() as s:
        e = s.get(Expense, eid)
        if not e:
            print("No such expense.")
            return
        s.delete(e)
        s.commit()
        print("Deleted.")

def run_cli():
    print("Simple Budget Tracker (SQLAlchemy) — student version")
    # seed a couple categories for convenience if none exist
    with SessionLocal() as s:
        if s.query(Category).count() == 0:
            s.add_all([Category(name="Food"), Category(name="Rent"), Category(name="Transport")])
            s.commit()
    while True:
        print("\nMenu:")
        print("1) Add user")
        print("2) Add category")
        print("3) Add expense")
        print("4) View expenses")
        print("5) Delete expense")
        print("6) Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            add_user()
        elif choice == "2":
            add_category()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            view_expenses()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Bye 👋")
            break
        else:
            print("Invalid choice.")



