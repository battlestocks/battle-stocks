from battle_stocks.classes.transaction import Transaction
from battle_stocks.classes.user import User

class Portfolio:
    def __init__(self):
        self.stocks = []
        self.past_stocks = []
        self.portfolio_value = portfolio_value

    def add_stock(self, symbol, qty):
        add_stock = Transaction.buy_stock(symbol, qty)
        self.stocks.append(add_stock)
       
    def remove_stock(self, symbol, qty):
        remove_stock = Transaction.sell_stock(symbol, qty)
        if symbol not in self.stocks:
            print(f'You do not have {symbol} in your portfolio')
        else:
            self.stocks.pop(remove_stock)

    def plot_single_stock(self):
        pass

    def plot_portfolio():
        pass

    def get_stock_info(self, stock_symbol):
        pass

    def get_portfolio_value(self, user):
        # need to add total values and stocks
        return self.portfolio_value

    def gain_loss(self):
        pass

# if __name__ == "__main__":
#     portfo = Portfolio()
#     added = portfo.add_stock('AAPL')
#     removed = portfo.remove_stock('AAPL')
#     print(added)
#     print(removed)