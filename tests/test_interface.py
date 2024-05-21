# Tests for CLI interface
import unittest

class TestInterface(unittest.TestCase):
    def test_parse_input(self):
        from src.cli.interface import parse_input
        self.assertEqual(parse_input("add John 1234567890"), ("add", ["John", "1234567890"]))

if __name__ == '__main__':
    unittest.main()
