from service import *
from util_json import *


def start():
    print('Welcome to notes app!\n')
    comands = ['create', 'find', 'showlist', 'edit', 'delete', 'exit']
    while True:
        comand = input(f'- Enter "{comands[0]}" to create new note\n'
                       f'- Enter "{comands[1]}" to search note\n'
                       f'- Enter "{comands[2]}" to show notes list\n'
                       f'- Enter "{comands[3]}" to modify note\n'
                       f'- Enter "{comands[4]}" to delete note\n'
                       f'- Enter "{comands[5]}" to exit app\n')
        # try:
        if comand == 'exit':
            print('Thank you for using notes app')
            break
        elif comand == 'create':
            note = set_note()
            save_data(note)
            print('Note was created')

        elif comand == 'showlist':
            get_all_notes()

        elif comand == 'edit':
            modify_note()

        elif comand == 'delete':
            delete_note()
        elif comand == 'find':
            search_note()


        # except:
        #     print('Error. Try again')
