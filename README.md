# CLI Contact and Note Manager

## Overview

Welcome to the CLI Contact and Note Manager! This project is a command-line application designed to manage contacts and notes efficiently. Developed as part of our Master's in Computer Science program, this project aims to provide a user-friendly interface for handling various contact details and notes through simple CLI commands.

## Features

- **Contact Management:** Add, update, delete, and search contacts with details such as phone numbers, emails, addresses, and birthdays.
- **Note Management:** Create, edit, delete, and search notes with tags.
- **Birthday Reminders:** View upcoming birthdays within a specified number of days.
- **User-Friendly Commands:** Intuitive commands to perform various operations quickly and efficiently.

## Download and Installation Instructions

To get started with the CLI Contact and Note Manager, follow these steps:

### 1. Clone the Repository

Clone the repository and navigate to the project directory:

```
git clone https://github.com/ilyafefelov/contacts-bot
cd contacts-bot
```
2. Install the Required Dependencies
The dependencies are listed in the requirements.txt file. You can install them using pip:

```pip install -r requirements.txt```


3. Run the Project
You can run the project using the python -m command with the module path to run the main script:

```python -m src.main```


4. Install the Project in Edit Mode 
This allows you to make changes to the project and see them reflected without having to reinstall the project. You can do this with the following command:

```pip install -e .```


5. Run the Project in Edit Mode
After installing the project in edit mode, you can run the project using the following command:

```contact_bot```


###### or just:
```
git clone https://github.com/ilyafefelov/contacts-bot
pip install contacts-bot
cls
contact_bot
```



### CLI Commands
Below is a detailed list of available commands and their usage:

Contact Commands
###### Add Contact

```add [name] [phone] [email] [birthday]```
Add a new contact with the specified name and other details.

###### Change Phone Number

```change-phone --[name] --[old phone] --[new phone]```
Change the phone number for the specified contact.

###### Show Phone Numbers

```phone --[name]```
Show phone numbers for the specified contact.

###### Show All Contacts

```all```
Show all contacts in the address book.

###### Add Birthday

```add-birthday --[name] --[birthday]```
Add a birthday for the specified contact.

```change-birthday --[name] --[birthday]```
Change birthday for the specified contact.

###### Show Birthday

```show-birthday --[name]```
Show the birthday for the specified contact.

###### Show Upcoming Birthdays

```birthdays [days]```
Show contacts with birthdays in the next specified number of days.

###### Search Contact

```search [name]```
Find a contact by name.

###### Delete Contact

```delete --[name]```
Delete a contact by name.

###### Add Email

```add-email --[name] --[email]```
Add an email for the specified contact.

###### Show Email

```show-email --[name]```
Show the email for the specified contact.

###### Change Email

```change-email --[name] --[new email]```
Change the email for the specified contact.

###### Delete Email

```delete-email --[name]```
Delete the email for the specified contact.

###### Add Address

```add-address --[name] --[address]```
Add the address for the specified contact.

###### Show Address

```show-address --[name]```
Show the address for the specified contact.

###### Change Address

```change-address --[name] --[new address]```
Change the address for the specified contact.


######  Delete Address

```delete-address --[name]```
Delete the address for the specified contact.


#### Note Commands
###### Add Note

```add-note --title [title] --text [text]```
Add a new note with the specified title and text.

###### Get Note

```get-note [ID]```
Get a note by its ID.

###### Edit Note

```edit-note --id [ID] --title [title] --text [text]```
Edit a note by its ID.

###### Delete Note

```delete-note [ID]```
Delete a note by its ID.

###### Add Note Tag

```add-note-tag --id [ID] --tag [tag]```
Add a tag to a note by its ID.

###### Delete Note Tag

```delete-note-tag --id [ID] --tag [tag]```
Delete a tag from a note by its ID.

###### Search Notes

```search-notes [text]```
Find notes by text.

###### List Notes

```list-notes```
List all notes.



#### General Commands

###### Hello

```hello```
Get a greeting from the bot.

###### Help

```help```
Display help information for all commands.

###### Close or Exit

```close```
```exit```
Close the program.



### License
This project is licensed under the MIT License. See the LICENSE file for more details.

We hope you find the CLI Contact and Note Manager useful and easy to use. Your feedback is highly appreciated!

Happy managing!

The Project Team 4
