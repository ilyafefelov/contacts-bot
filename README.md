🐣🐣🐣Create New Branches from main for your Taks, then pull request them into the main branch.


Running the Project
Navigate to the Project Directory:
Ensure you are in the contact_bot directory.


cd contact_bot
Install Dependencies:
Install the required packages from requirements.txt.


```pip install -r requirements.txt```



Run the Project:
Use the python -m command with the module path to run the main script.
```
python -m src.main
```


Run Tests:
Use unittest to run the tests.

```python -m unittest discover tests```



contact_bot/
├── src/
│   ├── __init__.py
│   ├── cli/
│   │   ├── interface.py
│   ├── models/
│   │   ├── address_book.py
│   │   ├── note_book.py
│   │   ├── record.py
│   │   ├── note.py
│   ├── utils/
│   │   ├── data_handler.py
│   │   ├── input_error.py
│   ├── commands/
│   │   ├── contact_commands.py
│   │   ├── note_commands.py
│   ├── main.py
├── tests/
│   ├── test_interface.py
│   ├── test_contact_commands.py
│   ├── test_note_commands.py
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
