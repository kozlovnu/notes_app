from util_json import *
from model import Note
import view


def get_all_notes():
    try:
        data = load_file()
        for val in data:
            print(val)
    except FileNotFoundError:
        print(f'File is empty\n{"-" * 15}')


def set_title():
    title = input('input title: ')
    return title


def set_text():
    text = input('input text: ')
    return text


def set_note_dict(id, date, title, text):
    note = {
        'id': id,
        'date': date,
        'title': title,
        'text': text
    }
    return note


def set_note():
    title = set_title()
    text = set_text()
    note = Note(title, text)
    notes = set_note_dict(note.get_id(), note.get_date(), title, text)
    return notes


def save_data(data):
    save_file(data)



