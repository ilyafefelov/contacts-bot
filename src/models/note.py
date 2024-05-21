class Note:
    def __init__(self, note_id: int, title: str, text: str):
        self.id = note_id
        self.title = title
        self.text = text

    def get_id(self):
        return self.id

    def __str__(self):
        short_text = self.text[:30] + "..." if len(self.text) > 30 else self.text
        return f"{self.id}. [{self.title}] {short_text}"
