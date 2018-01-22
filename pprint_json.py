import json
import argparse
from sys import argv


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("There is no file in the specified path.")
        quit()

def pretty_print_json(parent_data):
    print(json.dumps(parent_data, sort_keys=True, indent=4, ensure_ascii=False))


def get_path_data():
    if len(argv) > 1:
        return argv[1]
    else:
        print("Введите путь до файла формата JSON")
        return input()


if __name__ == '__main__':
    pretty_print_json(load_data(get_path_data()))

