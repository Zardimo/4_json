import json
import os
from sys import argv
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as prettystyle:
        return json.load(prettystyle)


def pretty_print_json(base_for_change):
    return json.dumps(base_for_change, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        exit('Укажите путь к файлу')
    try:
        base_for_change = load_data(argv[1])
    except json.decoder.JSONDecodeError:
        exit('Данные в файле должны быть формата json')
    if not base_for_change:
        exit('Укажите верный путь к файлу')
    print(pretty_print_json(base_for_change))
