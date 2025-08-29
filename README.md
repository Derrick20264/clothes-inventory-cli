# Clothes Inventory CLI

A simple command-line interface (CLI) application for managing a clothes inventory.  
Built with **Python** and **SQLite**, this project demonstrates CRUD operations, clean code design, and error handling.

---

## Learning Goals
This project was created to demonstrate:
- Building a Python CLI application from scratch.
- Performing **CRUD operations** (Create, Read, Update, Delete) with SQLite.
- Applying **clean coding practices** and modular design.
- Using **error handling** and input validation for better user experience.
- Communicating technical concepts clearly through documentation.

---

## Requirements
- Python 3.8+
- SQLite (built-in with Python)
- Optional: [tabulate](https://pypi.org/project/tabulate/) for nicer table formatting

Install tabulate if you want formatted tables:
```bash
pip install tabulate

## Installation
1. Clone this repository:

git clone git@github.com:Derrick20264/clothes-inventory-cli.git
cd clothes-inventory-cli

2. Ensure you have a SQLite database. A sample clothes_inventory.db is included.
To create your own, run:
sqlite3 clothes_inventory.db ".databases"

3. Run the CLI:
python cli.py

## Usage

After starting the program, you will see a menu like this:

===== Clothes Inventory Management =====
1. View all items
2. Add new item
3. Update item
4. Delete item
5. Exit

## Project Structure
clothes-inventory-cli/
│-- cli.py                # Main application logic
│-- clothes_inventory.db   # SQLite database
│-- README.md              # Project documentation

## Author

Created by Derrick Wachira as a Phase Project.
This project demonstrates Python fundamentals, database management, and technical communication.

## License
This project is for educational purposes only (Phase 3 Python + SQLAlchemy CLI project).  
No permission is granted to use this project for commercial purposes.
