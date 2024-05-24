from src.models.address_book import AddressBook
from src.models.record import Record
from src.utils.input_error import input_error
from colorama import Fore, Style
import re

@input_error
def add_contact(args, book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Please provide a name.")
    name = args[0]
    address = None
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
        else:
            address = arg
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
            print(f"Error adding phone {phone}: {e}")
    if email:
        record.add_email(email)
    if address:
        record.add_address(address)
    if birthday:
        record.add_birthday(birthday)
    return f"{message} {name}"


# PHONE COMMANDS
@input_error
def change_phone(args, book):
    if len(args) != 3:
        raise ValueError(
            "Please provide the contact name, old phone number, and new phone number."
        )
    name, old_phone, new_phone = args
    record: Record = book.find(name)
    return record.change_phone(old_phone, new_phone)


@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name.")
    name = args[0]
    record = book.find(name)
    return f"{name}'s numbers are: {', '.join(phone.value for phone in record.phones)}"


@input_error
def delete_phone(args, book):
    if len(args) != 2:
        raise ValueError(
            "Please provide the contact name and the phone number to delete."
        )
    name, phone = args
    record = book.find(name)
    record.delete_phone(phone)
    return f"Phone {phone} deleted from {name}."


@input_error
def search_phone(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name for the search.")
    name = args[0]
    record = book.find(name)
    if record.phones:
        return (
            f"{name}'s numbers are: {', '.join(phone.value for phone in record.phones)}"
        )
    else:
        return f"No phone numbers found for {name}."


# EMAIL COMMANDS
@input_error
def add_email(args, book: AddressBook) -> str:
    """ add email for requested name in contacts"""
    name, email, *_ = args
    record: Record = book.find(name)
    record.add_email(email)
    return "Email added"


@input_error
def show_email(args, book: AddressBook) -> str:
    name, *_ = args
    record: Record = book.find(name)
    email = record.show_email()
    return f"{name}'s email: {email}"


@input_error
def change_email(args, book: AddressBook) -> str:
    name, new_email, *_ = args
    record: Record = book.find(name)
    record.change_email(new_email)
    return "Email updated"


@input_error
def delete_email(args, book) -> str:
    name, *_ = args
    record: Record = book.find(name)
    record.delete_email()
    return "Email deleted"


@input_error
def show_all(book):
    if book.data:
        return "\n".join(str(record) for record in book.data.values())
    else:
        return "No contacts saved."


@input_error
def delete_contact(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name to delete.")
    name = args[0]
    result = book.delete(name)
    return f"Contact {name} deleted successfully."


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError("Please provide the contact name and the birthday in format DD.MM.YYYY.")
    name, birthday = args
    record: Record = book.find(name)
    return record.add_birthday(birthday)


@input_error
def change_birthday(args, book):
    if len(args) != 2:
        raise ValueError(
            "Please provide the contact name and the new birthday in format DD.MM.YYYY."
        )
    name, new_birthday = args
    record: Record = book.find(name)
    record.change_birthday(new_birthday)
    return "Birthday updated"


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name.")
    name = args[0]
    record = book.find(name)
    if record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}."
    else:
        return f"No birthday found for {name}."


@input_error
def birthdays(args, book):
    if len(args) != 1:
        raise ValueError("Please provide the number of days to look ahead for birthdays.")
    days = int(args[0])
    birthdays = book.get_upcoming_birthdays(days)
    if birthdays:
        birthdays_str = ", ".join(
            f"{name}'s birthday is on {date}" for name, date in birthdays
        )
        return "Upcoming birthdays: " + birthdays_str
    else:
        return "No upcoming birthdays."


@input_error
def add_address(args, book: AddressBook) -> str:
    """add address for requested name in contacts"""
    if len(args) < 2:
        raise ValueError(" Please provide both a name and an address.")
    name, address, *_ = args
    print(f"address: {address}")
    try:
        record: Record = book.find(name)
    except KeyError:
        return f"Record for {name} not found."
    if address:
        record.add_address(address)
        return "Address added"
    else:
        raise ValueError(" No address found in the input string.")


@input_error
def change_address(args, book: AddressBook) -> str:
    name, new_address, *_ = args
    record: Record = book.find(name)
    record.change_address(new_address)
    return "Address updated"

@input_error
def show_address(args, book: AddressBook) -> str:
    name, *_ = args
    record: Record = book.find(name)
    address = record.show_address()
    return f"{name}'s address: {address}"

@input_error
def delete_address(args, book: AddressBook) -> str:
    name, *_ = args
    record: Record = book.find(name)
    record.delete_address()
    return "Address deleted"
