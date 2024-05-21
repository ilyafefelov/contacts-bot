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

@input_error
def change_contact(args, book):
    if len(args) != 3:
        raise ValueError("Please provide the contact name, old phone number, and new phone number.")
    name, old_phone, new_phone = args
    record: Record = book.find(name)
    return record.edit_phone(old_phone, new_phone)

@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name.")
    name = args[0]
    record = book.find(name)
    return f"{name}'s numbers are: {', '.join(phone.value for phone in record.phones)}"

@input_error
def show_all(book):
    if book.data:
        return "\n".join(str(record) for record in book.data.values())
    else:
        return "No contacts saved."

@input_error
def search_phone(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name for the search.")
    name = args[0]
    record = book.find(name)
    if record.phones:
        return f"{name}'s numbers are: {', '.join(phone.value for phone in record.phones)}"
    else:
        return f"No phone numbers found for {name}."

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
        return "Upcoming birthdays: " + ", ".join(birthdays)
    else:
        return "No upcoming birthdays."
