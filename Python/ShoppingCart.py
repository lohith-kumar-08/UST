
items = {
    'Bread': 40,
    'Cookies': 80,
    'Butter': 120,
    'Cheese': 180,
    'Yoghurt': 60
}


cart = []


def display_items():
    print("Available Items:")
    for item, price in items.items():
        print(f"Name: {item}, Price: {price}")


def add_to_cart():
    item_name = input("Enter the item name: ")
    if item_name in items:
        quantity = int(input("Enter the quantity: "))
        cart.append([item_name, quantity, items[item_name], items[item_name] * quantity])
    else:
        print("Item not found.")


def update_cart():
    item_name = input("Which item to be updated: ")
    for entry in cart:
        if entry[0] == item_name:
            quantity = int(input("Enter the quantity to be updated: "))
            entry[1] = quantity
            entry[3] = entry[2] * quantity
            break
    else:
        print("Item not found in cart.")


def delete_from_cart():
    item_name = input("Which item to be removed: ")
    for entry in cart:
        if entry[0] == item_name:
            cart.remove(entry)
            break
    else:
        print("Item not found in cart.")


def print_bill():
    total_amount = 0
    print("\nCart Items:")
    for entry in cart:
        print(entry)
        total_amount += entry[3]
    print(f"\nTotal Amount of Bill: {total_amount}")


def main():
    while True:
        print("\nWhat do you want to do?")
        print("Enter 1 for viewing the items")
        print("Enter 2 for adding the items in cart")
        print("Enter 3 for updating the items in cart")
        print("Enter 4 for deleting the items in cart")
        print("Enter 5 for printing bill")
        print("Enter 6 to exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display_items()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            update_cart()
        elif choice == 4:
            delete_from_cart()
        elif choice == 5:
            print_bill()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
