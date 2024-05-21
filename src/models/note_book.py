from collections import UserDict

class NoteBook(UserDict):
    def add_record(self, note):
        self.data[len(self.data) + 1] = note

    def search(self, text):
        return [note for note in self.data.values() if text in note.text]

    def delete(self, note_id):
        if note_id in self.data:
            del self.data[note_id]
            return f"Note {note_id} deleted."
        raise KeyError(f"Note {note_id} not found.")
