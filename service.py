from util_json import *
from model import Note
from _datetime import datetime


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


def modify_note():
    temp = json.load(open('notes.json', encoding='utf-8'))
    input_key = int(input('Enter id of note to edit: '))

    for index, dict_ in enumerate(temp):

        if 'id' in dict_ and dict_['id'] == input_key:
            changed_title = input('Enter new title: ')
            changed_text = input('Enter new text: ')

            temp[index] = {
                'id': input_key,
                'date': datetime.now().strftime("%d.%m.%y %H:%M:%S"),
                'title': changed_title,
                'text': changed_text
            }
            print('Note was modified')
            rewrite_file(temp)


def delete_note():
    temp = json.load(open('notes.json', encoding='utf-8'))
    input_key = int(input('Enter id of note to edit: '))

    for index, dict_ in enumerate(temp):
        if 'id' in dict_ and dict_['id'] == input_key:
            temp.remove(dict_)
            print(f'Note id{input_key} was successfully deleted!')
        rewrite_file(temp)


def search_note():
    temp = json.load(open('notes.json', encoding='utf-8'))
    input_key = input('Search note by id, title or date of creation?\n'
                      'enter "id" or "title" or "date": ')
    if input_key == 'id':
        note_id = int(input('enter id of note to find: '))
        result = list(filter(lambda x: x['id'] == note_id, temp))
        if not result:
            print(f'There is no notes with id{note_id}')
        else:
            print_note(result)
    elif input_key == 'title':
        title = input('Enter title of note to find: ')
        result = list(filter(lambda x: x['title'] == title, temp))
        if not result:
            print(f'There is no notes with title "{title}"')
        else:
            print_note(result)
    elif input_key == 'date':
        date = input('Enter date in the format dd.mm.yy: ')
        result = list(filter(lambda x: x['date'] == date, temp))
        if not result:
            print(f'There is no notes with date "{date}"')
        else:
            print_note(result)
    else:
        print('there is no such command')


def print_note(notes):
    for note in notes:
        for k, v in note.items():
            print(k, ':', v)
        print()


def save_data(data):
    save_file(data)
