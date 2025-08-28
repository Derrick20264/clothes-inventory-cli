from models import Base, Customer, Clothes, Purchase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

engine = create_engine("sqlite:///clothes_store.db")
Session = sessionmaker(bind=engine)
session = Session()

# Clear tables
session.query(Purchase).delete()
session.query(Customer).delete()
session.query(Clothes).delete()

# Add sample customers
c1 = Customer(name="Alice", email="alice@email.com", phone="12345")
c2 = Customer(name="Bob", email="bob@email.com", phone="67890")

# Add clothes
shirt = Clothes(name="T-Shirt", category="Top", price=15.0, quantity=20)
jeans = Clothes(name="Jeans", category="Bottom", price=30.0, quantity=10)

# Commit
session.add_all([c1, c2, shirt, jeans])
session.commit()
session.close()
