contacts = []

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email
                })
    except FileNotFoundError:
        pass

def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact():
    view_contacts()
    choice = int(input("Enter contact number to edit: ")) - 1

    if 0 <= choice < len(contacts):
        contacts[choice]["name"] = input("Enter new name: ")
        contacts[choice]["phone"] = input("Enter new phone: ")
        contacts[choice]["email"] = input("Enter new email: ")
        save_contacts()
        print("Contact updated successfully!")
    else:
        print("Invalid selection.")

def delete_contact():
    view_contacts()
    choice = int(input("Enter contact number to delete: ")) - 1

    if 0 <= choice < len(contacts):
        contacts.pop(choice)
        save_contacts()
        print("Contact deleted successfully!")
    else:
        print("Invalid selection.")

load_contacts()

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        edit_contact()
    elif option == "4":
        delete_contact()
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
