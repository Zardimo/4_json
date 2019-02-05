import json
import os
from sys import argv
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as prettystyle:
        return json.load(prettystyle)


def pretty_print_json(json_way):
    return json.dumps(json_way, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        exit("Укажите путь к файлу")
    json_way = load_data(argv[1])
    if not json_way:
        exit("Укажите верный путь к файлу")
    print(pretty_print_json(json_way))
