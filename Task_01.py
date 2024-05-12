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

'''Unser Assistent kann bereits über die Befehlszeile mit dem Benutzer interagieren, 
indem er Befehle und Argumente empfängt und die erforderlichen Aktionen ausführt. In dieser 
Aufgabe müssen wir an der internen Logik des Assistenten arbeiten, wie Daten gespeichert werden, 
welche Daten es gibt und was damit gemacht werden kann.

Die Logik werden wir im nächsten Hausaufgabenprojekt zum Bot hinzufügen.

Für diese Zwecke wenden wir objektorientierte Programmierung an. Zunächst definieren wir 
einige Entitäten (Modelle), mit denen wir arbeiten werden.

Ein Benutzer wird ein Adressbuch oder ein Kontaktbuch haben. Dieses Kontaktbuch enthält Einträge. 
Jeder Eintrag enthält eine Reihe von Feldern.
So haben wir die Entitäten (Klassen) beschrieben, die implementiert werden müssen. 
Als nächstes betrachten wir die Anforderungen an diese Klassen und definieren ihre Beziehungen und die Regeln, 
nach denen sie interagieren werden.

Der Benutzer interagiert mit dem Kontaktbuch, indem er Einträge hinzufügt, löscht und bearbeitet. 
Der Benutzer sollte auch in der Lage sein, im Kontaktbuch nach Einträgen anhand eines oder mehrerer Kriterien 
(Felder) zu suchen. Felder können obligatorisch (Name) und optional (Telefon oder E-Mail zum Beispiel) sein. 
Einträge können auch mehrere Felder desselben Typs enthalten (zum Beispiel mehrere Telefone). 
Der Benutzer sollte in der Lage sein, Felder in einem Eintrag hinzuzufügen, zu löschen oder zu bearbeiten.
Technische Beschreibung der Aufgabe:

Entwickeln Sie ein System zur Verwaltung eines Adressbuchs.
Entitäten:

Field: Basisklasse für Eintragsfelder.
Name: Klasse zur Speicherung des Namens eines Kontakts. Pflichtfeld.
Phone: Klasse zur Speicherung der Telefonnummer. Muss Formatvalidierung haben (10 Ziffern).
Record: Klasse zur Speicherung von Kontaktinformationen, einschließlich Name und Liste von Telefonen.
AddressBook: Klasse zur Speicherung und Verwaltung von Einträgen.
Funktionalität:

AddressBook: Hinzufügen von Einträgen, Suchen von Einträgen nach Namen, Löschen von Einträgen nach Namen.
Record: Hinzufügen von Telefonen, Löschen von Telefonen, Bearbeiten von Telefonen, Suchen von Telefonen.
Empfehlungen für die Ausführung:

Als Ausgangspunkt können Sie den folgenden Basiscode zur Implementierung dieser Hausaufgabe verwenden:
Erklärung des Codes
Field Klasse: Grundklasse für Felder, speichert einfach einen Wert und gibt ihn formatiert zurück.
Name Klasse: Erbt von Field, speichert den Namen eines Kontakts. Keine spezielle Funktionalität 
über das Speichern und Umwandeln in String hinaus.
Phone Klasse: Ebenfalls eine Erweiterung von Field, fügt eine Validierung hinzu, um sicherzustellen, 
dass das Telefon zehn Ziffern lang ist. Bei Nichterfüllung wird ein ValueError ausgelöst.
Record Klasse: Verwaltet Kontaktinformationen, einschließlich eines Namens und einer Liste von Telefonen. 
Bietet Methoden zum Hinzufügen, Entfernen und Bearbeiten von Telefonnummern sowie zum Suchen einer bestimmten Nummer.
AddressBook Klasse: Erbt von UserDict zur Verwaltung einer Sammlung von Record-Objekten. Ermöglicht das Hinzufügen, 
Finden und Löschen von Kontakten basierend auf dem Namen.GPT
Die Fehlermeldung, die Sie erhalten haben, deutet darauf hin, dass es ein Problem mit dem Kontext gibt, in dem die List Comprehension innerhalb der __str__ Methode Ihrer Record Klasse verwendet wird. Speziell zeigt die Fehlermeldung, dass phones nicht definiert ist, was darauf hindeutet, dass self.phones korrekt referenziert werden muss.

Ich werde die korrekte Implementierung der Record Klasse zeigen, einschließlich der Methoden zum Hinzufügen, Entfernen und Bearbeiten von Telefonnummern sowie zum Suchen nach einem spezifischen Telefon, basierend auf der Aufgabenstellung. Ich werde auch die Implementierung der Phone Klasse mit der Telefonnummernvalidierung ergänzen.

Hier ist der korrigierte Python-Code mit detaillierten Kommentaren auf Englisch und einer anschließenden schrittweisen Erklärung auf Deutsch:

python
Copy code
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
Erklärung des Codes
Field Klasse: Grundklasse für Felder, speichert einfach einen Wert und gibt ihn formatiert zurück.
Name Klasse: Erbt von Field, speichert den Namen eines Kontakts. Keine spezielle Funktionalität 
über das Speichern und Umwandeln in String hinaus.
Phone Klasse: Ebenfalls eine Erweiterung von Field, fügt eine Validierung hinzu, um sicherzustellen, 
dass das Telefon zehn Ziffern lang ist. Bei Nichterfüllung wird ein ValueError ausgelöst.
Record Klasse: Verwaltet Kontaktinformationen, einschließlich eines Namens und einer Liste von Telefonen. 
Bietet Methoden zum Hinzufügen, Entfernen und Bearbeiten von Telefonnummern sowie zum Suchen einer bestimmten Nummer.
AddressBook Klasse: Erbt von UserDict zur Verwaltung einer Sammlung von Record-Objekten. Ermöglicht das Hinzufügen, 
Finden und Löschen von Kontakten basierend auf dem Namen.
Diese Klassenstruktur und die Methoden bieten eine solide Basis für die in der Aufgabe beschriebene Funktionalität 
zur Verwaltung eines Adressbuchs. Durch die Nutzung von Vererbung und List Comprehensions wird der Code sauber und leicht verständlich

Um die Funktionalität des oben genannten Codes zu prüfen, können Sie verschiedene Tests durchführen, die die wichtigsten Merkmale 
und Methoden Ihrer Klassen verifizieren. Hier sind einige grundlegende Testfälle, die Sie in Ihrer Python-Umgebung ausführen können, 
um sicherzustellen, dass alles wie erwartet funktioniert:

Erstellen von Kontakten und Hinzufügen von Telefonnummern
Suchen nach Kontakten im Adressbuch
Bearbeiten und Löschen von Telefonnummern
Hinzufügen und Löschen von Kontakteinträgen im Adressbuch
Initialisierung und Einträge Hinzufügen: Das Skript beginnt mit dem Erstellen eines AddressBook und dem Hinzufügen 
von zwei Record-Objekten für John und Jane. Jeder Eintrag erhält einige Telefonnummern.

Ausgabe des Initialzustands: Das gesamte Adressbuch wird ausgegeben, um zu zeigen, welche Einträge es anfangs enthält.

Bearbeitung eines Telefons: Johns Telefonnummer wird von "1234567890" auf "1112223333" geändert und das Ergebnis wird ausgegeben.

Suche nach einem Telefon: Es wird versucht, eine spezifische Telefonnummer in Johns Eintrag zu finden und auszugeben.

Löschen eines Eintrags: Der Eintrag für Jane wird aus dem Adressbuch gelöscht und der finale Zustand des Adressbuchs wird gezeigt, 
um zu bestätigen, dass der Eintrag entfernt wurde.

Durch Ausführen dieses Test-Skripts können Sie die korrekte Funktionsweise Ihrer Klassen und Methoden verifizieren. Es hilft dabei, 
sicherzustellen, dass Ihre Implementierung wie erwartet funktioniert und alle Grundfunktionalitäten abdeckt. 
Sie können weitere Tests hinzufügen oder anpassen, um spezifischere Fälle oder Ausnahmen zu prüfen.
'''