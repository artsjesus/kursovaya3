from src.utils import number_output, transaction, account_number



def test_number_output():
    assert number_output("1596837868705199") == "1596 83** **** 5199"


def test_transaction():
    assert (transaction({'id': 863064926, 'state': 'EXECUTED', 'date': '08.12.2019', 'operationAmount':
        {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},'description': 'Открытие вклада',
        'to': 'Счет 90424923579946435907'}) == '08.12.2019', 'Открытие вклада', 'Счет 90424923579946435907', '41096.24',
        'USD')

def test_account_number():
    assert account_number("64686473678894779589") == "**9589"

