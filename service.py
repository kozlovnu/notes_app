from writer import *
from model import Note
import view

notes_list = []

def get_all_notes():
    return notes_list

def set_title():
    title = input('title: ')
    return title

def set_text():
    text = input('text: ')
    return text

def note_dict(id, date, title, text):
    note_dict = {
        'id': id,
        'date': date,
        'title': title,
        'text': text
    }
    return note_dict

def set_note():
    title = set_title()
    text = set_text()
    note = Note(title, text)
    notes = note_dict(note.get_id(), note.get_date(), title, text)
    return notes

def save_file(data):
    save_file(data)

# def add_note():
#     notes_list.append(Note.set_note(Note(), input('title: '), input('text: ')))
#     return Note.notes_list

def find_note(id):
    for note in notes_list:
        if note.id == id:
            return note
    return "Error"

