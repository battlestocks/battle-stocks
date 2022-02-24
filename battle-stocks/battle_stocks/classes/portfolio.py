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
            self.stock_shares[transaction.name] += transaction.qty
        else:
            self.stocks.append(transaction)
            self.held_stocks.append(transaction.name)
            self.stock_shares[transaction.name] = transaction.qty

    def sell_shares(self, name, symbol, qty):
        shares = int(qty)
        value = 0
        stock_to_sell = 0
        current_amount = self.stock_shares[name]
        if int(current_amount) < shares:
            return 0

        stock_transactions = [ stock for stock in self.stocks if stock.name == name ]
        while stock_to_sell != shares:
            for stock in stock_transactions:
                if int(stock.qty) < int(shares):
                    self.stock_shares[name] = int(self.stock_shares[name]) - shares
                    value += stock.sell_stock(shares)
                    stock_to_sell += shares
                    self.held_stocks.remove(name)
                else:
                    self.stock_shares[name] = int(self.stock_shares[name]) - shares
                    value += stock.sell_stock(shares)
                    stock_to_sell += shares
        if self.stock_shares[name] == 0:
            self.held_stocks.remove(name)
        return value

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
