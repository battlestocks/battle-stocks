from battle_stocks.classes.transaction import Transaction
from battle_stocks.classes.stock import get_current_stock_price
from battle_stocks.classes.plot import Plot


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
        self.portfolio_value = self.get_portfolio_value()
        # self.loss_gain = loss_gain

    def add_stock(self, stock):
        self.stocks.append(stock)

    def plot_single_stock(self, stock):
        return Plot.plot_single_stock(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def plot_portfolio(self):
        return Plot.plot_portfolio(self.stocks)

    def get_stock_info(self, stock_symbol): 
        return get_current_stock_price(stock_symbol)

    def get_portfolio_value(self):
        updated_value = 0
        for stock in self.stocks:
             stock_current_total = stock.current_total_value()
             updated_value += stock_current_total
        return updated_value

    def gain_loss(self):
        diff = 0
        for stock in self.stocks:
            stock_diff = stock.overall_performance()
            diff += stock_diff
        return diff

