# lib/db/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database file
engine = create_engine("sqlite:///lib/db/clothes_store.db")

# Session factory
Session = sessionmaker(bind=engine)
session = Session()

