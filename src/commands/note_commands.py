from src.models.note_book import NoteBook
from src.models.note import Note
from src.utils.input_error import input_error

@input_error
def add_note(args, notebook: NoteBook) -> str:
    if len(args) < 1:
        raise ValueError("Please provide the note text.")
    note_text = " ".join(args)
    note = Note(note_text)
    notebook.add_record(note)
    return f"Note added: {note_text}"

@input_error
def search_notes(args, notebook: NoteBook):
    if len(args) < 1:
        raise ValueError("Please provide the search text.")
    search_text = " ".join(args)
    results = notebook.search(search_text)
    if results:
        return "\n".join(note.text for note in results)
    else:
        return "No notes found."

@input_error
def delete_note(args, notebook: NoteBook):
    if len(args) != 1:
        raise ValueError("Please provide the note ID to delete.")
    note_id = int(args[0])
    result = notebook.delete(note_id)
    return f"Note {note_id} deleted successfully."
