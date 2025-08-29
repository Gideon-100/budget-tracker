# main.py
from database import create_table
from cli import run_cli

def main():
    # Initialize database
    create_table()

    # Start CLI
    run_cli()

if __name__ == "__main__":
    main()
