from prompt_toolkit import PromptSession
from src.cli.completer import CommandCompleter
from src.commands.contact_commands import (
    add_contact,
    change_phone,
    change_birthday,
    delete_phone,
    show_phone,
    show_all,
    search_contact,
    delete_contact,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    show_email,
    change_email,
    delete_email,
    add_address,
    show_address,
    change_address,
    delete_address,
)
from src.commands.note_commands import add_note, search_notes, delete_note, list_notes, edit_note, get_note_by_id, add_note_tag, delete_note_tag
from src.utils.data_handler import save_data, load_data
from typing import List, Tuple
import re
from colorama import Fore, Style, init


init()

AUTOSAVE_INTERVAL = 1  # Save after every command


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parses the user input and returns the command and arguments.

    Args:
        user_input (str): The user input to be parsed.

    Returns:
        Tuple[str, List[str]]: A tuple containing the command and a list of arguments.
    """

    if not user_input.split():
        return "Please enter a command:", []

    cmd, *args = user_input.split()

    return cmd, args


# Create a PromptSession with custom completer
session = PromptSession(completer=CommandCompleter())


def main():
    """
    The main function of the contact bot program.

    This function loads the address book and notebook data from a file, prompts the user for commands,
    and executes the corresponding actions based on the user's input.

    Available commands:
    - hello: Get a greeting from the bot.
    - add: Add a new contact with name and other details.
    - add-birthday: Add a birthday for the specified contact.
    - show-birthday: Show the birthday for the specified contact.
    - change-birthday: Change the birthday for the specified contact.
    - birthdays: Show contacts with birthdays in the next specified number of days.
    - change-phone: Change the phone number for the specified contact.
    - delete-phone: Delete the phone number for the specified contact.
    - phone: Show phone numbers for the specified contact.
    - all: Show all contacts in the address book.
    - search: Find a contact.
    - delete: Delete a contact.
    - add-note: Add a new note.
    - get-note: Get a note by its ID.
    - edit-note: Edit a note by its ID.
    - add-note-tag: Add a tag to a note.
    - delete-note-tag: Delete a tag from a note.
    - search-notes: Find notes by text.
    - list-notes: List all notes.
    - delete-note: Delete a note by its ID.
    - add-email: Add the email for the specified contact.
    - show-email: Show the email for the specified contact.
    - change-email: Change the email for the specified contact.
    - delete-email: Delete the email for the specified contact.
    - add-address: Add the address for the specified contact.
    - show-address: Show the address for the specified contact.
    - change-address: Change the address for the specified contact.
    - delete-address: Delete the address for the specified contact.
    - help: Show the list of available commands.

    To exit the program, enter 'close' or 'exit'.

    """
    address_book, note_book = load_data()  # Load the address book and notebook data from a file

    command_count = 0  # Initialize command count for autosave

    print("Welcome. I am an assistant bot!")

    while True:
        user_input = session.prompt("Enter a command: ").strip()  # Prompt the user for input

        if not user_input:  # Check if the user entered an empty string
            print("Please enter a command.")
            continue

        if user_input.lower() in ["close", "exit"]:  # Check if the user wants to exit
            print("Good bye!")
            save_data((address_book, note_book))
            break

        command, args = parse_input(user_input)

        def switch_commands(command):
            switcher = {
                "hello": lambda: "How can I help you?",
                "add": lambda: add_contact(args, address_book),
                "add-birthday": lambda: add_birthday(args, address_book),
                "show-birthday": lambda: show_birthday(args, address_book),
                "change-birthday": lambda: change_birthday(args, address_book),
                "birthdays": lambda: birthdays(args, address_book),
                "change-phone": lambda: change_phone(args, address_book),
                "delete-phone": lambda: delete_phone(args, address_book),
                "phone": lambda: show_phone(args, address_book),
                "all": lambda: show_all(address_book),
                "search": lambda: search_contact(args, address_book),
                "delete": lambda: delete_contact(args, address_book),
                "add-note": lambda: add_note(args, note_book),
                "get-note": lambda: get_note_by_id(args, note_book),
                "edit-note": lambda: edit_note(args, note_book),
                "add-note-tag": lambda: add_note_tag(args, note_book),
                "delete-note-tag": lambda: delete_note_tag(args, note_book),
                "search-notes": lambda: search_notes(args, note_book),
                "list-notes": lambda: list_notes(note_book),
                "delete-note": lambda: delete_note(args, note_book),
                "add-email": lambda: add_email(args, address_book),
                "show-email": lambda: show_email(args, address_book),
                "change-email": lambda: change_email(args, address_book),
                "delete-email": lambda: delete_email(args, address_book),
                "add-address": lambda: add_address(args, address_book),
                "show-address": lambda: show_address(args, address_book),
                "change-address": lambda: change_address(args, address_book),
                "delete-address": lambda: delete_address(args, address_book),
                "help": lambda: """
                    add [name] [phone] [email] [address] [birthday]: Add a new contact with name and other details.
                    change [name] [old phone] [new phone]: Change the phone number for the specified contact.
                    phone [name]: Show phone numbers for the specified contact.
                    all: Show all contacts in the address book.
                    add-birthday --[name] --[birthday]: Add a birthday for the specified contact.
                    change-birthday --[name] --[birthday]: Change a birthday for the specified contact.
                    show-birthday [name]: Show the birthday for the specified contact.
                    birthdays [days]: Show contacts with birthdays in the next specified number of days.
                    search [name]: Find a contact.
                    delete [name]: Delete a contact.
                    add-note --title [title] --text [text]: Add a new note.
                    add-email [name] [email]: Add the email for the specified contact.
                    show-email [name]: Show the email for the specified contact.
                    change-email [name] [new email]: Change the email for the specified contact.
                    delete-email [name]: Delete the email for the specified contact.
                    add-address --[name] --[address]: Add the address for the specified contact.
                    show-address [name]: Show the address for the specified contact.
                    change-address [name] [new address]: Change the address for the specified contact.
                    delete-address [name]: Delete the address for the specified contact.
                    list-notes: List all notes.
                    get-note [ID]: Get a note by its ID.
                    add-note-tag --id [ID] --tag [tag]: Add a tag to a note.
                    delete-note-tag --id [ID] --tag [tag]: Delete a tag from a note.
                    search-notes [text]: Find notes by text.
                    edit-note --id [ID] --title [title] --text [text]: Edit a note by its ID.
                    delete-note [ID]: Delete a note by its ID.
                    hello: Get a greeting from the bot.
                    close or exit: Close the program.
                """,
            }

            result = switcher.get(
                command,
                lambda: """Invalid command. Available commands: hello, add, add-birthday, show-birthday, change-birthday, birthdays, 
                change-phone, delete-phone, phone, add-email, show-email, change-email, delete-email, add-address, show-address, 
                change-address, delete-address, all, search, delete, add-note, get-note, edit-note, add-note-tag, delete-note-tag,
                search-notes, list-notes, delete-note, close, exit & help""",
            )

            return result() if callable(result) else result

        print(switch_commands(command))

        command_count += 1

        if command_count >= AUTOSAVE_INTERVAL:
            save_data((address_book, note_book))
            command_count = 0


if __name__ == "__main__":

    main()
