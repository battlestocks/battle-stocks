from lib2to3.pgen2.token import BACKQUOTE
from battle_stocks.utils.constants import STARTING_BANK

class Bank:
    def __init__(self, balance=STARTING_BANK):
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('\nNot enough money, try another amount!\n')
        else:
            self.balance -= amount

    def get_balance(self):
        return round(self.balance, 2)

