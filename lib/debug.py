from models import Store, ClothingItem, session

# create
store = Store.create("Nairobi Branch", "CBD")
item = ClothingItem.create("T-Shirt", "M", "Black", 1200, store.id)

# read
print(Store.get_all())
print(ClothingItem.get_all())

# update (if you add it)
item.price = 1500
session.commit()

# delete
ClothingItem.delete(item.id)
