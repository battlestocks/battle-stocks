from battle_stocks.classes.bank import Bank
from battle_stocks.classes.portfolio import Portfolio


class User:
    def __init__(self, name):
        self.name = name
        self.bank = Bank()
        self.portfolio = Portfolio()

    def show_current_portfolio(self):
        return self.portfolio.stock_shares

    def lookup_stock():
        pass

    def get_portfolio_balance(self): 
         pass
        
    def get_current_bank_balance():
        pass