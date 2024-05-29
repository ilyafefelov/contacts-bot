from src.models.address_book import AddressBook
from src.models.record import Record
from src.utils.input_error import input_error
from src.utils.command_parser import parse_book_command
from colorama import Fore, Style
import re
import argparse


@input_error
def add_contact(args, book: AddressBook) -> str:
    """
    Add a new contact to the address book.

    Args:
        args (list): List of arguments passed to the command. The first argument should be the name of the contact.
        book (AddressBook): The address book object to add the contact to.

    Returns:
        str: A message indicating whether the contact was added or updated.

    Raises:
        ValueError: If no name is provided in the arguments.

    """
    if len(args) < 1:
        raise ValueError("Please provide a name.")
    name = args[0]
    if len(args) > 1 and not (
        args[1].isdigit()
        or re.fullmatch(r"[^@]+@[^@]+\.[^@]+", args[1])
        or re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", args[1])
    ):
        name += " " + args[1]
        args = args[1:]
    address = ''
    phones = []
    email = None
    birthday = None
    for arg in args[1:]:
        if arg.isdigit():
            if len(arg) == 10:
                phones.append(arg)
            else:
                print(f"{Fore.RED}Error adding phone {arg}: Phone number must be 10 digits.{Style.RESET_ALL}")
        elif re.fullmatch(r"[^@]+@[^@]+\.[^@]+", arg):
            email = arg
        elif re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", arg):
            birthday = arg
        # else:
        #     address.__add__(arg)
    try:
        record = book.find(name)
        message = "Contact updated."
    except KeyError:
        record = Record(name, address, [], email, birthday)
        book.add_record(record)
        message = "Contact added."
    for phone in phones:
        try:
            print(record.add_phone(phone))
        except ValueError as e:
            print(f"{Fore.RED}Error adding phone {phone}: {e}{Style.RESET_ALL}")
    if email:
        record.add_email(email)
    if address:
        record.add_address(address)
    if birthday:
        record.add_birthday(birthday)
    return f"{Fore.GREEN}{message} {name}{Style.RESET_ALL}"


# PHONE COMMANDS
@input_error
def change_phone(args, book):
    contact_name, data = parse_book_command(
        args,
        "change-phone",
        [
            {
                "key_name": "oldphone",
                "help": "10 digit phone number to delete.",
            },
            {
                "key_name": "newphone",
                "help": "10 digit phone number to add.",
            },
        ],
    )
    
    record: Record = book.find(contact_name)
    return record.change_phone(data['oldphone'], data['newphone'])


@input_error
def show_phone(args, book):
    contact_name, *_ = parse_book_command(
        args,
        "show-phone",
    )
    
    record = book.find(contact_name)
    return f"{contact_name}'s numbers are: {', '.join(phone.value for phone in record.phones)}"


@input_error
def delete_phone(args, book):
    contact_name, data = parse_book_command(
        args,
        "delete-phone",
        [
            {
                "key_name": "phone",
                "help": "10 digit phone number to delete.",
            }
        ],
    )
    
    record = book.find(contact_name)
    record.delete_phone(data['phone'])
    return f"{Fore.YELLOW}Phone {data['phone']} deleted from {contact_name}.{Style.RESET_ALL}"


@input_error
def search_contact(args, book):
    """
    Search for a contact in the address book based on the provided arguments.

    Args:
        args (list): A list of arguments. If the list contains two elements, it is assumed to be the first and last name of the contact.
        If the list contains only one element, it is assumed to be the name of the contact.
        book (AddressBook): An instance of the AddressBook class representing the address book.

    Returns:
        str: A formatted string containing the search results.
        If no contact is found, a message indicating that no contact was found is returned.

    """
    # Check if the user provided a first and last name
    name = (
        args[0] + " " + args[1]
        if len(args) == 2 and all(isinstance(arg, str) for arg in args)
        else args[0]
    )

    # Search for the contact in the address book
    search_results = book.find_all(name)

    # Check if the search results are empty
    if len(search_results) == 0:
        res.append(f"{Fore.RED}No contact found with the name {name}.{Style.RESET_ALL}")
        return "\n".join(res)

    # Format the search results
    res = []
    res.append("=================")
    res.append("= = = = = = = = =")
    res.append("=================")
    res.append(f"{Fore.GREEN}Search results - {len(search_results)}:{Style.RESET_ALL}")
    res.append("=========")

    for record in search_results:
        contact_phones = (
            ", ".join(phone.value for phone in record.phones)
            if record.phones
            else "No phone numbers"
        )

        contact_emails = record.email if record.email else "No emails"
        contact_address = record.address if record.address else "No address"
        contact_birthday = (
            record.birthday.value.strftime("%d.%m.%Y")
            if record.birthday
            else "No birthday"
        )

        contact_details = (
            f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Contact name:{Style.RESET_ALL}{Style.BRIGHT} {record.name}{Style.RESET_ALL}\n"
            f"{Fore.GREEN}Phones:{Style.RESET_ALL} {contact_phones}\n"
            f"{Fore.GREEN}Emails:{Style.RESET_ALL} {contact_emails}\n"
            f"{Fore.GREEN}Birthday:{Style.RESET_ALL} {contact_birthday}\n"
            f"{Fore.GREEN}Address:{Style.RESET_ALL}\n{contact_address}\n"
            f"===+=========+==="
        )
        res.append(contact_details)
    return "\n".join(res)


# EMAIL COMMANDS
@input_error
def add_email(args, book: AddressBook) -> str:
    """ add email for requested name in contacts"""
    contact_name, data = parse_book_command(
        args,
        "add-email",
        [
            {
                "key_name": "email",
                "help": "New email address to add.",
            }
        ],
    )
    record: Record = book.find(contact_name)
    record.add_email(data['email'])
    return f"{Fore.GREEN}Email added{Style.RESET_ALL}"


@input_error
def show_email(args, book: AddressBook) -> str:
    contact_name, *_ = parse_book_command(
        args,
        "show_email",
    )
    record: Record = book.find(contact_name)
    email = record.show_email()
    return f"{contact_name}'s email: {email}"


@input_error
def change_email(args, book: AddressBook) -> str:
    contact_name, data = parse_book_command(
        args,
        "change-email",
        [
            {
                "key_name": "email",
                "help": "New email address",
            }
        ],
    )
    record: Record = book.find(contact_name)
    record.change_email(data["email"])
    return f"{Fore.GREEN}Email updated{Style.RESET_ALL}"


@input_error
def delete_email(args, book) -> str:
    contact_name, *_ = parse_book_command(
        args,
        "delete_email",
    )
    record: Record = book.find(contact_name)
    record.delete_email()
    return f"{Fore.YELLOW}Email deleted{Style.RESET_ALL}"


@input_error
def show_all(book):
    if book.data:
        all_records = f"========There are {len(book.data.values())} contacts=========\n"
        for index, record in enumerate(book.data.values()):
            check_phones = f"{Fore.GREEN}Phones:{Style.RESET_ALL} {', '.join(phone.value for phone in record.phones)}\n" if record.phones else f"{Fore.MAGENTA}No phones{Style.RESET_ALL}\n"
            check_address = f"{Fore.GREEN}Address:{Style.RESET_ALL}\n{record.address}\n" if record.address else f"{Fore.MAGENTA}No address{Style.RESET_ALL}\n"
            check_email = f"{Fore.GREEN}Email:{Style.RESET_ALL}\n{record.email}\n" if record.email else f"{Fore.MAGENTA}No email{Style.RESET_ALL}\n"
            check_birthday = f"{Fore.GREEN}Birthday:{Style.RESET_ALL}\n{record.birthday}\n" if record.birthday else f"{Fore.MAGENTA}No birthday{Style.RESET_ALL}\n"
            all_records += (
                f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{index+1}. Contact name:{Style.RESET_ALL}{Style.BRIGHT} {record.name}{Style.RESET_ALL}\n"
                f"{check_phones}"
                f"{check_email}"
                f"{check_birthday}"
                f"{check_address}"
                f"{Fore.GREEN}-- -- -- -- -- --{Style.RESET_ALL}\n"
            )
            
        return all_records
    else:
        return f"{Fore.RED}No contacts saved.{Style.RESET_ALL}"


@input_error
def delete_contact(args, book):
    contact_name, *_ = parse_book_command(
        args,
        "delete_contact",
    )
    
    result = book.delete(contact_name)
    return f"{Fore.YELLOW}Contact {contact_name} deleted successfully.{Style.RESET_ALL}"


@input_error
def add_birthday(args, book):
    contact_name, data = parse_book_command(
        args,
        "add-birthday",
        [
            {
                "key_name": "date",
                "help": "Birthday in format: DD.MM.YYYY",
            }
        ],
    )
    
    record: Record = book.find(contact_name)
    record.add_birthday(data["date"])
    return f"{Fore.GREEN}Birthday {data["date"]} added to {contact_name}{Style.RESET_ALL}"


@input_error
def change_birthday(args, book):
    contact_name, data = parse_book_command(
        args,
        "change-birthday",
        [
            {
                "key_name": "date",
                "help": "Birthday in format: DD.MM.YYYY",
            }
        ],
    )
    
    record: Record = book.find(contact_name)
    record.change_birthday(data["date"])
    return f"{Fore.GREEN}Birthday updated to {data["date"]}{Style.RESET_ALL}"


@input_error
def show_birthday(args, book):
    contact_name, *_ = parse_book_command(
        args,
        "show_birthday",
    )
    
    record = book.find(contact_name)
    if record.birthday:
        return f"{Fore.MAGENTA}{contact_name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}.{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}No birthday found for {contact_name}.{Style.RESET_ALL}"


@input_error
def birthdays(args, book):
    if len(args) != 1:
        raise ValueError(
            f"{Fore.RED} Please provide the number of days to look ahead for birthdays.{Style.RESET_ALL}"
        )
    days = int(args[0])
    birthdays = book.get_upcoming_birthdays(days)
    if birthdays:
        birthdays_str = ", ".join(
            f"{name}'s birthday is on {date}" for name, date in birthdays
        )
        return f"{Fore.YELLOW}Upcoming birthdays: {birthdays_str}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}No upcoming birthdays.{Style.RESET_ALL}"


@input_error
def add_address(args, book: AddressBook) -> str:
    contact_name, data = parse_book_command(
        args,
        "add-address",
        [
            {
                "key_name": "address",
                "help": "Address in format: standard: street, city, state, postcode",
            }
        ],
    )

    try:
        record: Record = book.find(contact_name)
    except KeyError:
        return f"{Fore.RED}Record for {contact_name} not found.{Style.RESET_ALL}"
    if data["address"]:
        try:
            result = record.add_address(data["address"])
        except Exception:
            return f"{Fore.RED}Please provide address according to standard: street, city, state, postcode{Style.RESET_ALL}"
        else:
            return  f"{Fore.GREEN}{result}{Style.RESET_ALL}"
    else:
        raise ValueError(
            f"{Fore.RED}No address found in the input string.{Style.RESET_ALL}"
        )


@input_error
def change_address(args, book: AddressBook) -> str: 
    contact_name, data = parse_book_command(
        args,
        "change-address",
        [
            {
                "key_name": "address",
                "help": "Address in format: standard: street, city, state, postcode",
            }
        ],
    )
    
    try:
        record: Record = book.find(contact_name)
    except KeyError:
        return f"{Fore.RED}Record for {contact_name} not found.{Style.RESET_ALL}"
    try:
        result = record.change_address(data["address"])
    except Exception:
        return f"{Fore.RED}Please provide address according to standard: street, city, state, postcode{Style.RESET_ALL}"
    else:
        return f"{Fore.GREEN}{result}{Style.RESET_ALL}"

@input_error
def show_address(args, book: AddressBook) -> str:
    contact_name, *_ = parse_book_command(
        args,
        "show_address",
    )
    
    try:
        record: Record = book.find(contact_name)
    except KeyError:
        return f"{Fore.RED}Record for {contact_name} not found.{Style.RESET_ALL}"
    address = record.show_address()
    address_detail = (
            f"{contact_name}'s address:\n"
            f"{address}"
            )
    return address_detail

@input_error
def delete_address(args, book: AddressBook) -> str:
    contact_name, _ = parse_book_command(
        args,
        "delete_address",
    )
    try:
        record: Record = book.find(contact_name)
    except KeyError:
        return f"{Fore.RED}Record for {contact_name} not found.{Style.RESET_ALL}"
    record.delete_address()
    return f"{Fore.YELLOW}Address deleted{Style.RESET_ALL}"
