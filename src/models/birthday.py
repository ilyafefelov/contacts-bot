from src.models.field import Field
from datetime import datetime, date

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
            if self.value > date.today():
                raise ValueError("Birthday cannot be in the future.")
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use DD.MM.YYYY. {str(e)}") from e
        super().__init__(self.value)
