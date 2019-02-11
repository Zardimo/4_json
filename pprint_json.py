import json
import os
from sys import argv
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(python_object):
    return json.dumps(python_object, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        exit('Укажите путь к файлу')
    try:
        python_object = load_data(argv[1])
    except json.decoder.JSONDecodeError:
        exit('Данные в файле должны быть формата json')
    if not python_object:
        exit('Укажите верный путь к файлу')
    print(pretty_print_json(python_object))
