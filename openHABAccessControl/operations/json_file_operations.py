import glob
import json
import os


def store_token_to_file_system(filename, token):
    # store token as json format to local fs
    with open(filename + '.json', 'w', encoding='utf-8') as f:
        json.dump(token, f, ensure_ascii=False, indent=4)


def delete_json_files():
    json_files = glob.glob('*.json')
    for filename in json_files:
        os.remove(filename)
