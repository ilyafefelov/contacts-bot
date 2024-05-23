from prompt_toolkit import PromptSession

from prompt_toolkit.completion import WordCompleter

from src.commands.contact_commands import (
    add_contact,
    change_phone,
    change_birthday,
    delete_phone,
    show_phone,
    show_all,
    search_phone,
    delete_contact,
    add_birthday,
    show_birthday,
    birthdays,
)

from src.commands.note_commands import add_note, search_notes, delete_note, list_notes, edit_note

from src.utils.data_handler import save_data, load_data

from typing import List, Tuple
import re

from colorama import Fore, Style, init


init()


AUTOSAVE_INTERVAL = 5  # Save after every 5 commands


def parse_input(user_input: str) -> Tuple[str, List[str]]:

    if not user_input.split():

        return "Please enter a command:", []

    cmd, *args = user_input.split()

    return cmd, args


# List of available commands

commands = [
    "hello",
    "add",
    "add-birthday",
    "show-birthday",
    "birthdays",
    "change",
    "delete-phone",
    "change-phone",
    "change-birthday",
    "phone",
    "all",
    "search",
    "delete",
    "add-note",
    "search-notes",
    "delete-note",
    "help",
]


# Creating an object for autocompletion

command_completer = WordCompleter(commands, ignore_case=True)


# Creating a prompt_toolkit session

session = PromptSession(completer=command_completer)


def main():

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
                "search": lambda: search_phone(args, address_book),
                "delete": lambda: delete_contact(args, address_book),
                "add-note": lambda: add_note(args, note_book),
                "edit-note": lambda: edit_note(args, note_book),
                "search-notes": lambda: search_notes(args, note_book),
                "list-notes": lambda: list_notes(note_book),
                "delete-note": lambda: delete_note(args, note_book),
                "help": lambda: """ 

    add [name] [phone] [email] [address] [birthday]: Add a new contact with name and other details.

    change [name] [old phone] [new phone]: Change the phone number for the specified contact.

    phone [name]: Show phone numbers for the specified contact.

    all: Show all contacts in the address book.

    add-birthday [name] [birthday]: Add a birthday for the specified contact.

    show-birthday [name]: Show the birthday for the specified contact.

    birthdays [days]: Show contacts with birthdays in the next specified number of days.

    search [name]: Find a contact.

    delete [name]: Delete a contact.

    add-note --title [title] --text [text]: Add a new note.

    list-notes: List all notes.

    search-notes [text]: Find notes by text.

    edit-note --id [ID] --title [title] --text [text]: Edit a note by its ID.

    delete-note [ID]: Delete a note by its ID.

    hello: Get a greeting from the bot.

    close or exit: Close the program.
                    """,
            }

            result = switcher.get(
                command,
                lambda: "Invalid command. Available commands: hello, add, add-birthday, show-birthday, birthdays, change, phone, all, search, delete, add-note, edit-note, search-notes, delete-note, close, exit & help",
            )

            return result() if callable(result) else result

        print(switch_commands(command))

        command_count += 1

        if command_count >= AUTOSAVE_INTERVAL:

            save_data((address_book, note_book))

            print("Autosaved address book and notebook.")

            command_count = 0


if __name__ == "__main__":

    main()
