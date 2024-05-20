# from models import AddressBook, NoteBook, Record, Note
# from utils import save_data, load_data
from typing import List, Tuple
# import re
# from colorama import Fore, Style, init

# init()

# AUTOSAVE_INTERVAL = 5  # Save after every 5 commands


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