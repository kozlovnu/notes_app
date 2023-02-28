from service import *
from util_json import *
from logger import write_log


def start():
    write_log('started app')
    print('Welcome to notes app!\n')
    commands = ['create', 'find', 'showlist', 'edit', 'delete', 'exit']
    while True:
        command = input(f'- Enter "{commands[0]}" to create new note\n'
                       f'- Enter "{commands[1]}" to search note\n'
                       f'- Enter "{commands[2]}" to show notes list\n'
                       f'- Enter "{commands[3]}" to modify note\n'
                       f'- Enter "{commands[4]}" to delete note\n'
                       f'- Enter "{commands[5]}" to exit app\n')
        try:
            if command == 'exit':
                print('Thank you for using notes app')
                write_log(command)
                break
            elif command == 'create':
                note = set_note()
                save_data(note)
                write_log(command)
                print('Note was created')

            elif command == 'showlist':
                get_all_notes()
                write_log(command)

            elif command == 'edit':
                modify_note()
                write_log(command)

            elif command == 'delete':
                delete_note()
                write_log(command)

            elif command == 'find':
                search_note()
                write_log(command)


        except:
            print('Error. Try again')
