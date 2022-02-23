from battle_stocks.utils.constants import STARTING_BANK

class Bank:
    def __init__(self, balance=STARTING_BANK):
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough money, try another amount!')
        else:
            self.balance -= amount

    def get_balance(self):
        return round(self.balance, 2)

