from sys import argv
import json, os


def load_data(filepath):
    if not os.path.exists(filepath):
        print("There is no file in the specified path.")
        return None

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(parent_data):
    print(json.dumps(parent_data, sort_keys=True, indent=4, ensure_ascii=False))
    return None


def get_path_data():
    if len(argv) > 1:
        return argv[1]  # возвращаем путь к файлу, если программу запустили с параметрами
    else:
        print("Введите путь до файла формата JSON")
        return input()  # если программа запущена без параметров,
        # ожидаем ввода пути к файлу с клавиатуры.


if __name__ == '__main__':
    pretty_print_json(load_data(get_path_data()))
