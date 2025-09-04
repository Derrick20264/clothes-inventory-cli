from lib.db.models import Base, Store, ClothingItem, session

# Clear existing data
session.query(ClothingItem).delete()
session.query(Store).delete()

# Add sample stores
store1 = Store(name="Fashion Hub", location="Downtown")
store2 = Store(name="Trendy Wear", location="Uptown")

# Add clothing items
shirt = ClothingItem(name="T-Shirt", size="M", color="Blue", price=15.0, store=store1)
jeans = ClothingItem(name="Jeans", size="32", color="Black", price=40.0, store=store1)
dress = ClothingItem(name="Summer Dress", size="S", color="Red", price=30.0, store=store2)

# Commit to DB
session.add_all([store1, store2, shirt, jeans, dress])
session.commit()
session.close()
