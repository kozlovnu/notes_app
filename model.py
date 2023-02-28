import uuid
from datetime import *


class Note:

    def __init__(self, title_text, text_text):
        self.id = int(str(uuid.uuid4().int)[0:4])
        self.date = datetime.now().strftime("%d.%m.%y")
        self.title = title_text
        self.text = text_text

    def get_title(self):
        return self.title

    def set_title(self, x):
        self.title = x

    def get_text(self):
        return self.text

    def set_text(self, x):
        self.text = x

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def __str__(self) -> str:
        return f"id: {self.id}\ndate: {self.date}\ntitle: {self.title}\ntext: {self.text}\n{'-' * 10}\n"
