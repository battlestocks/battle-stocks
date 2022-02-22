from battle_stocks.classes.plot import Plot

class Portfolio:
    def __init__(self):
        self.stocks = []
        self.held_stocks = []
        self.stock_shares = {}
        self.portfolio_value = self.get_portfolio_value()
    
    def add_stock(self, transaction):
        if transaction.name in self.held_stocks:
            self.stocks.append(transaction)
            self.held_stocks.append(transaction.name)
            self.stock_shares[transaction.symbol] += transaction.qty
        else:
            self.stocks.append(transaction)
            self.held_stocks.append(transaction.name)
            self.stock_shares[transaction.symbol] = transaction.qty


    def remove_stock(self, transaction):
        # WIP
        pass
    

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
