import argparse
from src.models.note_book import NoteBook
from src.models.note import Note
from src.utils.input_error import input_error
from colorama import Fore, Style

@input_error
def add_note(args, notebook: NoteBook) -> str:
    parser = argparse.ArgumentParser(description="Add a new note")
    parser.add_argument('--title', required=True, help='Title of the note', nargs='+')
    parser.add_argument('--text', required=True, help='Text of the note', nargs='+')

    try:
        parsed = parser.parse_args(args)
    except SystemExit:
        return f"{Fore.RED}Invalid input. Please provide the title and text of the note.{Style.RESET_ALL}"

    note_title = " ".join(parsed.title)
    note_text = " ".join(parsed.text)
    note_id = notebook.generate_id()
    note = Note(note_id, note_title, note_text)
    notebook.add_record(note)
    return f"{Fore.GREEN}Note added:{Style.RESET_ALL}[{note_id}] {note_text}"


@input_error
def search_notes(args, notebook: NoteBook):
    if len(args) < 1:
        raise ValueError("Please provide the search text.")
    search_text = " ".join(args)
    results = notebook.search(search_text)
    if results:
        result = f"{Fore.BLUE}Search results for '{search_text}':\n{Style.RESET_ALL}"
        result += "\n".join(results)
        return result
    else:
        return f"{Fore.RED}No notes found.{Style.RESET_ALL}"


@input_error
def list_notes(notebook: NoteBook):
    notes = notebook.get_list()
    if notes:
        result = f"{Fore.BLUE}List of notes:{Style.RESET_ALL}\n"
        result += "\n".join(str(note) for note in notes)
        return result
    else:
        return f"{Fore.RED}No notes found.{Style.RESET_ALL}"


def edit_note(args, notebook: NoteBook):
    parser = argparse.ArgumentParser(description="Edit a note")
    parser.add_argument('--id', required=True, help='ID of the note', type=int)
    parser.add_argument('--title', required=False, help='Title of the note', nargs='+')
    parser.add_argument('--text', required=False, help='Text of the note', nargs='+')

    try:
        parsed = parser.parse_args(args)
    except SystemExit:
        return f"{Fore.RED}Invalid input. Please provide arguments to edit.{Style.RESET_ALL}"

    note_id = parsed.id
    note_title = " ".join(parsed.title) if parsed.title else None
    note_text = " ".join(parsed.text) if parsed.text else None

    if not note_title and not note_text:
        return f"{Fore.RED}Please provide the title or text to edit the note.{Style.RESET_ALL}"

    result = notebook.edit(note_id, note_title, note_text)

    if result:
        return f"{Fore.GREEN}Note {note_id} edited successfully.{Style.RESET_ALL}"
    else:
        return f"{Fore.BLUE}Note {note_id} not found.{Style.RESET_ALL}"


@input_error
def delete_note(args, notebook: NoteBook):
    if len(args) != 1:
        raise ValueError("Please provide the note ID to delete.")
    note_id = int(args[0])
    result = notebook.delete(note_id)
    if result:
        return f"{Fore.GREEN}Note {note_id} deleted successfully.{Style.RESET_ALL}"
    else:
        return f"{Fore.BLUE}Note {note_id} not found.{Style.RESET_ALL}"
