__author__ = 'Kostya'
from account import Account


class ATM(Account):
    def __init__(self, available_cash):
        super(ATM, self).__init__(cash_amount=available_cash, login='ATM')

    def __str__(self):
        return 'ATM has ${0}'.format(self.cash_amount)