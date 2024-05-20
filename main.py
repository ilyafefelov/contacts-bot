# from models import AddressBook, NoteBook, Record, Note
from utils import save_data, load_data
from typing import List, Tuple
# import re
# from colorama import Fore, Style, init

# init()

AUTOSAVE_INTERVAL = 5  # Save after every 5 commands


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Parses the user input and returns the command and arguments.

    Args:
        user_input (str): The user input to be parsed.

    Returns:
        tuple[str, list]: A tuple containing the command (str) and arguments (list).
    """
    if not user_input.split():
        return "Please enter a command:", []
    cmd, *args = user_input.split()
    return cmd, args


def input_error(func):
    """
    A decorator that handles common input errors and returns appropriate error messages.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function.

    Raises:
        KeyError: If a contact is not found.
        ValueError: If an invalid command usage is detected.
        IndexError: If insufficient arguments are provided for a command.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return "Contact or Note not found." + str(e)
        except ValueError as e:
            return "Invalid command usage." + str(e)
        except IndexError as e:
            return (
                "Invalid command usage. Insufficient arguments provided. Please provide all required information."
                + str(e)
            )

    return inner



def main():
    """
    The main function of the assistant bot program.

    This function initializes an empty dictionary to store contacts and then enters a loop to prompt the user for commands.
    The user can enter commands such as "hello", "add", "change", "phone", "all", "close", or "exit" to interact with the assistant bot.
    The function calls different helper functions based on the user's command and displays the corresponding output.
    The loop continues until the user enters "close" or "exit" to exit the program.
    """
    address_book, note_book = (
        load_data()
    )  # Load the address book and notebook data from a file
    command_count = 0  # Initialize command count for autosave

    print("Welcome. I am an assistant bot!")

    # Main loop to interact with the user
    while True:
        user_input = input("Enter a command: ").strip()  # Prompt the user for input

        if not user_input:  # Check if the user entered an empty string
            print("Please enter a command.")
            continue
        if user_input.lower() in ["close", "exit"]:  # Check if the user wants to exit
            print("Good bye!")
            save_data((address_book, note_book))
            break

        command, args = parse_input(user_input)

        # Helper functions to handle different commands
        def switch_commands(command):
            switcher = {
                "hello": "How can I help you?",
                "add": lambda: add_contact(args, address_book),
                "add-birthday": lambda: add_birthday(args, address_book),
                "show-birthday": lambda: show_birthday(args, address_book),
                "birthdays": lambda: birthdays(args, address_book),
                "change": lambda: change_contact(args, address_book),
                "phone": lambda: show_phone(args, address_book),
                "all": lambda: show_all(address_book),
                "search": lambda: search_phone(args, address_book),
                "delete": lambda: delete_contact(args, address_book),
                "add-note": lambda: add_note(args, note_book),
                "search-notes": lambda: search_notes(args, note_book),
                "delete-note": lambda: delete_note(args, note_book),
                "help": """ 
    add [ім'я] [**телефон] [email] [адреса] [день народження]: Додати новий контакт з іменем та іншими деталями.
    change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.
    phone [ім'я]: Показати телефонні номери для вказаного контакту.
    all: Показати всі контакти в адресній книзі.
    add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
    show-birthday [ім'я]: Показати дату народження для вказаного контакту.
    birthdays [дні]: Показати контакти, у яких день народження через задану кількість днів.
    search [ім'я]: Знайти контакт.
    delete [ім'я]: Видалити контакт.
    add-note [текст]: Додати нову нотатку.
    search-notes [текст]: Знайти нотатку за текстом.
    delete-note [ID]: Видалити нотатку за її ID.
    hello: Отримати вітання від бота.
    close або exit: Закрити програму.
                    """,
            }
            result = switcher.get(
                command,
                "Invalid command. Available commands: hello, add, add-birthday, show-birthday, birthdays, change, phone, all, search, delete, add-note, search-notes, delete-note, close, exit & help",
            )
            return result() if callable(result) else result

        print(switch_commands(command))

        # Increment command count and check if autosave is needed
        command_count += 1
        if command_count >= AUTOSAVE_INTERVAL:
            save_data((address_book, note_book))
            print("Autosaved address book and notebook.")
            command_count = 0


if __name__ == "__main__":
    main()
