import argparse
from colorama import Fore, Style


def parse_book_command(args, command: str, data_keys: list = []):
    """
    Parses the command arguments for adding a contact to the address book.

    Args:
        args (list): The command arguments.
        command (str): The name of the command.
        data_keys (list): A list of dictionaries containing information about the data keys.

    Returns:
        tuple: A tuple containing the contact name and a dictionary of contact data.

    Raises:
        ValueError: If the input is invalid and does not provide the name and expected arguments.
    """

    combined_args_text = " ".join(
        [f"--{key['key_name']} {key['key_name']}" for key in data_keys]
    )

    parser = argparse.ArgumentParser(
        description=f"{command} --name <name> {combined_args_text}"
    )

    parser.add_argument("--name", required=True, help="Name of the contact", nargs="+")

    for key in data_keys:
        parser.add_argument(
            f"--{key['key_name']}", required=True, help=key["help"], nargs="+"
        )

    try:
        parsed = parser.parse_args(args)
        contact_name = " ".join(parsed.name) if parsed.name else None

        # check if data_keys list is not empty and is iterable
        if not data_keys or not isinstance(data_keys, list):
            return contact_name, {}

        data = {
            key["key_name"]: (
                " ".join(
                    getattr(parsed, key["key_name"])
                )  # join the list of values to combine them into a single string
                if getattr(parsed, key["key_name"])  # check if the key is not None
                else None
            )
            for key in data_keys
        }

        return contact_name, data

    except SystemExit:
        raise ValueError(
            f"{Fore.YELLOW} Invalid input. Please provide the name and expected arguments.{Style.RESET_ALL}"
        )
