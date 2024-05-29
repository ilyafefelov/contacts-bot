from collections import UserDict
import re


class NoteBook(UserDict):
    def generate_id(self):
        """
        Generates a unique ID for a new entry in the note book.

        Returns:
            int: The generated ID.
        """
        return max(self.data.keys(), default=0) + 1

    def add_record(self, note):
        self.data[note.get_id()] = note

    def search(self, needle):
        """
        Search for notes that match the given needle.

        Args:
            needle (str): The search term to match against note titles, text, and tags.

        Returns:
            list: A list of strings representing the matching notes, including their IDs, titles, and snippets.
        """
        pattern = re.compile(re.escape(needle), re.IGNORECASE)
        results = []
        for note in self.data.values():
            title_match = pattern.search(note.title)
            text_match = pattern.search(note.text)
            tags_match = pattern.search(" ".join(note.tags))
            snippet = ""
            if title_match:
                snippet = self.__get_snippet(
                    note.title, title_match.start(), 30, "title"
                )
            elif text_match:
                snippet = self.__get_snippet(note.text, text_match.start(), 30, "text")
            elif tags_match:
                snippet = self.__get_snippet(
                    " ".join(note.tags), tags_match.start(), 30, "tags"
                )

            if snippet:
                results.append(f'{note.get_id()}. "{note.title}" ({snippet})')
        return results

    def get_list(self):
        return list(self.data.values())

    def get_by_id(self, note_id):
        return self.data.get(note_id)

    def edit(self, note_id, title, text):
        if note_id not in self.data:
            return False

        if title:
            self.data[note_id].title = title
        if text:
            self.data[note_id].text = text
        return True

    def delete(self, note_id):
        if note_id not in self.data:
            return False

        del self.data[note_id]
        return True

    def delete_tag(self, note_id, tag):
        if note_id not in self.data:
            return False

        note = self.data[note_id]
        return note.delete_tag(tag)

    def add_tag(self, note_id, tag):
        if note_id not in self.data:
            return False
        note = self.data[note_id]
        return note.add_tag(tag)

    def __get_snippet(self, text, start_idx, length, text_type):
        """
        Returns a snippet of the given text based on the start index and length.

        Args:
            text (str): The original text.
            start_idx (int): The starting index of the snippet.
            length (int): The desired length of the snippet.
            text_type (str): The type of the text (e.g., title, description).

        Returns:
            str: The snippet of the text.

        """
        if len(text) <= length:
            return f"{text_type}: {text}"

        start = max(0, start_idx - 5)
        end = min(len(text), start_idx + length - 5)
        return f"{text_type}:..{text[start:end].strip()}...."
