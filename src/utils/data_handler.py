import pickle
from src.models.address_book import AddressBook
from src.models.note_book import NoteBook

def save_data(data, filename="data.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_data(filename="data.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook(), NoteBook()  # Return new books if the file is not found
