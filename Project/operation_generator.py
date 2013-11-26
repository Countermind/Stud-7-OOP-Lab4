__author__ = 'Kostya'
from transfer import Transfer
from operation_checker import OperationChecker
from account_rep import AccountRep


class OperationGenerator:
    def __init__(self, account, atm):
        self._account = account
        self._atm = atm
        self._operation_checker = OperationChecker(AccountRep(), self._atm)

    def get_money_operation(self, money_amount):
        return Transfer(money_amount, [self._account.account_number, self._atm], None, self._operation_checker)

    def pay_rent_operation(self, money_amount):
        return Transfer(money_amount, self._account.account_number, 'RENT_ACCOUNT_NUMBER', self._operation_checker)

    def put_money_operation(self, money_amount):
        return Transfer(money_amount, None, [self._account.account_number, self._atm], self._operation_checker)