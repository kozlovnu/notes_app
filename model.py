from datetime import *

class Note:
    id_counter = 0

    def __init__(self, id, title, text):
        self.id = id
        self.date = datetime.now().strftime("%d.%m.%y %H:%M:%S")
        self.title = title
        self.text = text

    def set_note(self, title, text):
        Note.id_counter += 1
        date = datetime.now().strftime("%d.%m.%y %H:%M:%S")
        return Note(Note.id_counter, date, title, text)

    def get_note(self, id, date, title, text):
        if Note.id_counter < id:
            Note.id_counter = id
        return Note(id, date, title, text)

    def to_string(self) -> str:
        return f"id: {self.id}\n date: {self.date}\n title: {self.title}\n text: {self.text}"

