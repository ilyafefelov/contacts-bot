# Tests for contact commands
import unittest

class TestContactCommands(unittest.TestCase):
    def test_add_contact(self):
        from src.models.address_book import AddressBook
        from src.commands.contact_commands import add_contact
        book = AddressBook()
        result = add_contact(["John", "1234567890"], book)
        self.assertIn("John", book)
        self.assertEqual(result, "Contact added. John")

if __name__ == '__main__':
    unittest.main()
