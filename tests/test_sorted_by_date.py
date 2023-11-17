from utils import executed_sorted_by_date
import pytest


@pytest.mark.parametrize("op, expected", [(
        [{
            'state': 'EXECUTED',
            'date': '2019-08-04T20:17:25.443322'
        },
            {

            },
            {
                'state': 'EXECUTED',
                'date': '2018-07-15T18:44:13.346362'
            }
        ], [{
            'state': 'EXECUTED',
            'date': '2019-08-04T20:17:25.443322'
        },
            {
                'state': 'EXECUTED',
                'date': '2018-07-15T18:44:13.346362'
            }]),
    ([
         {
             'state': 'CANCELED',
             'date': '2019-08-04T20:17:25.443322'
         },
         {

         },
         {
             'state': 'EXECUTED',
             'date': '2018-07-15T18:44:13.346362',
             'description': 'Перевод с карты на счет',
             'to': 'Счет 19213886662094884261',
             'from': 'Visa Gold 9657499677062945',
             'operationAmount': {
                 'amount': '71024.64',
                 'currency': {
                     'name': 'руб.'
                 }
             }
         },
         {
            'state': 'EXECUTED',
            'date': '2018-08-06T16:22:54.643491',
            'description': 'Открытие вклада',
            'to': 'Счет 19213886662094884261',
            'operationAmount': {
                 'amount': '17628.50',
                 'currency': {
                     'name': 'USD'
                 }
             }
         }
     ], [
         {
             'state': 'EXECUTED',
             'date': '2018-08-06T16:22:54.643491',
             'description': 'Открытие вклада',
             'to': 'Счет 19213886662094884261',
             'operationAmount': {
                 'amount': '17628.50',
                 'currency': {
                     'name': 'USD'
                 }
             }
         },
         {
             'state': 'EXECUTED',
             'date': '2018-07-15T18:44:13.346362',
             'description': 'Перевод с карты на счет',
             'to': 'Счет 19213886662094884261',
             'from': 'Visa Gold 9657499677062945',
             'operationAmount': {
                 'amount': '71024.64',
                 'currency': {
                     'name': 'руб.'
                 }
             }
         }
     ])
])
def test_sorted_by_date(op, expected):
    assert executed_sorted_by_date.get_sorted_executed(op) == expected
