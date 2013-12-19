__author__ = 'Kostya'
from account_rep import AccountRep
from atm import ATM
from operation_generator import OperationGenerator
import re


cash_machine = ATM(1000)
account = None
while not account:
    login = raw_input('Enter login: ')
    password = raw_input('Enter password: ')
    account_repository = AccountRep.instance()
    account = account_repository.authorize(login, password)

    if not account:
        print 'Wrong login/password combination!\n'

operations = OperationGenerator(account, cash_machine)
while True:
    command = raw_input('\nEnter command: ')
    match = re.search(r'insert money (?P<money_amount>\d+(\.\d+)?)', command)
    if match:
        operation = operations.put_money_operation(float(match.group('money_amount')))
        result = operation.process()
        if result:
            print result
        else:
            print 'Operation executed successfully'
        continue

    match = re.search(r'get money (?P<money_amount>\d+(\.\d+)?)', command)
    if match:
        operation = operations.get_money_operation(float(match.group('money_amount')))
        result = operation.process()
        if result:
            print result
        else:
            print 'Operation executed successfully'
        continue

    match = re.search(r'pay rent (?P<money_amount>\d+(.\d+)?)', command)
    if match:
        operation = operations.pay_rent_operation(float(match.group('money_amount')))
        result = operation.process()
        if result:
            print result
        else:
            print 'Operation executed successfully'
        continue

    match = re.search(r'info', command)
    if match:
        account_repository = AccountRep()
        for acc in account_repository.get_all_accounts():
            print acc
        print cash_machine

    match = re.search(r'ex(it)?', command)
    if match:
        break