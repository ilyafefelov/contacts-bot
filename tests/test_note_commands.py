# Tests for note commands
import unittest

class TestNoteCommands(unittest.TestCase):
    def test_add_note(self):
        from src.models.note_book import NoteBook
        from src.commands.note_commands import add_note
        notebook = NoteBook()
        result = add_note(["--title", "some title", "--text", "text"], notebook)
        self.assertRegex(result, r"Note added")

if __name__ == '__main__':
    unittest.main()
