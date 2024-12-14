def contact_book():
    contacts = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact  2. View Contacts  3. Search Contact  4. Delete Contact  5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print(f"Contact '{name}' added.")
        elif choice == '2':
            print("\nAll Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == '3':
            search = input("Enter name to search: ")
            if search in contacts:
                print(f"{search}: {contacts[search]}")
            else:
                print(f"No contact found with the name '{search}'.")
        elif choice == '4':
            delete = input("Enter name to delete: ")
            if delete in contacts:
                del contacts[delete]
                print(f"Contact '{delete}' deleted.")
            else:
                print(f"No contact found with the name '{delete}'.")
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

contact_book()
