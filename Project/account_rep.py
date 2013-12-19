__author__ = 'Kostya'
from singleton import Singleton
from account import Account
import copy


@Singleton
class AccountRep:
    __accounts = [
        Account('1010', 'key', 500),
        Account('0023', 'pwd', 10),
        Account('RENT_ACCOUNT_NUMBER', 0123111123, 0),
        Account('rich', '$$$', 999999)
    ]

    def __init__(self):
        pass

    def authorize(self, login, password):
        #imitate receiving account information from server
        accounts = list(AccountRep.__accounts)
        try:
            matching_account = next(ac for ac in accounts if ac.match(login, password))
            return matching_account
        except StopIteration:
            return None

    def get_cash_amount(self, account_number):
        accounts = copy.deepcopy(AccountRep.__accounts)
        matching_account = next(ac for ac in accounts if ac.account_number == account_number)
        if matching_account:
            return matching_account.cash_amount
        return None

    def get_account(self, account_number):
        accounts = list(AccountRep.__accounts)
        return next(ac for ac in accounts if ac.account_number == account_number)

    def get_all_accounts(self):
        return list(AccountRep.__accounts)