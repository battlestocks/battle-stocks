import datetime

# Webscarp function returns dict
def get_current_stock_price(symbol):
    return { 'price' : 100 }

class Stock:
    def __init__(self, name, symbol, created=None, price=None):
        self.name = name
        self.symbol = symbol
        self.purchased_price = self.set_initial_purchased_price()
        self.purchased_date =  created or datetime.datetime.now().date()
        self.current_price = get_current_stock_price(self.symbol)
        

    def set_initial_purchased_price(self):
        current = get_current_stock_price(self.symbol)
        return current['price']

    def get_price_diff(self):
        current = get_current_stock_price(self.symbol)
        current_price = current['price']
        return self.purchased_price - current_price       

    # def set_date_purchased(self):
    #     if self.initialized == 0:
    #         self.initialized = 1
    #         return datetime.datetime.now()

