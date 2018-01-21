from sys import argv
import json, os


def load_data(filepath):

    if not os.path.exists(filepath):
        print("There is no file in the specified path.")
        return None

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(raw_json):

    print(json.dumps(raw_json, sort_keys=True, indent=4, ensure_ascii=False))
    return None


if __name__ == '__main__':
    if len(argv) > 1:
        pretty_print_json(load_data(argv[1]))
    else:
        print("Введите путь до файла с произвольными данными в формате JSON")
        pretty_print_json(load_data(input()))