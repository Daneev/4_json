import argparse
import json


def pretty_print_json(parent_data):
    print(json.dumps(parent_data, sort_keys=True, indent=4, ensure_ascii=False))


def get_file():
    parser = argparse.ArgumentParser()

    # required argument
    parser.add_argument('file', help='Enter the path to the JSON file', type=argparse.FileType('r', encoding='utf-8'))
    with parser.parse_args().file as file:
        return json.load(file)



if __name__ == '__main__':
    pretty_print_json(get_file())
