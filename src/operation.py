from datetime import datetime
import re


class Operation:
    def __init__(self, pk, date, state, operation_amount, description, to, from_=None):
        self.pk = pk
        self.date = self.convert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.to = self.hide_number(to)
        self.from_ = self.hide_number(from_) if from_ else ''

    def convert_date(self, date):
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        date = datetime.strptime(date, date_format)
        return date.date().strftime('%d.%m.%Y')

    def hide_number(self, pay_type):
        data = pay_type.split()
        if pay_type.startswith('Счет'):
            data[-1] = '**' + data[-1][-4:]
            return ' '.join(data)
        else:
            hidden_number = data[-1][0:6] + '******' + data[-1][-4:]
            return re.sub("(.{4})", r"\1 ", hidden_number)

    def __str__(self):
        amount = self.operation_amount['amount']
        currency = self.operation_amount['currency']['name']
        return f'{self.date } {self.description}\n{self.from_} -> {self.to}\n{amount} {currency}'