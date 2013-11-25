__author__ = 'Kostya'
from account_rep import AccountRep


class Transfer:
    def __init__(self, money_amount, transfer_from, transfer_to, operation_checker):
        self._transfer_money = money_amount
        if not transfer_from:
            self._transfer_from = []
        elif isinstance(transfer_from, list):
            self._transfer_from = list(transfer_from)
        else:
            self._transfer_from = [transfer_from]

        if not transfer_to:
            self._transfer_to = []
        elif isinstance(transfer_to, list):
            self._transfer_to = list(transfer_to)
        else:
            self._transfer_to = [transfer_to]
        self._operation_checker = operation_checker

    @property
    def transfer_money(self):
        return self._transfer_money

    @transfer_money.setter
    def transfer_money(self, value):
        self._transfer_money = value

    @property
    def transfer_from(self):
        return self._transfer_from

    @property
    def transfer_to(self):
        return self._transfer_to

    def process(self):
        result_message = None
        if self._operation_checker:
            result_message = self._operation_checker.check(self.transfer_from, self.transfer_money)

        if not result_message:
            account_repository = AccountRep()
            for acc in self.transfer_from:
                if isinstance(acc, basestring):
                    transfer_from_account = account_repository.get_account(acc)
                else:
                    transfer_from_account = acc
                transfer_from_account.decrease_cash(self.transfer_money)

            for acc in self.transfer_to:
                if isinstance(acc, basestring):
                    transfer_to_account = account_repository.get_account(acc)
                else:
                    transfer_to_account = acc
                transfer_to_account.increase_cash(self.transfer_money)


        return result_message