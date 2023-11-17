from datetime import datetime


def to_hidden_view(s):
    """Переводит номер карты/счета в замаскированный вид"""
    if len(s) == 20:
        return "**" + s[-4:]
    return s[:4] + " " + s[4:6] + "** ****" + s[-4:]


def last_executed(executed_op):
    """выводит 5 последних выполненых операций"""
    for i in range(5):
        print(datetime.strftime(datetime.strptime(executed_op[i]['date'][:executed_op[i]['date'].index("T")],
                                                  '%Y-%m-%d').date(), '%d.%m.%Y'), end=" ")
        print(executed_op[i]['description'])
        to = executed_op[i]['to'].split()
        if executed_op[i]['description'] == "Открытие вклада":
            for j in range(len(to) - 1):
                print(to[j], end=" ")
            print(to_hidden_view(to[-1]))
        else:
            get_from = executed_op[i]['from'].split()
            for j in range(len(get_from) - 1):
                print(get_from[j], end=" ")
            print(to_hidden_view(get_from[-1]) + " -> ", end="")
            for j in range(len(to) - 1):
                print(to[j], end=" ")
            print(to_hidden_view(to[-1]))
        print(executed_op[i]['operationAmount']['amount'], end=" ")
        print(executed_op[i]['operationAmount']['currency']['name'])
        print()
