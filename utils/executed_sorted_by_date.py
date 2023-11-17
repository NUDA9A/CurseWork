def get_sorted_executed(op):
    """Выбирает только те операции которые были выполнены
    и возвращает список словарей, отсортированный по дате в порядке убывания"""
    executed = []
    for operation in op:
        if len(operation.keys()) > 0:
            if operation['state'] == 'EXECUTED':
                executed.append(operation)
    return sorted(executed, key=lambda x: x['date'], reverse=True)
