from datetime import datetime
from src.models.fields import Name, Phone
from src.models.email_ import Email
from src.models.address import Address
from src.models.birthday import Birthday
from colorama import Fore, Style

class Record:
    def __init__(self, name, address=None, phones=None, email=None, birthday=None):
        self.name = Name(name)
        self.address = Address(address) if address else None
        self.phones = phones if phones else []
        self.email = Email(email) if email else None
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        new_phone = Phone(str(phone))
        if any(p.value == new_phone.value for p in self.phones):
            return f"{Fore.MAGENTA}Phone {phone} already exists for {self.name.value}.{Style.RESET_ALL}"
        self.phones.append(new_phone)
        return f"{Fore.GREEN}Phone {phone} added to {self.name.value}.{Style.RESET_ALL}"

    def add_email(self, email: str) -> str:
        self.email = Email(email)
        return f"Email {email} added to {self.name.value}."

    def show_email(self) -> str:
        return self.email

    def change_email(self, new_email: str) -> None:
        self.email = new_email

    def delete_email(self) -> None:
        self.email = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"Birthday {birthday} added to {self.name.value}."

    def add_address(self, address: str) -> str:
        self.address = Address(address)
        return f"Address added to {self.name.value}"

    def show_address(self) -> str:
        return self.address

    def change_address(self, new_address: str) -> None:
        self.add_address = new_address

    def delete_address(self) -> None:
        self.address = None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = (
            self.birthday.value.strftime("%d.%m.%Y")
            if self.birthday
            else "No birthday set"
        )
        email = self.email if self.email else "No email set"
        address = self.address if self.address else "No address set"
        contact_detail = (
            f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}, email: {email}, address:\n"
            f"{address}"
            )
        return contact_detail

    def change_birthday(self, new_birthday: str) -> None:
        self.birthday = Birthday(new_birthday)

    def change_phone(self, old_phone: str, new_phone: str) -> None:
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"{Fore.YELLOW}Phone {old_phone} changed to {new_phone}.{Style.RESET_ALL}"
        raise ValueError(f"Phone {old_phone} not found for {self.name.value}")

    def delete_phone(self, phone: str) -> None:
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Phone {phone} not found for {self.name.value}")


# r = Record("tom")
# print(r)
# r.add_phone('1234567890')
# print(r)
# r.show_email()
# r.add_email("fghhrk@ukr.net")
# print(r)
# print(r.show_email())
