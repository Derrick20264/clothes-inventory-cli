from db.models import Store, ClothingItem

def list_stores():
    stores = Store.get_all()
    if not stores:
        print("No stores found.")
    for s in stores:
        print(f"ID: {s.id}, Name: {s.name}, Location: {s.location}")

def view_store_items(store_id):
    store = Store.find_by_id(store_id)
    if not store:
        print("store not found.")
        return            
    if not store .items:
        print("No items in this store.")
        return
    print(f"Items in {store.name}")
    for item in store.items:
        print(f"{item.id}: {item.name}, Size: {item.size}, Color: {item.color}, Price: ${item.price}")

def list_items():
    items = ClothingItem.get_all()
    if not items:
        print("No clothing items found.")
        return
    for item in items:
        print(f"ID: {item.id}, Name: {item.name}, Size: {item.size}, Color: {item.color}, Price: ${item.price}, Store ID: {item.store_id}")         