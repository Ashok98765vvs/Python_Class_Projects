inventory: dict[str, int] = {}

def add_item() -> None:
    name = input("Enter item name: ").strip()
    qty = int(input("Enter quantity: "))
    inventory[name] = inventory.get(name, 0) + qty
    print("Item added.\n")

def print_inventory() -> None:
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("Current Inventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")
    print()

def update_item() -> None:
    name = input("Enter item name to update: ").strip()
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty
        print("Item updated.\n")
    else:
        print("Item not found.\n")

def run() -> None:
    while True:
        print("==== Menu ====")
        print("1. Add item")
        print("2. Show inventory")
        print("3. Update item")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            print_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

run()