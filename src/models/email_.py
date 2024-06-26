import re
from src.models.field import Field
from colorama import Fore

class Email(Field):
    """
    creates email if valid value provided <name@domain>
    """

    def __init__(self, email: str) -> str:
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'   # RegEx for validating an Email
        if (re.fullmatch(regex, email)):
            self.__email = email
        else:
            raise ValueError(Fore.RED + "Invalid Email" + Fore.RESET)

    def __str__(self):
        return f"{self.email}"


# Driver Code
# if __name__ == '__main__':
#     # Enter the email
#     email = Email("ankitrai326@gmail.com")
#     print(email)
