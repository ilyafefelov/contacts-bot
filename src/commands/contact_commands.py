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
    if len(args) != 3:
        raise ValueError(
            f"{Fore.RED} Please provide the contact name, old phone number, and new phone number.{Style.RESET_ALL}"
        )
    name, old_phone, new_phone = args
    record: Record = book.find(name)
    return record.change_phone(old_phone, new_phone)


@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise ValueError(
            f"{Fore.RED} Please provide exactly one contact name.{Style.RESET_ALL}"
        )
    name = args[0]
    record = book.find(name)
    return f"{name}'s numbers are: {', '.join(phone.value for phone in record.phones)}"


@input_error
def delete_phone(args, book):
    if len(args) != 2:
        raise ValueError(
            f"{Fore.RED} Please provide the contact name and the phone number to delete.{Style.RESET_ALL}"
        )
    name, phone = args
    record = book.find(name)
    record.delete_phone(phone)
    return f"{Fore.YELLOW}Phone {phone} deleted from {name}.{Style.RESET_ALL}"


@input_error
def search_contact(args, book):
    if len(args) != 1:
        raise ValueError("Please provide exactly one contact name for the search.")
    name = args[0]
    record = book.find(name)
    if not record:
        return f"{Fore.RED}No contact found with the name {name}.{Style.RESET_ALL}"

    phones = ", ".join(phone.value for phone in record.phones) if record.phones else "No phone numbers"
    emails = record.email if record.email else "No emails"
    addresse = record.address if record.address else "No addresse"
    birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "No birthday"

    contact_detail = (
        f"{Fore.GREEN}Contact name:{Style.RESET_ALL} {name}\n"
        f"{Fore.GREEN}Phones:{Style.RESET_ALL} {phones}\n"
        f"{Fore.GREEN}Emails:{Style.RESET_ALL} {emails}\n"
        f"{Fore.GREEN}Birthday:{Style.RESET_ALL} {birthday}\n"
        f"{Fore.GREEN}Address:{Style.RESET_ALL}\n{addresse}\n"
    )
    return contact_detail

# EMAIL COMMANDS
@input_error
def add_email(args, book: AddressBook) -> str:
    """ add email for requested name in contacts"""
    if len(args) != 2:
        raise ValueError(f"{Fore.RED}Please provide contact name and email.{Style.RESET_ALL}")
    name, email, *_ = args
    record: Record = book.find(name)
    record.add_email(email)
    return f"{Fore.GREEN}Email added{Style.RESET_ALL}"


@input_error
def show_email(args, book: AddressBook) -> str:
    if len(args) != 1:
        raise ValueError(f"{Fore.RED}Please provide the contact name to show_email.{Style.RESET_ALL}")
    name, *_ = args
    record: Record = book.find(name)
    email = record.show_email()
    return f"{name}'s email: {email}"


@input_error
def change_email(args, book: AddressBook) -> str:
    if len(args) != 2:
        raise ValueError(f"{Fore.RED}Please provide contact name and email to add.{Style.RESET_ALL}")
    name, new_email, *_ = args
    record: Record = book.find(name)
    record.change_email(new_email)
    return f"{Fore.GREEN}Email updated{Style.RESET_ALL}"


@input_error
def delete_email(args, book) -> str:
    if len(args) != 1:
        raise ValueError(f"{Fore.RED}Please provide contact name to delete email.{Style.RESET_ALL}")
    name, *_ = args
    record: Record = book.find(name)
    record.delete_email()
    return f"{Fore.YELLOW}Email deleted{Style.RESET_ALL}"


@input_error
def show_all(book):
    if book.data:
        return "\n".join(str(record) for record in book.data.values())
    else:
        return f"{Fore.RED}No contacts saved.{Style.RESET_ALL}"


@input_error
def delete_contact(args, book):
    if len(args) != 1:
        raise ValueError(
            f"{Fore.RED}Please provide exactly one contact name to delete.{Style.RESET_ALL}"
        )
    name = args[0]
    result = book.delete(name)
    return f"{Fore.YELLOW}Contact {name} deleted successfully.{Style.RESET_ALL}"


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError(
            f"{Fore.RED}Please provide the contact name and the birthday in format DD.MM.YYYY.{Style.RESET_ALL}"
        )
    name, birthday = args
    record: Record = book.find(name)
    return record.add_birthday(birthday)


@input_error
def change_birthday(args, book):
    if len(args) != 2:
        raise ValueError(
            f"{Fore.RED}Please provide the contact name and the new birthday in format DD.MM.YYYY.{Style.RESET_ALL}"
        )
    name, new_birthday = args
    record: Record = book.find(name)
    record.change_birthday(new_birthday)
    return f"{Fore.GREEN}Birthday updated{Style.RESET_ALL}"


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError(
            f"{Fore.RED}Please provide exactly one contact name.{Style.RESET_ALL}"
        )
    name = args[0]
    record = book.find(name)
    if record.birthday:
        return f"{Fore.MAGENTA}{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}.{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}No birthday found for {name}.{Style.RESET_ALL}"


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
    """add address for requested name in contacts"""
    if len(args) < 2:
        raise ValueError(
            f"{Fore.RED} Please provide both a name and an address.{Style.RESET_ALL}"
        )
    name = args[0]
    address = " ".join(args[1:])
    try:
        record: Record = book.find(name)
    except KeyError:
        return f"{Fore.RED}Record for {name} not found.{Style.RESET_ALL}"
    if address:
        try:
            result = record.add_address(address)
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
    if len(args) < 2:
        raise ValueError(
            f"{Fore.RED} Please provide both a name and an address.{Style.RESET_ALL}"
        )
    name = args[0]
    new_address = " ".join(args[1:])
    try:
        record: Record = book.find(name)
    except KeyError:
        return f"{Fore.RED}Record for {name} not found.{Style.RESET_ALL}"
    try:
        result = record.change_address(new_address)
    except Exception:
        return "{Fore.RED}Please provide address according to standard: street, city, state, postcode{Style.RESET_ALL}"
    else:
        return f"{Fore.GREEN}{result}{Style.RESET_ALL}"

@input_error
def show_address(args, book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError(
            f"{Fore.RED} Please provide both a name to show address.{Style.RESET_ALL}"
        )
    name, *_ = args
    try:
        record: Record = book.find(name)
    except KeyError:
        return f"{Fore.RED}Record for {name} not found.{Style.RESET_ALL}"
    address = record.show_address()
    address_detail = (
            f"{name}'s address:\n"
            f"{address}"
            )
    return address_detail

@input_error
def delete_address(args, book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError(
            f"{Fore.RED} Please provide both a name to delete address.{Style.RESET_ALL}"
        )
    name, *_ = args
    try:
        record: Record = book.find(name)
    except KeyError:
        return f"{Fore.RED}Record for {name} not found.{Style.RESET_ALL}"
    record.delete_address()
    return f"{Fore.YELLOW}Address deleted{Style.RESET_ALL}"
