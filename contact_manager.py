contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\nContact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()


def search_contact():
    keyword = input("Enter name or phone to search: ")

    found = False
    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword in c["phone"]:
            print("\nContact Found:")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            print()
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for c in contacts:
        if c["phone"] == phone:
            print("Enter new details (leave blank to keep same):")
            name = input("New name: ")
            email = input("New email: ")
            address = input("New address: ")

            if name:
                c["name"] = name
            if email:
                c["email"] = email
            if address:
                c["address"] = address

            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    phone = input("Enter phone number of contact to delete: ")

    for c in contacts:
        if c["phone"] == phone:
            contacts.remove(c)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


while True:
    print("📒 Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
