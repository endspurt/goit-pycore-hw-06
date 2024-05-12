from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Inherits Field, used to store a contact's name
    pass

class Phone(Field):
    # Inherits Field, used to store phone numbers, includes validation
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)  # Name object storing the contact's name
        self.phones = []  # List to store Phone objects

    def add_phone(self, phone):
        self.phones.append(Phone(phone))  # Adds a new phone number after validation

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]  # Remove phone number by value

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone  # Update phone value if it matches old_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p  # Returns the phone if found
        return None

    def __str__(self):
        # Returns a formatted string representation of the contact
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # Inherits UserDict to manage a collection of Record objects
    def add_record(self, record):
        self.data[record.name.value] = record  # Adds a record to the dictionary using the name as a key

    def find(self, name):
        return self.data.get(name)  # Finds a record by name

    def delete(self, name):
        if name in self.data:
            del self.data[name]  # Deletes a record by name

def test_address_book():
    # Create a new instance of AddressBook
    book = AddressBook()

    # Create entries for John and add phone numbers
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John's record to the address book
    book.add_record(john_record)

    # Create and add an entry for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print all entries in the book to show initial state
    print("Initial state of the address book:")
    for name, record in book.data.items():
        print(record)

    # Find John and edit one of his phones
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")

    print("\nAfter editing John's phone:")
    print(john)

    # Search for a specific phone in John's entry
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"\nFound phone for John: {found_phone}")

    # Delete Jane's entry from the address book
    book.delete("Jane")

    print("\nAddress book after deleting Jane:")
    for name, record in book.data.items():
        print(record)

# Run the test
test_address_book()
