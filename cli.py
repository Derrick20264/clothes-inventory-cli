 # cli.py
# cli.py
from lib.db.models import Store, ClothingItem, session


def menu():
    print("\n=== CLOTHES INVENTORY CLI ===")
    print("1. View all stores")
    print("2. Add a store")
    print("3. Delete a store")
    print("4. View all clothing items")
    print("5. Add a clothing item")
    print("6. Update a clothing item")
    print("7. Delete a clothing item")
    print("0. Exit")


def view_stores():
    stores = Store.get_all()
    if not stores:
        print("No stores found.")
    for store in stores:
        print(f"[{store.id}] {store.name} - {store.location}")


def add_store():
    name = input("Enter store name: ").strip()
    location = input("Enter store location: ").strip()
    try:
        store = Store.create(name, location)
        print(f" Store '{store.name}' added successfully.")
    except Exception as e:
        print(f" Error: {e}")


def delete_store():
    store_id = input("Enter store ID to delete: ").strip()
    if store_id.isdigit() and Store.delete(int(store_id)):
        print(" Store deleted.")
    else:
        print(" Store not found.")


def view_items():
    items = ClothingItem.get_all()
    if not items:
        print("No clothing items found.")
    for item in items:
        store_name = item.store.name if item.store else "No store"
        print(f"[{item.id}] {item.name} | {item.size} | {item.color} | ${item.price:.2f} | Store: {store_name}")


def add_item():
    name = input("Enter item name: ").strip()
    size = input("Enter size: ").strip()
    color = input("Enter color: ").strip()
    price = float(input("Enter price: ").strip())
    store_id = int(input("Enter store ID: ").strip())

    try:
        item = ClothingItem.create(name, size, color, price, store_id)
        print(f" Item '{item.name}' added successfully.")
    except Exception as e:
        print(f" Error: {e}")


def update_item():
    item_id = input("Enter item ID to update: ").strip()
    if not item_id.isdigit():
        print(" Invalid ID.")
        return

    item = ClothingItem.find_by_id(int(item_id))
    if not item:
        print(" Item not found.")
        return

    print("Leave blank to keep current value.")
    name = input(f"New name ({item.name}): ").strip() or item.name
    size = input(f"New size ({item.size}): ").strip() or item.size
    color = input(f"New color ({item.color}): ").strip() or item.color
    price_input = input(f"New price ({item.price}): ").strip()
    price = float(price_input) if price_input else item.price
    store_id_input = input(f"New store ID ({item.store_id}): ").strip()
    store_id = int(store_id_input) if store_id_input else item.store_id

    updated = ClothingItem.update(item.id, name, size, color, price, store_id)
    print(f" Item '{updated.name}' updated successfully.")


def delete_item():
    item_id = input("Enter item ID to delete: ").strip()
    if item_id.isdigit() and ClothingItem.delete(int(item_id)):
        print(" Item deleted.")
    else:
        print(" Item not found.")


def run():
    while True:
        menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            view_stores()
        elif choice == "2":
            add_store()
        elif choice == "3":
            delete_store()
        elif choice == "4":
            view_items()
        elif choice == "5":
            add_item()
        elif choice == "6":
            update_item()
        elif choice == "7":
            delete_item()
        elif choice == "0":
            print("👋 Exiting...")
            session.close()
            break
        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    run()
