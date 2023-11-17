from utils.read_json import read_json
from utils.executed_sorted_by_date import get_sorted_executed
from utils.transactions_info import last_executed


op = read_json('operations.json')
executed = get_sorted_executed(op)
last_executed(executed)

