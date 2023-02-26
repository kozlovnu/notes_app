import json

def save_file(data):
    with open ('data.json', 'a') as outfile:
        json.dump(data, outfile, indent=2)