from datetime import datetime


def write_log(command):
    time = datetime.now().strftime('%d.%m.%y %H:%M:%S')
    with open('log.txt', 'a') as file:
        file.write(f'{time}, {command}\n')
