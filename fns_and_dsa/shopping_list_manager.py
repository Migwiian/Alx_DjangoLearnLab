def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            if not shopping_list:
                print("Your list is empty. Nothing to remove.")
                continue
            
            item_to_remove = input("Enter the item to remove: ").strip()
            
            try:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                print(f"'{item_to_remove}' not found in the list.")

        elif choice == '3':
            print("\n--- Current Shopping List ---")
            if not shopping_list:
                print("Your list is empty.")
            else:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("----------------------------")

        elif choice == '4':
            print("Goodbye! Your shopping list is ready.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()