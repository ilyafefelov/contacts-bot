from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise KeyError(f"Record for {name} not found.")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record for {name} deleted."
        raise KeyError(f"Record for {name} not found.")

    def get_upcoming_birthdays(self, days=7):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value
                birthday_this_year = datetime(
                    today.year, birthday.month, birthday.day
                ).date()

                if birthday_this_year < today:
                    birthday_this_year = datetime(
                        today.year + 1, birthday.month, birthday.day
                    ).date()

                days_before_birthday = (birthday_this_year - today).days

                if days_before_birthday <= days:
                    upcoming_birthdays.append(record.name.value)

        return upcoming_birthdays
