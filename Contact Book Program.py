# Contact Book Program

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update_contact(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found with '{keyword}'.")

    def update_contact(self, search_name, new_name=None, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                contact.update_contact(new_name, new_phone, new_email, new_address)
                print(f"Contact '{search_name}' updated successfully.")
                return
        print(f"Contact '{search_name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

# User Interface
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            search_name = input("Enter the name of the contact you want to update: ")
            new_name = input("Enter new name (leave blank to skip): ")
            new_phone = input("Enter new phone (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            new_address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(search_name, new_name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact you want to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
