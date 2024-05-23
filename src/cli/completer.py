from prompt_toolkit.completion import Completer, Completion

# List of available commands
commands = [
    "hello",
    "add",
    "add-birthday",
    "show-birthday",
    "birthdays",
    "change",
    "delete-phone",
    "change-phone",
    "change-birthday",
    "phone",
    "all",
    "search",
    "delete",
    "add-note",
    "get-note",
    "edit-note",
    "add-note-tag",
    "delete-note-tag",
    "list-notes",
    "search-notes",
    "delete-note",
    "help",
    "close", 
    "exit"
]

class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        # We are interested only in the first word
        text_before_cursor = document.text_before_cursor
        if ' ' in text_before_cursor:
            return  # Do not show completions after a space
        words = text_before_cursor.split()
        if len(words) == 1:
            word_before_cursor = words[0]
            for command in commands:
                if command.startswith(word_before_cursor):
                    yield Completion(command, start_position=-len(word_before_cursor))