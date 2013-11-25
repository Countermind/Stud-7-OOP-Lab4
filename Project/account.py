__author__ = 'Kostya'


class Account(object):
    def __init__(self, login='', password='', cash_amount=.0):
        self.__login = login
        self.__password = password
        self._cash_amount = cash_amount

    def match(self, login, password):
        return self.__login == login and self.__password == password

    @property
    def account_number(self):
        #assume account number is the same as login
        return self.__login

    @property
    def cash_amount(self):
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, value):
        self._cash_amount = value

    def increase_cash(self, value):
        self._cash_amount += value

    def decrease_cash(self, value):
        if self._cash_amount < value:
            raise AttributeError()
        self._cash_amount -= value

    def __str__(self):
        return 'Account #{0} has ${1}'.format(self.account_number, self.cash_amount)