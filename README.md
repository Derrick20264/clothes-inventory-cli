# Clothes Inventory CLI

A command-line interface (CLI) application for managing clothing stores and their inventory.  
Built with **Python** and **SQLAlchemy**, this app allows you to create, view, update, and delete stores and clothing items.

---

## Features
- Manage **Stores**
  - Add a new store
  - View all stores
  - Update store details
  - Delete a store (and its items)

- Manage **Clothing Items**
  - Add a new clothing item to a store
  - View all clothing items
  - Update clothing item details
  - Delete clothing items

---

## Requirements
- Python 3.8+
- Virtual environment (recommended)

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd clothes-inventory-cli

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run database migrations (tables will be created automatically when running the app).
## Usage

Start the CLI:

python cli.py


You’ll see a menu with options like:

Manage Stores

Manage Clothing Items

Exit

Follow the prompts to interact with the inventory system.

## File Structure
clothes-inventory-cli/
│
├── lib/
│   └── db/
│       └── models.py        # SQLAlchemy models for Store & ClothingItem
│
├── cli.py                   # Main CLI entry point
├── requirements.txt         # Project dependencies
└── README.md                # Documentation

## License

This project is for educational purposes (Phase 3 Python + SQLAlchemy CLI project).