__author__ = 'Kostya'


class OperationChecker:
    def __init__(self, account_rep, atm):
        self._account_repository = account_rep
        self._atm = atm

    def check(self, transfer_from, money_amount):
        for acc in transfer_from:
            if isinstance(acc, basestring):
                account_id = acc
            else:
                account_id = acc.account_number
            if not self.account_has_enough_money(account_id, money_amount):
                return '{0} has not enough money'.format(account_id)

    def account_has_enough_money(self, account_id, need_money):
        if account_id == 'ATM':
            available_cash = self._atm.cash_amount
        else:
            available_cash = self._account_repository.get_cash_amount(account_id)

        return available_cash >= need_money