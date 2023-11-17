import json


def read_json():
    """Открывает json файл и читает его. Возвращает список словарей"""
    with open('operations.json', 'r', encoding="utf8") as operations:
        op = json.load(operations)
        return op
