class Note:
    def __init__(self, note_id: int, title: str, text: str, tags=None):
        if tags is None:
            tags = []
        self.id = note_id
        self.title = title
        self.text = text
        self.tags = tags

    def get_id(self):
        return self.id

    def __str__(self):
        short_text = self.text[:30] + "..." if len(self.text) > 30 else self.text
        return f"{self.id}. [{self.title}] {short_text}"

    def add_tag(self, tag):
        self.tags.append(tag)
        return True

    def delete_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def show_note(self):
        tags = 'No tags'
        if self.tags:
            tags = ", ".join(self.tags)
        return f"""
Note ID: {self.id}
Title: {self.title}
Text: {self.text}
Tags: {tags}
        """
