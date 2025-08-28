# test_cli_orm.py
from lib.db.models import Base, Store, ClothingItem
from lib.db.db import engine, session

# Ensure tables exist
Base.metadata.create_all(engine)

# Clear existing data for a fresh test
session.query(ClothingItem).delete()
session.query(Store).delete()
session.commit()

# Test store creation
store = Store.create(name="Downtown Store", location="Nairobi")
print("Store created:", store.name, store.location)

# Test getting all stores
stores = Store.get_all()
print("All stores:", [(s.id, s.name) for s in stores])

# Test creating a clothing item
item = ClothingItem.create(
    name="T-Shirt", size="M", color="Blue", price=1500, store_id=store.id
)
print("Clothing item created:", item.name, item.size, item.color, item.price)

# Test getting all clothing items
items = ClothingItem.get_all()
print("All clothing items:", [(i.id, i.name) for i in items])
