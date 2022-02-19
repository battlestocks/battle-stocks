#import matplotlib.pyplot as plt
from battle_stocks.classes.transaction import Transaction
from battle_stocks.classes.stock import get_current_stock_price
from battle_stocks.classes.plot import Plot
from battle_stocks.classes.user import User

class Portfolio:
    def __init__(self):
        self.stocks = []
        self.past_stocks = []
        self.portfolio_value = portfolio_value
        self.loss_gain = loss_gain

    def add_stock(self, symbol, qty):
        add_stock = Transaction.buy_stock(symbol, qty)
        self.stocks.append(add_stock)
       
    def remove_stock(self, symbol, qty):
        remove_stock = Transaction.sell_stock(symbol, qty)
        if symbol not in self.stocks:
            print(f'You do not own any {symbol} stocks.')
        else:
            self.stocks.pop(remove_stock)

    def plot_single_stock(self, stock):
        return Plot.plot_single_stock(stock)

    def plot_portfolio(self):
        return Plot.plot_portfolio()

    def get_stock_info(self, stock_symbol): 
        return get_current_stock_price(stock_symbol)

    def get_portfolio_value(self):
        # need to add total values and stocks
        for stock in self.stocks:
             stock_current_total = stock.current_total_value()
             self.portfolio_value += stock_current_total
        return self.portfolio_value

    def gain_loss(self):
        for stock in self.stocks:
            stock_diff = stock.get_price_diff()
            self.loss_gain += stock_diff
        return self.loss_gain
       
# if __name__ == "__main__":
#     portfo = Portfolio()
#     _add = portfo.add_stock('AAPL')
#     _remove = portfo.remove_stock('AAPL')
#     print(_add)
#     print(_remove)