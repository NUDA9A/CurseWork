import json


def read_json(name):
    """Открывает json файл и читает его. Возвращает список словарей"""
    with open(name, 'r', encoding="utf8") as operations:
        op = json.load(operations)
        return op
