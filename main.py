# main.py
from database import init_db
from cli import run_cli

def main():
    init_db()     # create tables if needed
    run_cli()

if __name__ == "__main__":
    main()
