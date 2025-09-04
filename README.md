# Clothes Inventory CLI

A simple command-line interface (CLI) application for managing a clothes inventory.  
Built with **Python** and **SQLite**, this project demonstrates CRUD operations, clean code design, and error handling.



## Learning Goals
This project was created to demonstrate:
- Building a Python CLI application from scratch.
- Performing **CRUD operations** (Create, Read, Update, Delete) with SQLite.
- Applying **clean coding practices** and modular design.
- Using **error handling** and input validation for better user experience.
- Communicating technical concepts clearly through documentation.



## Requirements
- Python 3.8+
- SQLite (built-in with Python)
- Pipenv (for managing dependencies)

## Installation
1. Clone this repository: 
```bash
git clone git@github.com:Derrick20264/clothes-inventory-cli.git
cd clothes-inventory-cli
```
2. Install dependencies using Pipenv:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Usage

Run the CLI application:
```bash
python -m lib.db.seed
```
Confirm seeded data:
```bash
sqlite3 clothes_store.db "SELECT * FROM stores;"
sqlite3 clothes_store.db "SELECT * FROM clothing_items;"
```
**Database**
- stores: id, name, location

- clothing_items: id, name, size, color, price, store_id

**Sample Data**
Stores:
1 | Fashion Hub | Downtown
2 | Trendy Wear | Uptown

Clothing Items:
1 | T-Shirt       | M  | Blue  | 15.0 | Store 1
2 | Jeans         | 32 | Black | 40.0 | Store 1
3 | Summer Dress  | S  | Red   | 30.0 | Store 2


Main Menu Options:

1. **Stores**

- List Stores

- Add Store

- Delete Store

- Update Store

- View Store Items

2. **Clothing Items**

- List Clothing Items

- Add Clothing Item

- Delete Clothing Item

- Update Clothing Item

3. **Exit**


## Author

Created by Derrick Wachira as a Phase Project.

## License
This project is for educational purposes only (Phase 3 Python + SQLAlchemy CLI project).  


