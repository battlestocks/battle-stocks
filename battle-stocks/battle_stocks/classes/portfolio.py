from battle_stocks.classes.stock import get_current_stock_price
from battle_stocks.classes.plot import Plot


class Portfolio:
    def __init__(self):
        self.stocks = []
        self.past_stocks = []
        self.portfolio_value = self.get_portfolio_value()
        # self.loss_gain = loss_gain
    
    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def plot_portfolio(self):
        return Plot.plot_portfolio(self.stocks)


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
