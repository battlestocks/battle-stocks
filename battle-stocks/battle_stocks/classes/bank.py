from symtable import Symbol
# from battle_stocks.classes.user import User
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import SYMBOL
from battle_stocks.utils.scraping import get_current_stock_price

class Bank:
    def __init__(self, balance=10000):
        self.balance = balance 
        
    def deposit(self):            
        if self.balance < Transaction.current_total_value():
            cash_total = self.balance - Transaction.current_total_value()
        return cash_total

    def withdraw(self):
        get_money = float(get_current_stock_price(self.symbol))
        self.balance += get_money

    def get_balance(self):
        pass

    def set_starting_balance():
        pass

if __name__ == '__main__':
    apple_stock = Transaction.buy_stock(SYMBOL['APPLE'], 10)
    print(apple_stock.current_total_value())
    print(Bank.withdraw())

