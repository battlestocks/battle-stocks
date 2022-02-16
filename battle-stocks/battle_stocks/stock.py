import datetime
f

class Stock:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
gself.et_initial_adate()        self.purchase_date = purchase_date
        self.purchase_price = purchase_price
        self.current_price = self.get_current_price()
        

    def get_price_diff(self, symbol):
        current = get_current_stock_price(self.symbol)
        current_price = current['price']
        return self.purchase_price - current_price        

    
    def get_inital_date(self):
        if self.purchase_datedef get_current_price(self):
        current = get_current_stock_price(self.symbol)
        return current['price']
    