# Design Pattern: Singleton Pattern : Printer Class
# Create a Printer class using the Singleton Pattern.
# Multiple users should access the same printer object to print documents.
# Verify that only one object exists.

class Printer:
    _instance = None

    def __new__(cls):
        # Create a new instance only if one doesn't already exist
        if cls._instance is None:
            cls._instance = super(Printer, cls).__new__(cls)
        return cls._instance

    def print_document(self, user, document):
        print(f"[{user}] printing: {document}")

# --- Verification ---
# Multiple users trying to access the printer
user1_printer = Printer()
user2_printer = Printer()

user1_printer.print_document("Alice", "Resume.pdf")
user2_printer.print_document("Bob", "Invoice.docx")

# Verify that both users are using the exact same printer object
print(f"Are both printer objects the same? {user1_printer is user2_printer}")