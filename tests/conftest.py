import pytest


@pytest.fixture
def valid_data():
    return [{
    "pk": 863064926,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operation_amount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from_": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "pk": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operation_amount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from_": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]