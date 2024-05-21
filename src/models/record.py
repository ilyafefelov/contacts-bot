from datetime import datetime
from src.models.fields import Name, Phone, Address, Birthday
#from fields import Name, Phone, Birthday
#from email import Email
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
        return [p.value for p in self.phones]

    def add_email(self, email: str) -> str:
        self.email = Email(email)
        return f"Email {email} added to {self.name.value}."
    
    def show_email(self) -> str:
        return self.email

    def add_address(self, address):
        self.address = Address(address)
        return f"Address {address} added to {self.name.value}."

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"Birthday {birthday} added to {self.name.value}."

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = (
            self.birthday.value.strftime("%d.%m.%Y")
            if self.birthday
            else "No birthday set"
        )
        email = self.email.value if self.email else "No email set"
        address = self.address.value if self.address else "No address set"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}, email: {email}, address: {address}"



r = Record("tom")
print(r)
r.add_phone('1234567890')
print(r)
r.show_email()
r.add_email("fghhrk@ukr.net")
print(r)