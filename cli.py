# cli.py
import sys
from tabulate import tabulate
from colorama import Fore, Style, init
from lib.db.models import Store, ClothingItem, session

init(autoreset=True)  


def main_menu():
    while True:
        print(Fore.CYAN + "\n=== MAIN MENU ===")
        table = [
            [1, "Stores"],
            [2, "Clothing Items"],
            [3, "Exit"],
        ]
        print(tabulate(table, headers=[Fore.YELLOW + "Option", Fore.YELLOW + "Description"], tablefmt="fancy_grid"))

        choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)

        if choice == "1":
            stores_menu()
        elif choice == "2":
            clothing_items_menu()
        elif choice == "3":
            print(Fore.MAGENTA + "Exiting CLI. Goodbye!\n")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option, try again.")



def stores_menu():
    while True:
        print(Fore.CYAN + "\n=== STORES MENU ===")
        table = [
            [1, "List Stores"],
            [2, "Add Store"],
            [3, "Delete Store"],
            [4, "Update Store"],
            [5, "View Store Items"],
            [6, "Back to Main Menu"],
        ]
        print(tabulate(table, headers=[Fore.YELLOW + "Option", Fore.YELLOW + "Description"], tablefmt="fancy_grid"))

        choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)

    if choice == "1":
        stores = Store.get_all()
        display_stores(stores)
    elif choice == "2":
        name = input("Enter store name: ")
        location = input("Enter store location: ")
        try:
            store = Store.create(name, location)
            print(Fore.BLUE + f"Store '{store.name}' created successfully!")
        except Exception as e:
            print(Fore.RED + str(e))
    elif choice == "3":  
        stores = Store.get_all()
        if not stores:
            print(Fore.RED + "No stores found.")
            return

        print(Fore.YELLOW + "\nAvailable stores:")
        for store in stores:
            print(f"ID: {store.id} | Name: {store.name}")

        while True:
            try:
                store_id = int(input("Enter store ID to delete: "))
                if not any(store.id == store_id for store in stores):
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "Invalid store ID. Enter a number from the list above.")
        
        if Store.delete(store_id):
            print(Fore.GREEN + "Store deleted successfully.")
        else:
            print(Fore.RED + "Failed to delete store.")

    elif choice == "4":
        store_id = int(input("Enter store ID to update: "))
        name = input("Enter new name (leave blank to skip): ")
        location = input("Enter new location (leave blank to skip): ")
        updated = Store.update(store_id, name=name or None, location=location or None)
        if updated:
            print(Fore.BLUE + "Store updated successfully!")
        else:
            print(Fore.RED + "Store not found.")
    elif choice == "5":
        store_id = int(input("Enter store ID to view items: "))
        store = Store.find_by_id(store_id)
        if store:
            display_items(store.items)
        else:
            print(Fore.RED + "Store not found.")
    elif choice == "6":
        return
    else:
        print(Fore.RED + "Invalid option, try again.")



def clothing_items_menu():
    while True:
        print(Fore.CYAN + "\n=== CLOTHING ITEMS MENU ===")
        table = [
            [1, "List Clothing Items"],
            [2, "Add Clothing Item"],
            [3, "Delete Clothing Item"],
            [4, "Update Clothing Item"],
            [5, "Back to Main Menu"],
        ]
        print(tabulate(table, headers=[Fore.YELLOW + "Option", Fore.YELLOW + "Description"], tablefmt="fancy_grid"))

        choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)

    if choice == "1":
        items = ClothingItem.get_all()
        display_items(items)
    elif choice == "2":  # Add Clothing Item
        print(Fore.BLUE + "\n👉 Add a new clothing item...")
        
        # List stores for reference
        stores = Store.get_all()
        if not stores:
            print(Fore.RED + "No stores found. Please add a store first.")
            return
        
        print(Fore.YELLOW + "\nAvailable stores:")
        for store in stores:
            print(f"ID: {store.id} | Name: {store.name}")
        
        name = input("Enter item name: ")
        size = input("Enter item size: ")
        color = input("Enter item color: ")
        
        # Validate price input
        while True:
            try:
                price = float(input("Enter item price: "))
                if price < 0:
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "Invalid price. Enter a positive number.")
        
        # Validate store_id input
        while True:
            try:
                store_id = int(input("Enter store ID: "))
                if not any(store.id == store_id for store in stores):
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "Invalid store ID. Enter a number from the list above.")
        
        item = ClothingItem.create(name=name, size=size, color=color, price=price, store_id=store_id)
        print(Fore.GREEN + f"Clothing item '{item.name}' added successfully!")
    elif choice == "3":
        item_id = input("Enter item ID to delete: ")
        if ClothingItem.delete(int(item_id)):
            print(Fore.BLUE + "Item deleted successfully!")
        else:
            print(Fore.RED + "Item not found.")
    elif choice == "4":
        item_id = int(input("Enter item ID to update: "))
        name = input("Enter new name (leave blank to skip): ")
        size = input("Enter new size (leave blank to skip): ")
        color = input("Enter new color (leave blank to skip): ")
        price_input = input("Enter new price (leave blank to skip): ")
        price = float(price_input) if price_input else None
        store_id_input = input("Enter new store ID (leave blank to skip): ")
        store_id =  int(store_id_input) if store_id_input else None
        updated = ClothingItem.update(item_id, name=name or None, size=size or None, color=color or None, price=price, store_id=store_id)
        if updated:
            print(Fore.BLUE + "Item updated successfully!")
        else:
            print(Fore.RED + "Item not found.")
    elif choice == "5":
        return
    else:
        print(Fore.RED + "Invalid option, try again.")



def display_stores(stores):
    if not stores:
        print(Fore.YELLOW + "No stores found.")
        return
    table = [[s.id, s.name, s.location] for s in stores]
    print(tabulate(table, headers=["ID", "Name", "Location"], tablefmt="fancy_grid"))


def display_items(items):
    if not items:
        print(Fore.YELLOW + "No items found.")
        return
    table = [[i.id, i.name, i.size, i.color, i.price, i.store_id] for i in items]
    print(tabulate(table, headers=["ID", "Name", "Size", "Color", "Price", "Store ID"], tablefmt="fancy_grid"))



if __name__ == "__main__":
    main_menu()
